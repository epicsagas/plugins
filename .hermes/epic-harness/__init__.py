"""epic-harness Hermes plugin — register memory tools."""

from __future__ import annotations

from .schemas import SCHEMAS
from .tools import (
    harness_mem_add,
    harness_mem_list,
    harness_mem_recall,
    harness_mem_related,
    harness_mem_search,
)

_HANDLERS = {
    "harness_mem_add": harness_mem_add,
    "harness_mem_search": harness_mem_search,
    "harness_mem_recall": harness_mem_recall,
    "harness_mem_list": harness_mem_list,
    "harness_mem_related": harness_mem_related,
}


def register(ctx):
    """Register all epic-harness memory tools with the Hermes context."""
    for tool_name, schema in SCHEMAS.items():
        handler = _HANDLERS[tool_name]
        ctx.register_tool(tool_name, schema=schema, handler=handler)
