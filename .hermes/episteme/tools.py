"""Tool handlers for the Episteme Hermes Agent plugin.

Uses only Python 3.10+ stdlib (urllib.request).  Requires ``epis serve``
to be running (default http://localhost:8731).
"""

from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from typing import Any

_TIMEOUT = 10  # seconds


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _base_url() -> str:
    """Return the Episteme API base URL from env or default."""
    return os.environ.get("EPISTEME_URL", "http://localhost:8731")


def _epis_get(path: str, params: dict[str, str] | None = None) -> str:
    """Perform a GET request and return the raw JSON string."""
    url = _base_url().rstrip("/") + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, method="GET")
    req.add_header("Accept", "application/json")
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
        return resp.read().decode("utf-8")


def _epis_post(path: str, body_dict: dict[str, Any]) -> str:
    """Perform a POST request with a JSON body and return the raw JSON string."""
    url = _base_url().rstrip("/") + path
    data = json.dumps(body_dict).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    with urllib.request.urlopen(req, timeout=_TIMEOUT) as resp:
        return resp.read().decode("utf-8")


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
def episteme_search_knowledge(args: dict, **kwargs) -> str:
    """Search the Episteme knowledge graph."""
    query = args["query"]
    return _epis_get("/search", params={"q": query})


@_safe
def episteme_analyze_code(args: dict, **kwargs) -> str:
    """Analyze source code for smells."""
    code = args["code"]
    language = args.get("language", "")
    body: dict[str, Any] = {"code": code}
    if language:
        body["language"] = language
    return _epis_post("/analyze", body)


@_safe
def episteme_suggest_refactorings(args: dict, **kwargs) -> str:
    """Suggest refactorings for source code."""
    code = args["code"]
    language = args.get("language", "")
    body: dict[str, Any] = {"code": code}
    if language:
        body["language"] = language
    return _epis_post("/refactor", body)


@_safe
def episteme_get_entity(args: dict, **kwargs) -> str:
    """Retrieve an entity by ID."""
    entity_id = args["entity_id"]
    return _epis_get(f"/graph/{urllib.parse.quote(entity_id, safe='')}")
