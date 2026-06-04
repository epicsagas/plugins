"""Tool handlers for the obscura Hermes Agent plugin.

Uses only Python 3.10+ stdlib (subprocess).  Requires ``obscura`` CLI
to be available on PATH.
"""

from __future__ import annotations

import json
import subprocess
from typing import Any

_TIMEOUT = 60  # seconds — web requests can be slow


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _obscura(*args: str) -> str:
    """Run ``obscura`` with the given arguments and return stdout."""
    result = subprocess.run(
        ["obscura", *args],
        capture_output=True,
        text=True,
        timeout=_TIMEOUT,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"obscura exited with code {result.returncode}")
    return result.stdout


def _safe(fn):  # noqa: ANN001 – decorator
    """Wrap a handler so *any* exception becomes ``{"error": "..."}``."""

    def wrapper(args: dict, **kwargs) -> str:
        try:
            return fn(args, **kwargs)
        except Exception as exc:  # noqa: BLE001
            return json.dumps({"error": str(exc)})

    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------

@_safe
def obscura_fetch_page(args: dict, **kwargs) -> str:
    """Fetch a single web page and return HTML, text, or links."""
    url = args["url"]
    dump = args.get("dump", "text")
    selector = args.get("selector")
    stealth = args.get("stealth", False)

    cmd_args: list[str] = ["fetch", url, "--dump", dump]
    if selector:
        cmd_args += ["--selector", selector]
    if stealth:
        cmd_args.append("--stealth")

    output = _obscura(*cmd_args)
    # If the output is already valid JSON, pass it through; otherwise wrap it.
    try:
        json.loads(output)
        return output
    except (json.JSONDecodeError, ValueError):
        return json.dumps({"result": output})


@_safe
def obscura_scrape_urls(args: dict, **kwargs) -> str:
    """Scrape multiple URLs in parallel."""
    urls = args["urls"]
    fmt = args.get("format", "json")
    concurrency = args.get("concurrency", 5)

    cmd_args: list[str] = [
        "scrape",
        *urls,
        "--format", fmt,
        "--concurrency", str(concurrency),
    ]

    output = _obscura(*cmd_args)
    try:
        json.loads(output)
        return output
    except (json.JSONDecodeError, ValueError):
        return json.dumps({"result": output})


@_safe
def obscura_extract_markdown(args: dict, **kwargs) -> str:
    """Fetch a URL and return clean markdown content."""
    url = args["url"]
    stealth = args.get("stealth", False)

    cmd_args: list[str] = ["fetch", url, "--dump", "text"]
    if stealth:
        cmd_args.append("--stealth")

    output = _obscura(*cmd_args)
    return json.dumps({"markdown": output})
