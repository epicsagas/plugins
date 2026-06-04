"""JSON Schema definitions for epic-harness memory tools."""

SCHEMAS = {
    "harness_mem_add": {
        "name": "harness_mem_add",
        "description": "Add a new memory node to the epic-harness unified memory graph.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title or summary of the memory node.",
                },
                "type": {
                    "type": "string",
                    "description": "Node classification.",
                    "enum": ["concept", "decision", "pattern", "task", "bug", "insight"],
                    "default": "concept",
                },
            },
            "required": ["title"],
        },
    },
    "harness_mem_search": {
        "name": "harness_mem_search",
        "description": "Full-text search across all memory nodes in the unified memory graph.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query string.",
                },
            },
            "required": ["query"],
        },
    },
    "harness_mem_recall": {
        "name": "harness_mem_recall",
        "description": "Smart recall with relevance scoring (recency 25%, importance 35%, access frequency 15%, full-text search 25%).",
        "parameters": {
            "type": "object",
            "properties": {
                "hint": {
                    "type": "string",
                    "description": "Describe current task context for relevance ranking.",
                },
            },
            "required": [],
        },
    },
    "harness_mem_list": {
        "name": "harness_mem_list",
        "description": "List memory nodes, optionally filtered by type.",
        "parameters": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "Filter nodes by type.",
                    "enum": ["concept", "decision", "pattern", "task", "bug", "insight"],
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of nodes to return.",
                    "default": 20,
                },
            },
            "required": [],
        },
    },
    "harness_mem_related": {
        "name": "harness_mem_related",
        "description": "Find related memory nodes via BFS graph traversal starting from a given node.",
        "parameters": {
            "type": "object",
            "properties": {
                "node_id": {
                    "type": "string",
                    "description": "ID of the source memory node to traverse from.",
                },
            },
            "required": ["node_id"],
        },
    },
}
