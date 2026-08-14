# kanban-dev-lane (Autonomous Multi-Engine Fallback Lane)

A **Hermes Agent** plugin that lets a Kanban worker delegate bounded implementation work to autonomous coding engines (**Claudy**, **Codex**, **AGYD / Antigravity**) in an isolated git worktree with automatic failover, while Hermes keeps full ownership of the task lifecycle, reconciliation, testing, and handoff.

---

## 🚀 Key Features

1. **Multi-Engine Quota Fallback**:
   - **Primary**: `claudy -p "<prompt>" --yolo`
   - **Fallback 1 (on quota/rate-limit)**: `codex exec "<prompt>" < /dev/null --dangerously-bypass-approvals-and-sandbox --ephemeral` (or `codex --yolo`)
   - **Fallback 2 (on quota/error)**: `agy --dangerously-skip-permissions -p "<prompt>"` (alias `agyd`)
   - **Final Safety**: Hermes Agent native direct execution.
2. **Strict Hermes Ownership**: Hermes creates the isolated worktree, runs the lane, verifies the diff against repository safety constraints, reruns canonical test suites, and performs final merge/rejection.
3. **Automated Lane Runner**: Includes `scripts/lane_runner.py` for automated error parsing, quota exhaustion detection (429, tokens, limits), process timeouts, and structured JSON reporting.
4. **Zero State Mutation Risk**: External engines run strictly in the worktree cwd and cannot write to durable Kanban state or invoke messaging gateways.

---

## 🛠️ Usage

### Quick Capability Check
```bash
command -v claudy && claudy --version
command -v codex && codex --version
command -v agy && agy --version
```

### Automated Runner Execution
```bash
python3 ~/.hermes/plugins/kanban-dev-lane/scripts/lane_runner.py \
  --prompt-file /tmp/prompt.md \
  --worktree /tmp/t_task123-lane \
  --task-id t_task123 \
  --engines claudy,codex,agyd \
  --timeout 600 \
  --output-json /tmp/t_task123-report.json
```

---

## 📋 Telemetry & Metadata

Completed tasks record execution telemetry in `metadata.dev_lane`:

```json
{
  "dev_lane": {
    "used": true,
    "primary_engine": "claudy",
    "successful_engine": "codex",
    "fallback_occurred": true,
    "fallback_chain": ["claudy (429 rate limit)", "codex (success)"],
    "worktree": "/tmp/t_dev123-lane",
    "result": "accepted",
    "accepted_commits": ["b8c4d12"],
    "tests_run": [
      {"command": "pytest tests/", "exit_code": 0, "owner": "hermes"}
    ]
  }
}
```

---

## 📄 License
Apache-2.0
