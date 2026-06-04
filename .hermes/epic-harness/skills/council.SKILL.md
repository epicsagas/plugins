---
name: council
description: >-
  4-voice parallel deliberation for architecture, tech selection, or design
  decisions with no clear answer. Each voice gets independent context to
  prevent anchoring bias.
  Use when the user says "council", "deliberate", "second opinion", or faces
  a trade-off between multiple valid approaches.
---

4-voice deliberation: Architect · Skeptic · Pragmatist · Critic. Each evaluates independently, then a synthesis is produced.

## Usage
```
/council <decision or question>
```

## The four voices

### 🏗️ Architect
- Focuses on long-term system design, extensibility, and maintainability
- Asks: "How does this scale? What are the boundaries? What patterns apply?"
- Argues for the cleanest design

### 🔍 Skeptic
- Looks for flaws, hidden risks, and failure modes
- Asks: "What could go wrong? What assumptions are untested? What are the edge cases?"
- Argues for the safest approach

### ⚡ Pragmatist
- Prioritizes speed, simplicity, and immediate value
- Asks: "What's the fastest path? What can we defer? What's good enough?"
- Argues for the simplest approach

### 📊 Critic
- Evaluates trade-offs with data, benchmarks, and precedents
- Asks: "What does the evidence say? What have others done? What are the measurable differences?"
- Argues for the most evidence-based approach

## Process

1. **State the question** — clarify the decision and constraints
2. **Recall context** — `harness_mem_recall` to surface past decisions on related topics
3. **Each voice responds independently** — no voice sees another's response
4. **Synthesize** — identify consensus, list disagreements, recommend a path
5. **Record** — `harness_mem_add` the decision with reasoning as type "decision"
6. **Link** — `harness_mem_link` to any related prior decisions

## Output format

```
## Decision: <question>

### Architect
<2-3 paragraph argument>

### Skeptic
<2-3 paragraph argument>

### Pragmatist
<2-3 paragraph argument>

### Critic
<2-3 paragraph argument>

### Synthesis
- **Consensus:** <what all 4 agree on>
- **Disagreement:** <where voices diverge>
- **Recommendation:** <final recommendation with reasoning>
- **Risk:** <highest-risk aspect regardless of choice>
```

## When to use council vs. just decide

| Situation | Use council? |
|---|---|
| Two+ valid approaches with real trade-offs | ✅ Yes |
| Simple choice with obvious best answer | ❌ Just decide |
| User explicitly asks for deliberation | ✅ Yes |
| Reversible decision with low stakes | ❌ Just decide |
| Architecture change affecting multiple components | ✅ Yes |
