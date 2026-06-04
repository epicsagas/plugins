"""Obsidian-forge Hermes Agent plugin registration."""

from __future__ import annotations

from typing import Any

from . import schemas
from . import tools


def register(ctx: Any) -> None:
    """Wire tool schemas to their handlers via the provided context.

    ``ctx`` is expected to expose ``register_tool(schema, handler)``.
    """
    for schema in schemas.ALL_SCHEMAS:
        name = schema["name"]
        handler = tools.HANDLERS[name]
        ctx.register_tool(
            name, toolset="obsidian-forge", schema=schema, handler=handler
        )
