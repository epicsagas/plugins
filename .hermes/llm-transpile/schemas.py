"""JSON Schema definitions for llm-transpile tools."""

TRANSPILE_FILE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "transpile_file",
        "description": (
            "Convert a document to LLM-optimized format using the transpile CLI. "
            "Reduces token usage by up to 40%% while preserving semantic content."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "input_path": {
                    "type": "string",
                    "description": "Path to the input file to transpile.",
                },
                "format": {
                    "type": "string",
                    "enum": ["markdown", "html", "plaintext"],
                    "description": (
                        "Input format. When omitted, the format is auto-detected "
                        "from the file extension and content."
                    ),
                },
                "fidelity": {
                    "type": "string",
                    "enum": ["lossless", "semantic", "compressed"],
                    "description": (
                        "Transpilation fidelity level. "
                        "'lossless' preserves all content, 'semantic' keeps meaning "
                        "while removing redundancy, 'compressed' maximizes token savings. "
                        "Defaults to 'semantic'."
                    ),
                },
            },
            "required": ["input_path"],
        },
    },
}

TRANSPILE_STATS_SCHEMA = {
    "type": "function",
    "function": {
        "name": "transpile_stats",
        "description": (
            "Show transpile usage statistics as an ASCII table. "
            "Includes token savings, file counts, and per-agent breakdown."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "days": {
                    "type": "integer",
                    "description": "Number of days to look back for statistics. Defaults to 7.",
                },
                "agent": {
                    "type": "string",
                    "description": "Filter statistics to a specific agent name.",
                },
            },
        },
    },
}

TOOL_SCHEMAS = {
    "transpile_file": TRANSPILE_FILE_SCHEMA,
    "transpile_stats": TRANSPILE_STATS_SCHEMA,
}
