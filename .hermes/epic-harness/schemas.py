"""JSON Schema definitions for epic-harness tools."""

SCHEMAS = {
    # ── Memory CRUD ────────────────────────────────────────────────────
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
                    "enum": [
                        "concept", "decision", "pattern",
                        "task", "bug", "insight",
                    ],
                    "default": "concept",
                },
                "tags": {
                    "type": "string",
                    "description": "Comma-separated tags.",
                },
                "project": {
                    "type": "string",
                    "description": "Associate with a project slug.",
                },
                "body": {
                    "type": "string",
                    "description": "Node body content (markdown).",
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
        "description": "Smart recall with relevance scoring (recency 25%, importance 35%, access frequency 15%, full-text search 25%). Use before starting a task to surface relevant past decisions and patterns.",
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
                    "enum": [
                        "concept", "decision", "pattern",
                        "task", "bug", "insight",
                    ],
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
    "harness_mem_edit": {
        "name": "harness_mem_edit",
        "description": "Edit an existing memory node's title, type, tags, or body content.",
        "parameters": {
            "type": "object",
            "properties": {
                "node_id": {
                    "type": "string",
                    "description": "ID of the node to edit.",
                },
                "title": {
                    "type": "string",
                    "description": "New title.",
                },
                "type": {
                    "type": "string",
                    "description": "New node type.",
                    "enum": [
                        "concept", "decision", "pattern",
                        "task", "bug", "insight",
                    ],
                },
                "tags": {
                    "type": "string",
                    "description": "Replace tags (comma-separated).",
                },
                "body": {
                    "type": "string",
                    "description": "Replace body content.",
                },
            },
            "required": ["node_id"],
        },
    },
    "harness_mem_remove": {
        "name": "harness_mem_remove",
        "description": "Remove a memory node and all its edges from the graph.",
        "parameters": {
            "type": "object",
            "properties": {
                "node_id": {
                    "type": "string",
                    "description": "ID of the node to remove.",
                },
            },
            "required": ["node_id"],
        },
    },
    "harness_mem_link": {
        "name": "harness_mem_link",
        "description": "Create a directed edge between two memory nodes.",
        "parameters": {
            "type": "object",
            "properties": {
                "source_id": {
                    "type": "string",
                    "description": "Source node ID.",
                },
                "target_id": {
                    "type": "string",
                    "description": "Target node ID.",
                },
                "relation": {
                    "type": "string",
                    "description": "Edge label (e.g. 'related', 'depends_on', 'supersedes').",
                    "default": "related",
                },
            },
            "required": ["source_id", "target_id"],
        },
    },
    "harness_mem_context": {
        "name": "harness_mem_context",
        "description": "Show recently-updated memory nodes for a project — useful for session context restoration.",
        "parameters": {
            "type": "object",
            "properties": {
                "project": {
                    "type": "string",
                    "description": "Filter by project slug.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Max nodes to return.",
                    "default": 5,
                },
            },
            "required": [],
        },
    },
    "harness_mem_export": {
        "name": "harness_mem_export",
        "description": "Export all memory nodes to Markdown files for Git backup and diffing.",
        "parameters": {
            "type": "object",
            "properties": {
                "out": {
                    "type": "string",
                    "description": "Output directory (default: ~/.harness/exports).",
                },
            },
            "required": [],
        },
    },
    "harness_mem_validate": {
        "name": "harness_mem_validate",
        "description": "Validate all memory node files for parse errors.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    "harness_mem_graph_rebuild": {
        "name": "harness_mem_graph_rebuild",
        "description": "Rebuild the graph cache from current nodes and edges.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    # ── Team / Org ─────────────────────────────────────────────────────
    "harness_team_list": {
        "name": "harness_team_list",
        "description": "List all agent teams in the current org.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    "harness_team_show": {
        "name": "harness_team_show",
        "description": "Show details of a specific agent team.",
        "parameters": {
            "type": "object",
            "properties": {
                "team": {
                    "type": "string",
                    "description": "Team name to show.",
                },
            },
            "required": ["team"],
        },
    },
    "harness_team_sync": {
        "name": "harness_team_sync",
        "description": "Sync team agent definitions to .claude/agents/ directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "team": {
                    "type": "string",
                    "description": "Team name to sync.",
                },
                "global": {
                    "type": "boolean",
                    "description": "Sync to ~/.claude/agents/ instead of .claude/agents/.",
                    "default": False,
                },
            },
            "required": ["team"],
        },
    },
    # ── Reflect ────────────────────────────────────────────────────────
    "harness_reflect_context": {
        "name": "harness_reflect_context",
        "description": "Collect harness session data as structured JSON — analysis window, evolution stats, recent sessions, skill history. Use for self-assessment and skill evolution.",
        "parameters": {
            "type": "object",
            "properties": {
                "days": {
                    "type": "integer",
                    "description": "Analysis window in days (default: 30).",
                },
                "project": {
                    "type": "string",
                    "description": "Specific project slug.",
                },
            },
            "required": [],
        },
    },
}
