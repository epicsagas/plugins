"""Tool handlers for the alcove Hermes plugin."""

from __future__ import annotations

import json
import subprocess


def _alcove(*args: str, input_data: str | None = None) -> str:
    """Run an alcove CLI command and return its stdout.

    Raises subprocess.CalledProcessError on non-zero exit,
    subprocess.TimeoutExpired if the command exceeds 30 seconds.
    """
    result = subprocess.run(
        ["alcove", *args],
        capture_output=True,
        text=True,
        timeout=30,
        input=input_data,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(stderr or f"alcove exited with code {result.returncode}")
    return result.stdout.strip()


def _ok(data: object) -> str:
    """Wrap a successful result as JSON."""
    return json.dumps({"ok": data})


def _err(message: str) -> str:
    """Wrap an error result as JSON."""
    return json.dumps({"error": message})


# ---------- handlers ----------


def search_docs(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Search project documentation."""
    try:
        query = args["query"]
        cmd = ["search", "--query", query]

        scope = args.get("scope", "project")
        cmd.extend(["--scope", scope])

        limit = args.get("limit", 20)
        cmd.extend(["--limit", str(limit)])

        output = _alcove(*cmd)
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def lint_docs(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Lint project documentation."""
    try:
        cmd = ["lint"]
        project = args.get("project")
        if project:
            cmd.extend(["--project", project])
        output = _alcove(*cmd)
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def validate_docs(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Validate documentation against policy."""
    try:
        output = _alcove("validate")
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def rebuild_index(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Rebuild the search index from scratch."""
    try:
        output = _alcove("rebuild")
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


def doctor(args: dict, **kwargs) -> str:  # noqa: ARG001
    """Check alcove installation health."""
    try:
        output = _alcove("doctor")
        return _ok(output)
    except Exception as exc:
        return _err(str(exc))


# ---------- mapping ----------

HANDLERS: dict[str, callable] = {
    "alcove_search_docs": search_docs,
    "alcove_lint_docs": lint_docs,
    "alcove_validate_docs": validate_docs,
    "alcove_rebuild_index": rebuild_index,
    "alcove_doctor": doctor,
}
