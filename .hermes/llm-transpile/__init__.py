"""llm-transpile Hermes Agent plugin — registration entry point."""

from .schemas import TOOL_SCHEMAS
from .tools import transpile_file, transpile_stats

_HANDLERS = {
    "transpile_file": transpile_file,
    "transpile_stats": transpile_stats,
}


def register(ctx):
    """Register llm-transpile tools with the Hermes agent context.

    Parameters
    ----------
    ctx : object
        Plugin context that exposes ``register_tool(name, schema, handler)``.
    """
    for name, schema in TOOL_SCHEMAS.items():
        handler = _HANDLERS[name]
        ctx.register_tool(name, toolset="llm-transpile", schema=schema, handler=handler)
