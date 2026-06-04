"""Tool handlers for epic-harness CLI commands."""

from __future__ import annotations

import json
import subprocess


_TIMEOUT = 15


def _harness(*args: str) -> str:
    """Run epic-harness with the given arguments and return stdout."""
    result = subprocess.run(
        ["epic-harness", *args],
        capture_output=True,
        text=True,
        timeout=_TIMEOUT,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(stderr or f"epic-harness exited with code {result.returncode}")
    return result.stdout.strip()


def _ok(data: object) -> str:
    return json.dumps({"status": "ok", "output": data})


def _err(exc: Exception) -> str:
    return json.dumps({"error": str(exc)})


# ── Memory CRUD ────────────────────────────────────────────────────────


def harness_mem_add(args: dict, **kwargs) -> str:
    """Add a new memory node."""
    try:
        cmd = ["mem", "add", "--title", args["title"]]
        if args.get("type"):
            cmd.extend(["--type", args["type"]])
        if args.get("tags"):
            cmd.extend(["--tags", args["tags"]])
        if args.get("project"):
            cmd.extend(["--project", args["project"]])
        if args.get("body"):
            cmd.extend(["--body", args["body"]])
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)


def harness_mem_search(args: dict, **kwargs) -> str:
    """Full-text search across memory nodes."""
    try:
        return _ok(_harness("mem", "search", args["query"]))
    except Exception as exc:
        return _err(exc)


def harness_mem_recall(args: dict, **kwargs) -> str:
    """Smart recall with relevance scoring."""
    try:
        hint = args.get("hint")
        if hint:
            return _ok(_harness("mem", "recall", hint))
        return _ok(_harness("mem", "recall"))
    except Exception as exc:
        return _err(exc)


def harness_mem_list(args: dict, **kwargs) -> str:
    """List memory nodes with optional filtering."""
    try:
        cmd = ["mem", "list"]
        if args.get("type"):
            cmd.extend(["--type", args["type"]])
        cmd.extend(["--limit", str(args.get("limit", 20))])
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)


def harness_mem_related(args: dict, **kwargs) -> str:
    """Find related nodes via graph traversal."""
    try:
        return _ok(_harness("mem", "related", args["node_id"]))
    except Exception as exc:
        return _err(exc)


def harness_mem_edit(args: dict, **kwargs) -> str:
    """Edit an existing memory node."""
    try:
        cmd = ["mem", "edit", args["node_id"]]
        if args.get("title"):
            cmd.extend(["--title", args["title"]])
        if args.get("type"):
            cmd.extend(["--type", args["type"]])
        if args.get("tags"):
            cmd.extend(["--tags", args["tags"]])
        if args.get("body"):
            cmd.extend(["--body", args["body"]])
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)


def harness_mem_remove(args: dict, **kwargs) -> str:
    """Remove a memory node and its edges."""
    try:
        return _ok(_harness("mem", "remove", args["node_id"]))
    except Exception as exc:
        return _err(exc)


def harness_mem_link(args: dict, **kwargs) -> str:
    """Create a directed edge between two nodes."""
    try:
        cmd = ["mem", "link", args["source_id"], args["target_id"]]
        if args.get("relation"):
            cmd.extend(["--relation", args["relation"]])
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)


def harness_mem_context(args: dict, **kwargs) -> str:
    """Show recently-updated nodes for a project."""
    try:
        cmd = ["mem", "context"]
        if args.get("project"):
            cmd.extend(["--project", args["project"]])
        cmd.extend(["--limit", str(args.get("limit", 5))])
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)


def harness_mem_export(args: dict, **kwargs) -> str:
    """Export all nodes to Markdown files."""
    try:
        cmd = ["mem", "export"]
        if args.get("out"):
            cmd.extend(["--out", args["out"]])
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)


def harness_mem_validate(args: dict, **kwargs) -> str:
    """Validate all node files for parse errors."""
    try:
        return _ok(_harness("mem", "validate"))
    except Exception as exc:
        return _err(exc)


def harness_mem_graph_rebuild(args: dict, **kwargs) -> str:
    """Rebuild the graph cache."""
    try:
        return _ok(_harness("mem", "graph", "rebuild"))
    except Exception as exc:
        return _err(exc)


# ── Team / Org ─────────────────────────────────────────────────────────


def harness_team_list(args: dict, **kwargs) -> str:
    """List all agent teams in the current org."""
    try:
        return _ok(_harness("team", "list"))
    except Exception as exc:
        return _err(exc)


def harness_team_show(args: dict, **kwargs) -> str:
    """Show details of a specific team."""
    try:
        return _ok(_harness("team", "show", args["team"]))
    except Exception as exc:
        return _err(exc)


def harness_team_sync(args: dict, **kwargs) -> str:
    """Sync team agents to .claude/agents/."""
    try:
        cmd = ["team", "sync", args["team"]]
        if args.get("global"):
            cmd.append("--global")
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)


# ── Reflect ────────────────────────────────────────────────────────────


def harness_reflect_context(args: dict, **kwargs) -> str:
    """Collect harness session data as structured JSON."""
    try:
        cmd = ["reflect", "--context"]
        if args.get("days"):
            cmd.extend(["--days", str(args["days"])])
        if args.get("project"):
            cmd.extend(["--project", args["project"]])
        return _ok(_harness(*cmd))
    except Exception as exc:
        return _err(exc)
