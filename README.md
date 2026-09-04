# epicsagas plugins

> Handcrafted plugins for serious AI-assisted development — autonomous agents, context compression, and tools that get out of your way.

<p align="center">
  <a href="https://github.com/epicsagas/plugins/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=ffd700&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=2ecc71&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/issues"><img alt="Issues" src="https://img.shields.io/github/issues/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=ff6b6b&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=58a6ff&logo=git&logoColor=white" /></a>
</p>
<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-3fb950?style=for-the-badge&labelColor=0d1117" /></a>
  <a href="https://buymeacoffee.com/epicsaga"><img alt="Buy Me a Coffee" src="https://img.shields.io/badge/buy_me_a_coffee-FFDD00?style=for-the-badge&labelColor=0d1117&logo=buymeacoffee&logoColor=black" /></a>
</p>

**Translations:** [한국어](docs/README.ko.md) · [日本語](docs/README.ja.md) · [简体中文](docs/README.zh-cn.md) · [繁體中文](docs/README.zh-tw.md) · [Español](docs/README.es.md) · [Français](docs/README.fr.md) · [Deutsch](docs/README.de.md) · [Português](docs/README.pt.md) · [Русский](docs/README.ru.md) · [العربية](docs/README.ar.md)

---

## Plugins

The hub carries the core epiccounty lineup. Everything else lives in its own repository with a same-named standalone marketplace (see [Individualized plugins](#individualized-plugins)).

| Plugin | Description | Source |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Autonomous agent harness — 8 commands, self-evolving skills, and invisible hooks that guard, polish, and reflect on every session. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Token-optimized document reader — silently compresses `.md`, `.html`, and `.txt` files on Read, cutting context usage by up to 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP documentation server — hybrid BM25+vector search, lint, and launchd lifecycle management for project docs. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Books to the human-quality bar — 6-phase publishing pipeline, 12 agents, readiness gate, visual system. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | Software engineering knowledge graph — design patterns, code smells, refactorings, and architecture analysis with AI-powered code review. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian vault lifecycle management — AI inbox classification, graph strengthening, MOC regeneration, and multi-vault sync as agent skills. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Personal agent skill collection — problem discovery (5 Whys, JTBD, Fishbone), introspect (bias detection, thinking pattern analysis), and OSS distribution readiness. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## Installation

### Claude Code (recommended)

Register this marketplace once, then install any plugin:

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic@epicsagas
claude plugin install llm-transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install episteme@epicsagas
claude plugin install obsidian-forge@epicsagas
claude plugin install epicsagas@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

All plugins are available immediately — no further steps needed.

### Grok Build (xAI)

```bash
grok plugin marketplace add epicsagas/plugins
grok plugin install epic --trust
grok plugin install llm-transpile --trust
grok plugin install alcove --trust
grok plugin install velith --trust
grok plugin install episteme --trust
grok plugin install obsidian-forge --trust
grok plugin install epicsagas --trust
```

Browse the catalog with `/marketplace` in the Grok TUI. Note: single-plugin repositories (the Individualized plugins below) do not list as Grok marketplaces — install those directly with `grok plugin install epicsagas/<repo> --trust`.

### Hermes Agent

One command installs the epiccounty suite — 6 plugins, 32 tools:

```bash
hermes plugins install epicsagas/plugins --enable
```

Or install and enable individual plugins:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` is Hermes-only — bundled in `.hermes/` in this repo, not published to the Claude/Codex marketplaces.

**Prerequisites:** Each plugin wraps a Rust CLI binary. Install the ones you need:

```bash
brew install epicsagas/tap/alcove          # alcove plugin
brew install epicsagas/tap/episteme        # episteme plugin (also needs `epis serve` running)
brew install epicsagas/tap/epic-harness    # epic-harness plugin
brew install epicsagas/tap/llm-transpile   # llm-transpile plugin
brew install epicsagas/tap/obsidian-forge  # obsidian-forge plugin
```

**Quick start — install everything at once:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## Standalone Install

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # pre-built binary
cargo install epic-harness    # build from source
```

### transpile

```bash
brew install epicsagas/tap/llm-transpile
cargo binstall llm-transpile
cargo install llm-transpile
```

### alcove

```bash
brew install epicsagas/tap/alcove
cargo binstall alcove
cargo install alcove
```

### episteme

```bash
brew install epicsagas/tap/episteme
cargo binstall episteme
cargo install episteme
```

### obsidian-forge

```bash
brew install epicsagas/tap/obsidian-forge
cargo binstall obsidian-forge
cargo install obsidian-forge
```

---

## Individualized plugins

These plugins moved out of the hub. Each repository ships its own marketplace named after the plugin itself, so it installs standalone:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

Grok Build installs these directly from the repository instead (they do not register as Grok marketplaces):

```bash
grok plugin install epicsagas/<repo> --trust
```

| Plugin | Repository | What it does |
|--------|------------|--------------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | Headless browser as MCP tools — fetch, scrape, extract markdown, JS evals. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | Interview → compile → evolve a personalized AI agent harness. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | Multi-host plugin manager — scaffold, doctor, install-validate, publish. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | GeekMagic SmallTV as a live agent status display. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | Login-walled content harvester — hidden-API recon, human-paced collection. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Upbit coin investment analyst — bull/bear debate pipeline with risk gates. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | KRX stock investment analyst — same bull/bear debate architecture with investor-flow/short-selling evidence and KRX rules, via the Toss Securities Open API. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | AI/tech event intelligence — deterministic 9-source aggregator. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | Offline TOEFL iBT grading across all 4 sections with a local LLM. |
| wishket-radar | [epicsagas/wishket-radar](https://github.com/epicsagas/wishket-radar) | Wishket project radar — search, deep-analyze, and tech-match outsourcing projects. |

---

## Plugin Details

### epic-harness

**Autonomous Agent Harness**

Build agent workflows that handle complex, multi-step tasks independently. Powered by 8 built-in power commands and an autonomous `/orbit` pipeline. Skills evolve the more you use them. Session hooks run automatically to guard your code, polish output, and reflect on each session.

**When to use:**
- Automating repetitive code review, commit, and test cycles
- Defining custom per-project workflows
- Enforcing consistent behavior patterns across Claude sessions

**Key features:**
- 8 built-in power commands including `/orbit` (full autonomous pipeline)
- Self-evolving skill system — learns from usage patterns and improves over time
- Session guard hooks — prevents mistakes and maintains quality automatically

→ [Source & Docs](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Token-Optimized Document Reader**

Automatically compresses `.md`, `.html`, and `.txt` files on every Read tool call, cutting context token usage by up to 40%. Takes effect immediately with no workflow changes required.

**When to use:**
- Projects that frequently reference large documents or specs
- When you regularly hit context window limits
- Reducing token costs across long sessions

**Key features:**
- Silent compression — same output, up to 40% fewer tokens
- Auto-detects `.md` / `.html` / `.txt` formats
- Fully compatible with existing Read tool workflows

→ [Source & Docs](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP Documentation Server**

Gives AI coding agents on-demand access to your private project docs via MCP. Hybrid BM25+vector search, semantic lint, document validation, and background HTTP server with proxy mode for instant response.

**When to use:**
- Managing private project documentation across multiple AI agents
- Searching architecture decisions, PRDs, and runbooks from any MCP-compatible agent
- Enforcing documentation standards with policy validation and semantic lint

**Key features:**
- Hybrid search — BM25 + vector similarity with Reciprocal Rank Fusion
- One doc-repo, any agent — Claude Code, Cursor, Gemini CLI, Codex, and 5+ more
- Background server with proxy mode — eliminates cold-start latency on new sessions
- Semantic lint — broken links, orphan files, stale markers, outdated date claims
- macOS launchd integration — enable/disable/start/stop/restart lifecycle commands

→ [Source & Docs](https://github.com/epicsagas/alcove)

---

### velith

**Books to the Human-Quality Bar**

A cold reader who buys books in the genre cannot tell the manuscript was machine-drafted. Six phases, twelve agents, one standard. Agents read the entire manuscript, the voice is locked on a sample chapter before drafting volume, every chapter is critiqued and revised before it is saved, every claim is fact-checked, and publishing is blocked until simulated target readers would keep reading.

**When to use:**
- Writing a novel, nonfiction book, technical guide, screenplay, poetry collection, game scenario, or thesis
- Long manuscripts where voice drift, contradictions, and invented facts break the book
- Illustrations, diagrams, and covers that must look like one book, on any image model
- Publishing to EPUB, PDF, MOBI, TXT, or Markdown

**Key features:**
- 6-phase pipeline with author checkpoints: concept, outline, voice lock, look lock, restructures, readiness
- Full-manuscript context: agents read the whole book, never summaries
- Draft → critique with quoted lines → revise, inside the writer, before saving
- 7-stage editing: fact check → assessment → developmental → line → copy → proofread → beta-reader readiness verdict
- Visual system: art bible, look lock, code-rendered diagrams, prompts compiled for Midjourney/gpt-image/SD/Imagen/Ideogram, vision QA
- 7 genre craft references (fiction, non-fiction, technical, screenplay, poetry, game, academic) + custom genres
- EPUB, PDF, MOBI, TXT, Markdown via Pandoc + epubcheck, KDP and Korean platform checklists

→ [Source & Docs](https://github.com/epicsagas/Velith)

---

### episteme

**Software Engineering Knowledge Graph**

A queryable knowledge graph of design patterns, code smells, refactorings, and architecture laws. AI-powered code analysis detects quality issues, suggests improvements, and grounds every recommendation in established engineering principles.

**When to use:**
- Reviewing code for design pattern misuse, code smells, or architecture violations
- Choosing between refactoring strategies with principled trade-off analysis
- Learning and applying software engineering laws (Conway's, Amdahl's, Gall's)

**Key features:**
- Knowledge graph with graph traversal across patterns, smells, refactorings, and laws
- AI-powered code analysis with smell detection and ranked refactoring suggestions
- Multiple agent personas — code reviewer, architecture analyst, engineering advisor

→ [Source & Docs](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Obsidian Vault Lifecycle Management**

Gives AI agents skill-driven access to Obsidian vault operations — AI-powered inbox classification with PARA routing, knowledge graph strengthening (backlinks, bridge notes, auto-tags), MOC regeneration, tag/link/frontmatter repair, and full sync cycles. Single Rust binary, multi-vault, zero config to start.

**When to use:**
- Managing an Obsidian vault (Second Brain, Zettelkasten, PARA) from AI agent sessions
- Processing inbox notes with AI classification and automatic routing
- Strengthening knowledge graph connections between projects and concepts

**Key features:**
- 5 agent skills — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- AI-powered inbox classification with frontmatter injection and PARA routing
- Knowledge graph strengthening with before/after metrics reporting
- Multi-vault support with shared settings and background daemon (macOS)

→ [Source & Docs](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**Personal Agent Skills**

A curated set of agent skills for personal and team use — problem discovery, cognitive self-analysis, and OSS release readiness. No binary required; skills load directly from markdown files.

**When to use:**
- Discovering and defining real problems before building (individuals, teams, startups)
- Analyzing your own thinking patterns and cognitive biases from conversation history
- Auditing an OSS project's release readiness across community, README, distribution, and security

**Key features:**
- `discover` — 5 Whys, JTBD, Fishbone, Socratic questioning, Assumption mapping
- `cognitive-audit` — evidence-based bias detection, decision-making analysis, 10 actionable routines
- `oss-dist` — full release lifecycle: community standards, README, launch strategy, i18n, security

→ [Source & Docs](https://github.com/epicsagas/epicsagas)

---


## Contributing

To submit a plugin or suggest improvements:

1. Fork this repository
2. Add your plugin entry to `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`
3. Open a Pull Request

Plugins are maintained as independent GitHub repositories. This marketplace contains metadata only.

---

## License

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
