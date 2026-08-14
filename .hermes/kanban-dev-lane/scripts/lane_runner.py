#!/usr/bin/env python3
"""lane_runner.py — Autonomous Multi-Engine Implementation Lane Runner with Fallback.

Executes implementation tasks in an isolated git worktree with automatic failover:
  1. Primary: claudy -p "<prompt>" --yolo
  2. Fallback 1: codex exec "<prompt>" < /dev/null --dangerously-bypass-approvals-and-sandbox --ephemeral (or codex --yolo)
  3. Fallback 2: agy --dangerously-skip-permissions -p "<prompt>" (agyd)
  4. Final Fallback: Return structured report to Hermes worker for direct resolution.

Handles quota exhaustion, rate limits (429), process timeouts, and crash recovery.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Regex patterns that indicate quota / rate-limit / balance exhaustion across providers
QUOTA_ERROR_PATTERNS = [
    r"rate[_\s-]?limit",
    r"429\b",
    r"insufficient[_\s-]?quota",
    r"credit[_\s-]?balance[_\s-]?is[_\s-]?too[_\s-]?low",
    r"exceeded[_\s-]?your[_\s-]?current[_\s-]?quota",
    r"usage[_\s-]?limit[_\s-]?reached",
    r"resource[_\s-]?has[_\s-]?been[_\s-]?exhausted",
    r"resource_exhausted",
    r"overloaded[_\s-]?error",
    r"capacity[_\s-]?exhausted",
    r"monthly[_\s-]?budget[_\s-]?reached",
    r"billing[_\s-]?hard[_\s-]?limit",
    r"quota_exceeded",
    r"rate_limit_exceeded",
    r"daily[_\s-]?quota[_\s-]?reached",
    r"tokens[_\s-]?per[_\s-]?minute[_\s-]?limit",
    r"requests[_\s-]?per[_\s-]?minute[_\s-]?limit",
]
QUOTA_REGEX = re.compile("|".join(QUOTA_ERROR_PATTERNS), re.IGNORECASE)


@dataclass
class EngineResult:
    engine: str
    command: str
    exit_code: int
    duration_sec: float
    output: str
    error: str
    quota_exhausted: bool = False
    timed_out: bool = False
    success: bool = False


@dataclass
class LaneExecutionReport:
    task_id: str
    worktree: str
    branch: str
    attempted_engines: List[str] = field(default_factory=list)
    successful_engine: Optional[str] = None
    fallback_occurred: bool = False
    result: str = "failed"  # accepted | partial | rejected | timed_out | failed
    engine_results: List[Dict[str, Any]] = field(default_factory=list)
    accepted_commits: List[str] = field(default_factory=list)
    diff_stat: str = ""
    error_summary: Optional[str] = None
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def is_quota_error(text: str) -> bool:
    """Check if the error string or stdout/stderr contains quota exhaustion markers."""
    return bool(QUOTA_REGEX.search(text))


def check_engine_installed(engine: str) -> Tuple[bool, str]:
    """Verify if engine CLI is installed and return its path/version."""
    cli_map = {
        "claudy": "claudy",
        "codex": "codex",
        "agyd": "agy",  # agyd is alias for 'agy --dangerously-skip-permissions'
        "agy": "agy",
    }
    target = cli_map.get(engine, engine)
    path = shutil.which(target)
    if not path:
        return False, f"Command '{target}' not found in PATH"
    return True, path


def build_engine_command(engine: str, prompt_text: str, worktree: str) -> List[str]:
    """Construct non-interactive shell command list for the specified engine."""
    if engine == "claudy":
        return ["claudy", "-p", prompt_text, "--yolo"]
    elif engine == "codex":
        return [
            "codex",
            "exec",
            prompt_text,
            "--dangerously-bypass-approvals-and-sandbox",
            "--ephemeral",
        ]
    elif engine in ("agyd", "agy"):
        return ["agy", "--dangerously-skip-permissions", "-p", prompt_text]
    else:
        raise ValueError(f"Unknown engine: {engine}")


def run_engine_in_worktree(
    engine: str,
    prompt_text: str,
    worktree: str,
    timeout: int = 600,
) -> EngineResult:
    """Executes a single engine in the worktree directory with timeout and quota inspection."""
    installed, reason = check_engine_installed(engine)
    if not installed:
        return EngineResult(
            engine=engine,
            command="",
            exit_code=127,
            duration_sec=0.0,
            output="",
            error=reason,
            quota_exhausted=False,
            timed_out=False,
            success=False,
        )

    cmd = build_engine_command(engine, prompt_text, worktree)
    start_time = time.time()
    timed_out = False
    quota_exhausted = False
    stdout_text = ""
    stderr_text = ""
    exit_code = -1

    try:
        with open(os.devnull, "r") as devnull:
            proc = subprocess.run(
                cmd,
                cwd=worktree,
                stdin=devnull,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=timeout,
                env=os.environ.copy(),
            )
            exit_code = proc.returncode
            stdout_text = proc.stdout or ""
            stderr_text = proc.stderr or ""
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        exit_code = 124
        stdout_text = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr_text = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        stderr_text += f"\nProcess timed out after {timeout} seconds."
    except Exception as exc:
        exit_code = 1
        stderr_text = str(exc)

    duration = time.time() - start_time
    combined_output = f"{stdout_text}\n{stderr_text}"

    if is_quota_error(combined_output):
        quota_exhausted = True

    success = (exit_code == 0) and not quota_exhausted and not timed_out

    return EngineResult(
        engine=engine,
        command=" ".join(cmd),
        exit_code=exit_code,
        duration_sec=round(duration, 2),
        output=stdout_text,
        error=stderr_text,
        quota_exhausted=quota_exhausted,
        timed_out=timed_out,
        success=success,
    )


def get_git_diff_and_commits(worktree: str) -> Tuple[str, List[str]]:
    """Inspects worktree for git diff stat and recent commit SHAs."""
    diff_stat = ""
    commits: List[str] = []
    try:
        res = subprocess.run(
            ["git", "-C", worktree, "diff", "--stat"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        diff_stat = res.stdout.strip()

        res_log = subprocess.run(
            ["git", "-C", worktree, "log", "-n", "5", "--format=%H %s"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        if res_log.stdout:
            commits = [line.strip() for line in res_log.stdout.splitlines() if line.strip()]
    except Exception:
        pass
    return diff_stat, commits


def execute_lane_with_fallback(
    prompt_text: str,
    worktree: str,
    task_id: str = "t_manual",
    branch: str = "",
    engines: Optional[List[str]] = None,
    timeout_per_engine: int = 600,
) -> LaneExecutionReport:
    """Orchestrates fallback execution across the engine chain: claudy -> codex -> agyd."""
    if engines is None:
        engines = ["claudy", "codex", "agyd"]

    report = LaneExecutionReport(
        task_id=task_id,
        worktree=worktree,
        branch=branch,
    )

    for idx, engine in enumerate(engines):
        report.attempted_engines.append(engine)
        print(f"🚀 [Lane Runner] Starting engine ({idx+1}/{len(engines)}): {engine}...", file=sys.stderr)

        res = run_engine_in_worktree(
            engine=engine,
            prompt_text=prompt_text,
            worktree=worktree,
            timeout=timeout_per_engine,
        )
        report.engine_results.append(asdict(res))

        if res.success:
            print(f"✅ [Lane Runner] Engine '{engine}' completed successfully in {res.duration_sec}s.", file=sys.stderr)
            report.successful_engine = engine
            report.result = "accepted"
            diff_stat, commits = get_git_diff_and_commits(worktree)
            report.diff_stat = diff_stat
            report.accepted_commits = commits
            return report

        if res.quota_exhausted:
            print(
                f"⚠️ [Lane Runner] Engine '{engine}' exhausted quota / hit rate limits (Exit {res.exit_code}). Failing over...",
                file=sys.stderr,
            )
            report.fallback_occurred = True
        elif res.timed_out:
            print(f"⏱️ [Lane Runner] Engine '{engine}' timed out ({timeout_per_engine}s). Failing over...", file=sys.stderr)
            report.fallback_occurred = True
        else:
            print(
                f"❌ [Lane Runner] Engine '{engine}' failed with exit code {res.exit_code}. Failing over...",
                file=sys.stderr,
            )
            report.fallback_occurred = True

    report.result = "failed"
    report.error_summary = "All delegation engines failed or exhausted quota. Fallback to Hermes direct worker."
    print("⛔ [Lane Runner] All engines failed. Returning control to Hermes direct worker.", file=sys.stderr)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Multi-engine implementation lane runner with fallback.")
    parser.add_argument("--prompt-file", "-f", help="Path to prompt markdown file")
    parser.add_argument("--prompt", "-p", help="Inline prompt string")
    parser.add_argument("--worktree", "-w", required=True, help="Target git worktree directory")
    parser.add_argument("--task-id", "-t", default="t_manual", help="Kanban Task ID")
    parser.add_argument("--branch", "-b", default="", help="Git branch name")
    parser.add_argument("--engines", "-e", default="claudy,codex,agyd", help="Comma-separated engine fallback list")
    parser.add_argument("--timeout", type=int, default=600, help="Timeout in seconds per engine")
    parser.add_argument("--output-json", "-o", help="Optional path to write JSON execution report")

    args = parser.parse_args()

    prompt_text = ""
    if args.prompt_file:
        with open(args.prompt_file, "r", encoding="utf-8") as f:
            prompt_text = f.read()
    elif args.prompt:
        prompt_text = args.prompt
    else:
        prompt_text = sys.stdin.read()

    if not prompt_text.strip():
        print("Error: Prompt content cannot be empty.", file=sys.stderr)
        return 1

    engines = [e.strip() for e in args.engines.split(",") if e.strip()]
    report = execute_lane_with_fallback(
        prompt_text=prompt_text,
        worktree=args.worktree,
        task_id=args.task_id,
        branch=args.branch,
        engines=engines,
        timeout_per_engine=args.timeout,
    )

    json_str = json.dumps(report.to_dict(), indent=2, ensure_ascii=False)
    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as f:
            f.write(json_str)

    print(json_str)
    return 0 if report.successful_engine else 2


if __name__ == "__main__":
    sys.exit(main())
