"""Episteme Hermes Agent plugin registration."""

from __future__ import annotations

from typing import Any

from . import schemas
from . import tools

_HANDLERS = {
    "episteme_search_knowledge": tools.episteme_search_knowledge,
    "episteme_analyze_code": tools.episteme_analyze_code,
    "episteme_suggest_refactorings": tools.episteme_suggest_refactorings,
    "episteme_get_entity": tools.episteme_get_entity,
}


def register(ctx: Any) -> None:
    """Wire tool schemas to their handlers via the provided context.

    ``ctx`` is expected to expose ``register_tool(schema, handler)``.
    """
    for schema in schemas.ALL_SCHEMAS:
        name = schema["name"]
        handler = _HANDLERS[name]
        ctx.register_tool(name, toolset="episteme", schema=schema, handler=handler)
