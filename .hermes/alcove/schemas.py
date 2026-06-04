"""JSON Schema tool definitions for the alcove Hermes plugin."""

alcove_search_docs = {
    "name": "alcove_search_docs",
    "description": (
        "Search across project documentation using alcove's BM25-ranked index. "
        "Use this when the user asks about project architecture, conventions, "
        "decisions, code structure, tech debt, or any topic covered in docs. "
        "Falls back to grep-based substring matching when no index exists."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query — keywords, phrases, or topic to find in docs.",
            },
            "scope": {
                "type": "string",
                "description": (
                    "Search scope: 'project' searches only the current project's docs, "
                    "'global' searches across all projects in the doc repository."
                ),
                "enum": ["project", "global"],
                "default": "project",
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of results to return.",
                "default": 20,
            },
        },
        "required": ["query"],
    },
}

alcove_lint_docs = {
    "name": "alcove_lint_docs",
    "description": (
        "Lint project documentation for quality issues: broken links, orphaned files, "
        "stale markers (WIP, TODO, FIXME, DRAFT, DEPRECATED), and stale year references. "
        "Use this when the user asks to check doc hygiene, find broken links, "
        "or locate stale content."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "project": {
                "type": "string",
                "description": (
                    "Project name to lint. Omit to lint all projects."
                ),
            },
        },
        "required": [],
    },
}

alcove_validate_docs = {
    "name": "alcove_validate_docs",
    "description": (
        "Validate current project documentation against the team policy defined in "
        "policy.toml. Checks that required files exist, template placeholders are filled, "
        "required section headings are present, and lists meet minimum item counts. "
        "Use this when the user asks to verify doc completeness before a release."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
}

alcove_rebuild_index = {
    "name": "alcove_rebuild_index",
    "description": (
        "Rebuild the alcove search index from scratch. Use this when search results "
        "seem stale, after major doc changes, or when the index is corrupted. "
        "For incremental updates, prefer the lighter index command."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
}

alcove_doctor = {
    "name": "alcove_doctor",
    "description": (
        "Check alcove installation health — verifies CLI availability, doc repository "
        "access, index status, and configuration. Use this when diagnosing alcove "
        "issues or confirming the environment is set up correctly."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
}

ALL_SCHEMAS = [
    alcove_search_docs,
    alcove_lint_docs,
    alcove_validate_docs,
    alcove_rebuild_index,
    alcove_doctor,
]
