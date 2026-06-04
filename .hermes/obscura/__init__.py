"""Obscura Hermes Agent plugin registration."""

from __future__ import annotations

from typing import Any

from . import schemas
from . import tools

_HANDLERS = {
    "obscura_fetch_page": tools.obscura_fetch_page,
    "obscura_scrape_urls": tools.obscura_scrape_urls,
    "obscura_extract_markdown": tools.obscura_extract_markdown,
}


def register(ctx: Any) -> None:
    """Wire tool schemas to their handlers via the provided context.

    ``ctx`` is expected to expose ``register_tool(schema, handler)``.
    """
    for schema in schemas.ALL_SCHEMAS:
        name = schema["name"]
        handler = _HANDLERS[name]
        ctx.register_tool(name, toolset="obscura", schema=schema, handler=handler)
