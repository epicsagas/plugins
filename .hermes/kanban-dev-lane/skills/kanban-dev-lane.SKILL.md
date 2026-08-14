---
name: kanban-dev-lane
description: Use when a Hermes Kanban worker wants to run an autonomous implementation delegation lane with a 3-tier fallback chain across claudy -> codex (--yolo) -> agyd (agy --dangerously-skip-permissions) -> Hermes direct on quota exhaustion.
version: 1.0.0
author: epicsagas
license: Apache-2.0
metadata:
  hermes:
    tags: [kanban, dev-lane, claudy, codex, agy, agyd, fallback-lane, autonomous-agents, worktrees]
    related_skills: [kanban-worker, hermes-agent]
---

# Kanban Dev Lane (Multi-Engine Autonomous Implementation Lane)

## Overview

The `kanban-dev-lane` plugin enables Hermes Kanban workers (specifically `dev-lead` and `devops-lead`) to delegate bounded implementation work into an isolated git worktree with an automatic, resilient **3-tier failover chain**:

```
[Hermes Worker (dev-lead)]
          │
          ▼
 ┌──────────────────────────────────────────────────────────┐
 │ Isolated Git Worktree: /tmp/<task_id>-dev-lane           │
 └──────────────────────────────────────────────────────────┘
          │
    ┌─────┴─────────────────────────────────────────┐
    ▼                                               ▼
Tier 1: Claudy (Primary)                     [Success] ──► Hermes Reconcile & Verify
    │ (Quota Exhaustion / 429 / Error)
    ▼
Tier 2: Codex (`codex exec ...` / `--yolo`)   [Success] ──► Hermes Reconcile & Verify
    │ (Quota Exhaustion / Error)
    ▼
Tier 3: AGYD (`agy --dangerously-skip-perms`) [Success] ──► Hermes Reconcile & Verify
    │ (All Engines Exhausted)
    ▼
Tier 4: Hermes Agent Direct Execution ────────────────────► Hermes Complete / Block
```

Hermes is always the task owner: it controls worktree lifecycle, diff inspection, regression testing, and final board completion. External CLIs serve as isolated input engines only.

---

## When to Use

Use `kanban-dev-lane` when:
- The task is a coding, refactoring, documentation, or test implementation task (`DEV-*`, `OPS-*`).
- Acceptance criteria and scope constraints are clearly stated in the Kanban card.
- An isolated git worktree can be created without dirty checkout conflicts.
- Hermes can execute canonical verification commands after the engine finishes.
- At least one engine CLI (`claudy`, `codex`, `agy`) is available on `PATH`.

---

## Capability Check

```bash
command -v claudy && claudy --version
command -v codex && codex --version
command -v agy && agy --version
```

---

## Worktree Isolation Pattern

```bash
TASK_ID="${HERMES_KANBAN_TASK:-t_manual}"
REPO="/path/to/repo"
BASE="$(git -C "$REPO" rev-parse --abbrev-ref HEAD)"
SAFE_TASK="$(printf '%s' "$TASK_ID" | tr -cd '[:alnum:]_-')"
BRANCH="lane/${SAFE_TASK}/$(date -u +%Y%m%d%H%M%S)"
WORKTREE="/tmp/${SAFE_TASK}-dev-lane"

git -C "$REPO" fetch --all --prune
git -C "$REPO" worktree add -b "$BRANCH" "$WORKTREE" "$BASE"
```

---

## Execution Methods

### Method 1: Automated Lane Runner (Recommended)
Automatically detects 429 / quota errors and shifts across engines:

```bash
python3 ~/.hermes/plugins/kanban-dev-lane/scripts/lane_runner.py \
  --prompt-file "/tmp/${SAFE_TASK}-prompt.md" \
  --worktree "$WORKTREE" \
  --task-id "$TASK_ID" \
  --branch "$BRANCH" \
  --engines "claudy,codex,agyd" \
  --timeout 600 \
  --output-json "/tmp/${SAFE_TASK}-report.json"
```

### Method 2: Manual Invocations with Fallback

1. **Tier 1 (Claudy)**:
   ```bash
   claudy -p "$(cat /tmp/${SAFE_TASK}-prompt.md)" --yolo
   ```
2. **Tier 2 (Codex)**:
   ```bash
   codex exec "$(cat /tmp/${SAFE_TASK}-prompt.md)" < /dev/null \
     --dangerously-bypass-approvals-and-sandbox \
     --ephemeral
   ```
3. **Tier 3 (AGYD / Antigravity)**:
   ```bash
   agy --dangerously-skip-permissions -p "$(cat /tmp/${SAFE_TASK}-prompt.md)"
   ```
4. **Tier 4 (Hermes Direct)**:
   Native Hermes worker tools (`file_write`, `file_edit`, `terminal`).

---

## Reconciliation & Final Handoff

```bash
git -C "$WORKTREE" status --short
git -C "$WORKTREE" diff --stat
cd "$WORKTREE" && npm test # Canonical verification
git -C "$REPO" merge "$BRANCH" --ff-only
git -C "$REPO" worktree remove "$WORKTREE"
git -C "$REPO" branch -d "$BRANCH"
```

Record telemetry in `kanban_complete`:

```json
{
  "dev_lane": {
    "used": true,
    "primary_engine": "claudy",
    "successful_engine": "codex",
    "fallback_occurred": true,
    "fallback_chain": ["claudy (429 quota exhausted)", "codex (success)"],
    "worktree": "/tmp/t_dev123-dev-lane",
    "result": "accepted",
    "accepted_commits": ["a1b2c3d"],
    "tests_run": [
      {"command": "npm test", "exit_code": 0, "owner": "hermes"}
    ]
  }
}
```
