---
name: reflect
description: >-
  Self-assessment of AI session quality. Scores 5 dimensions from session data
  and harness memory. Not an agent performance review — it's human self-reflection
  on how well they used AI assistance.
  Use when the user says "reflect", "how did I do", "session review", or at the
  end of a long session.
---

Self-assessment of AI session quality across 5 dimensions. Uses harness session data and memory to produce an honest scorecard.

## Usage
```
/reflect
```

## The 5 dimensions

| Dimension | Weight | Measures |
|---|---|---|
| **Goal clarity** | 20% | Were requirements specific enough? Did the user provide clear acceptance criteria? |
| **Prompt quality** | 20% | Were instructions precise? Did the user catch misunderstandings early? |
| **Iteration efficiency** | 20% | How many correction cycles? Were they due to unclear specs or exploration? |
| **Tool utilization** | 20% | Did the user leverage available tools (memory, search, code analysis)? |
| **Outcome alignment** | 20% | Does the final result match what was actually needed? |

## Process

1. **Collect data** — `harness_reflect_context` to get session stats and evolution history
2. **Recall context** — `harness_mem_recall` with hint about the current session
3. **Score each dimension** — 1-5 scale with specific evidence
4. **Calculate overall** — weighted average
5. **Identify top improvement** — single most impactful thing to do differently
6. **Record** — `harness_mem_add` the reflection as type "insight"

## Output format

```
## Session Reflection

### Scores
| Dimension | Score | Evidence |
|---|---|---|
| Goal clarity | 4/5 | ... |
| Prompt quality | 3/5 | ... |
| Iteration efficiency | 4/5 | ... |
| Tool utilization | 2/5 | ... |
| Outcome alignment | 5/5 | ... |
| **Overall** | **3.6/5** | |

### What went well
- ...

### What to improve
- ...

### Top recommendation for next session
> Single most impactful change to make.
```

## Important notes

- This is NOT about agent performance — it's about how the human used AI
- Be honest, not flattering — low scores are more useful than high scores
- The "top recommendation" should be actionable and specific
