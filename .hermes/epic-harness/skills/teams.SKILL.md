---
name: teams
description: >-
  Manage org-level agent teams — list available teams, sync agent definitions
  to a project, or design a new team composition.
  Use when the user says "team", "agents", "set up a team", or wants to
  coordinate multiple specialized agents.
---

Manage agent teams for multi-agent coordination. List, sync, and compose teams of specialized agents.

## Usage
```
/teams list              — show all teams
/teams show <name>       — show team details
/teams sync <name>       — sync team agents to current project
/teams design            — interactive team composition
```

## Quick reference

### List teams
```bash
# Via tool
harness_team_list

# Or CLI
epic team list
```

### Show team details
```bash
# Via tool
harness_team_show(team="core")

# Or CLI
epic team show core
```

### Sync team to project
```bash
# Via tool — sync to .claude/agents/ in current project
harness_team_sync(team="core")

# Via tool — sync globally to ~/.claude/agents/
harness_team_sync(team="core", global=true)
```

## Team composition guidelines

A well-designed team covers these roles:

| Role | Purpose | Example agents |
|---|---|---|
| **Leader** | Coordinates, assigns tasks, reviews | architect, project-lead |
| **Researcher** | Explores code, finds information | explorer, researcher |
| **Builder** | Writes implementation code | coder, implementer |
| **Reviewer** | Quality gate, testing | reviewer, tester |

## Workflow: setting up a team

1. `harness_team_list` — see what's available
2. `harness_team_show(team="<name>")` — inspect the team
3. `harness_team_sync(team="<name>")` — sync agents to project
4. Agents appear in `.claude/agents/` and are ready to use

## Designing a new team

For custom teams, run `epic team` (no subcommand) for interactive design.
The CLI walks through role selection, skill assignment, and agent configuration.
