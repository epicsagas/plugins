"""JSON Schema tool definitions for the obsidian-forge Hermes plugin."""

obsidian_vault_health = {
    "name": "obsidian_vault_health",
    "description": (
        "Diagnose Obsidian vault health and status using 'of doctor'. "
        "Reports vault configuration, AI connectivity, inbox state, and git health. "
        "Use this when the user wants to check vault status or diagnose vault issues."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "vault_path": {
                "type": "string",
                "description": (
                    "Absolute path to the Obsidian vault directory. "
                    "When omitted, uses the default vault from global config."
                ),
            },
        },
        "required": [],
    },
}

obsidian_process_inbox = {
    "name": "obsidian_process_inbox",
    "description": (
        "Process all inbox notes with AI classification and PARA routing using "
        "'of process-all'. Classifies notes by topic, injects frontmatter, and "
        "moves them to the appropriate PARA folder. "
        "Use this when the user wants to empty the inbox or classify new notes."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "vault": {
                "type": "string",
                "description": (
                    "Vault name as registered in the global obsidian-forge config. "
                    "When omitted, uses the default vault."
                ),
            },
        },
        "required": [],
    },
}

obsidian_graph_strengthen = {
    "name": "obsidian_graph_strengthen",
    "description": (
        "Strengthen the knowledge graph by adding backlinks, bridge notes, and "
        "auto-tags using 'of strengthen-graph'. Improves connectivity between "
        "related notes and surfaces hidden relationships. "
        "Use this when the user wants to improve graph density or find connections."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "vault_path": {
                "type": "string",
                "description": (
                    "Absolute path to the Obsidian vault directory. "
                    "When omitted, uses the default vault from global config."
                ),
            },
        },
        "required": [],
    },
}

obsidian_sync = {
    "name": "obsidian_sync",
    "description": (
        "Run a full sync cycle using 'of sync': rebuilds MOCs, strengthens the "
        "knowledge graph, then commits changes to git. This is the complete "
        "end-to-end vault maintenance operation. "
        "Use this when the user wants a full vault refresh or periodic maintenance."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "vault_path": {
                "type": "string",
                "description": (
                    "Absolute path to the Obsidian vault directory. "
                    "When omitted, uses the default vault from global config."
                ),
            },
        },
        "required": [],
    },
}

obsidian_update_mocs = {
    "name": "obsidian_update_mocs",
    "description": (
        "Rebuild all project hub files (Maps of Content) using 'of update-mocs'. "
        "Regenerates MOC pages that serve as navigational entry points for each "
        "project area in the vault. "
        "Use this when the user wants to refresh the vault's table of contents."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "vault_path": {
                "type": "string",
                "description": (
                    "Absolute path to the Obsidian vault directory. "
                    "When omitted, uses the default vault from global config."
                ),
            },
        },
        "required": [],
    },
}

ALL_SCHEMAS = [
    obsidian_vault_health,
    obsidian_process_inbox,
    obsidian_graph_strengthen,
    obsidian_sync,
    obsidian_update_mocs,
]
