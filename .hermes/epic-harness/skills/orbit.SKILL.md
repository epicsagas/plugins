---
name: orbit
description: >-
  Autonomous pipeline — spec requirements, execute implementation, audit quality,
  and ship. Runs the full epic-harness orbit cycle in one go.
  Use when the user says "orbit", "full pipeline", "spec to ship", or describes
  a feature that needs end-to-end handling.
---

Autonomous software delivery pipeline: spec → go → audit → ship. One command takes a feature from idea to PR.

## Usage
```
/orbit <feature description>
```

## Pipeline phases

### Phase 1 — Spec
Write a numbered requirements + acceptance criteria document.

1. Use `harness_mem_recall` to surface relevant past decisions and patterns
2. Analyze the codebase to understand current architecture
3. Produce a SPEC.md with numbered requirements (REQ-1, REQ-2, …) and acceptance criteria (AC-1.1, …)
4. Present spec to user for approval before proceeding

### Phase 2 — Go
Implement the approved spec via TDD.

1. For each requirement, write a failing test first
2. Implement minimum code to pass the test
3. Run tests after each change — no progress without green tests
4. Use `harness_mem_add` to record key decisions made during implementation

### Phase 3 — Audit
Parallel review across 3 dimensions.

1. **Code quality** — unused imports, dead code, naming, complexity
2. **Security** — input validation, auth checks, secret exposure
3. **Test coverage** — missing edge cases, uncovered error paths
4. Output PASS / WARN / FAIL per dimension
5. Fix all FAIL items, address WARN items if trivial

### Phase 4 — Ship
Create PR and verify CI passes.

1. Create a feature branch if not already on one
2. Commit all changes with conventional commit messages
3. Push branch and create PR with spec summary
4. Monitor CI — if it fails, fix and re-push
5. Report final status

## Decision: which phases to run

| User request | Phases |
|---|---|
| "orbit" or "full pipeline" | All 4 phases |
| "just spec it" | Phase 1 only |
| "implement this spec" | Phase 2–4 |
| "audit and ship" | Phase 3–4 |

## Error handling

| Situation | Action |
|---|---|
| Spec rejected by user | Revise spec, do not proceed to Go |
| Tests failing after 3 attempts | Stop, report to user, ask for guidance |
| Audit finds security FAIL | Must fix before shipping |
| CI fails | Auto-fix once, then report to user |

## Memory integration

- `harness_mem_recall` at pipeline start — surface context
- `harness_mem_add` for each significant decision — preserve knowledge
- `harness_mem_link` to connect decisions to requirements
