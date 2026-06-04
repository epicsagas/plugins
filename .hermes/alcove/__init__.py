"""Alcove Hermes plugin — registers alcove CLI tools."""

from __future__ import annotations

from .schemas import ALL_SCHEMAS
from .tools import HANDLERS


def register(ctx) -> None:
    """Register all alcove tools with the Hermes agent context.

    Parameters
    ----------
    ctx : object
        Agent context that provides ``register_tool(name, schema, handler)``.
    """
    for schema in ALL_SCHEMAS:
        name = schema["name"]
        handler = HANDLERS[name]
        ctx.register_tool(name=name, schema=schema, handler=handler)
