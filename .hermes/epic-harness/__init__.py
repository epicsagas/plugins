"""epic-harness Hermes plugin — register memory, team, and reflect tools."""

from __future__ import annotations

from .schemas import SCHEMAS
from .tools import (
    harness_mem_add,
    harness_mem_context,
    harness_mem_edit,
    harness_mem_export,
    harness_mem_graph_rebuild,
    harness_mem_link,
    harness_mem_list,
    harness_mem_recall,
    harness_mem_related,
    harness_mem_remove,
    harness_mem_search,
    harness_mem_validate,
    harness_reflect_context,
    harness_team_list,
    harness_team_show,
    harness_team_sync,
)

_HANDLERS = {
    "harness_mem_add": harness_mem_add,
    "harness_mem_search": harness_mem_search,
    "harness_mem_recall": harness_mem_recall,
    "harness_mem_list": harness_mem_list,
    "harness_mem_related": harness_mem_related,
    "harness_mem_edit": harness_mem_edit,
    "harness_mem_remove": harness_mem_remove,
    "harness_mem_link": harness_mem_link,
    "harness_mem_context": harness_mem_context,
    "harness_mem_export": harness_mem_export,
    "harness_mem_validate": harness_mem_validate,
    "harness_mem_graph_rebuild": harness_mem_graph_rebuild,
    "harness_team_list": harness_team_list,
    "harness_team_show": harness_team_show,
    "harness_team_sync": harness_team_sync,
    "harness_reflect_context": harness_reflect_context,
}


def register(ctx):
    """Register all epic-harness tools with the Hermes context."""
    for tool_name, schema in SCHEMAS.items():
        handler = _HANDLERS[tool_name]
        ctx.register_tool(
            tool_name, toolset="epic-harness", schema=schema, handler=handler
        )
