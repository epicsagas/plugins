"""Tool handlers for epic-harness memory commands."""

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


def harness_mem_add(args: dict, **kwargs) -> str:
    """Add a new memory node."""
    try:
        cmd_args = ["mem", "add"]
        title = args["title"]
        cmd_args.extend(["--title", title])

        node_type = args.get("type", "concept")
        cmd_args.extend(["--type", node_type])

        output = _harness(*cmd_args)
        return json.dumps({"status": "ok", "output": output})
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def harness_mem_search(args: dict, **kwargs) -> str:
    """Full-text search across memory nodes."""
    try:
        query = args["query"]
        output = _harness("mem", "search", query)
        return json.dumps({"status": "ok", "output": output})
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def harness_mem_recall(args: dict, **kwargs) -> str:
    """Smart recall with relevance scoring."""
    try:
        hint = args.get("hint")
        if hint:
            output = _harness("mem", "recall", hint)
        else:
            output = _harness("mem", "recall")
        return json.dumps({"status": "ok", "output": output})
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def harness_mem_list(args: dict, **kwargs) -> str:
    """List memory nodes with optional filtering."""
    try:
        cmd_args = ["mem", "list"]

        node_type = args.get("type")
        if node_type:
            cmd_args.extend(["--type", node_type])

        limit = args.get("limit", 20)
        cmd_args.extend(["--limit", str(limit)])

        output = _harness(*cmd_args)
        return json.dumps({"status": "ok", "output": output})
    except Exception as exc:
        return json.dumps({"error": str(exc)})


def harness_mem_related(args: dict, **kwargs) -> str:
    """Find related nodes via graph traversal."""
    try:
        node_id = args["node_id"]
        output = _harness("mem", "related", node_id)
        return json.dumps({"status": "ok", "output": output})
    except Exception as exc:
        return json.dumps({"error": str(exc)})
