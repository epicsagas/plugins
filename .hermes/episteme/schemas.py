"""JSON Schema definitions for Episteme Hermes Agent plugin tools."""

EPISTEME_SEARCH_KNOWLEDGE = {
    "name": "episteme_search_knowledge",
    "description": (
        "Search the Episteme knowledge graph for design patterns, "
        "software laws, code smells, and refactoring techniques."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query — e.g. 'singleton', 'god class', 'extract method'.",
            }
        },
        "required": ["query"],
    },
}

EPISTEME_ANALYZE_CODE = {
    "name": "episteme_analyze_code",
    "description": "Detect code smells and quality issues in source code using the Episteme knowledge graph.",
    "parameters": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "Source code to analyze.",
            },
            "language": {
                "type": "string",
                "description": "Programming language of the source code.",
                "enum": [
                    "python",
                    "java",
                    "go",
                    "rust",
                    "typescript",
                    "c++",
                    "csharp",
                    "kotlin",
                    "php",
                    "ruby",
                ],
            },
        },
        "required": ["code"],
    },
}

EPISTEME_SUGGEST_REFACTORINGS = {
    "name": "episteme_suggest_refactorings",
    "description": (
        "Get ranked refactoring suggestions for source code, "
        "grounded in the Episteme knowledge graph."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "Source code to suggest refactorings for.",
            },
            "language": {
                "type": "string",
                "description": "Programming language of the source code.",
                "enum": [
                    "python",
                    "java",
                    "go",
                    "rust",
                    "typescript",
                    "c++",
                    "csharp",
                    "kotlin",
                    "php",
                    "ruby",
                ],
            },
        },
        "required": ["code"],
    },
}

EPISTEME_GET_ENTITY = {
    "name": "episteme_get_entity",
    "description": "Retrieve detailed information about a specific entity in the Episteme knowledge graph by its ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "entity_id": {
                "type": "string",
                "description": "Entity ID like DP-005, LAW-003, RF-012, SMELL-001.",
            }
        },
        "required": ["entity_id"],
    },
}

ALL_SCHEMAS = [
    EPISTEME_SEARCH_KNOWLEDGE,
    EPISTEME_ANALYZE_CODE,
    EPISTEME_SUGGEST_REFACTORINGS,
    EPISTEME_GET_ENTITY,
]
