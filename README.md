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

| Plugin | Description | Source |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Autonomous agent harness — 8 commands, self-evolving skills, and invisible hooks that guard, polish, and reflect on every session. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Token-optimized document reader — silently compresses `.md`, `.html`, and `.txt` files on Read, cutting context usage by up to 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP documentation server — hybrid BM25+vector search, lint, and launchd lifecycle management for project docs. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI-native publishing system — autonomous multi-phase workflows from ideation to EPUB/PDF. Build books like software. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Headless browser as MCP tools — fetch, scrape, extract markdown, and run JS evals. Zero config, auto-installs binaries on first load. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Software engineering knowledge graph — design patterns, code smells, refactorings, and architecture analysis with AI-powered code review. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian vault lifecycle management — AI inbox classification, graph strengthening, MOC regeneration, and multi-vault sync as agent skills. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Personal agent skill collection — problem discovery (5 Whys, JTBD, Fishbone), introspect (bias detection, thinking pattern analysis), and OSS distribution readiness. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | Personal academic research assistant — ingest arXiv/Semantic-Scholar/PDF papers, run LLM gap analysis and reports, all driven by an LLM agent via MCP tools (`research serve`). | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — collect a user's tacit knowledge and goals via interview, then compile, deploy, and evolve a personalized AI agent harness. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | Autonomous multi-engine implementation lane — delegates coding work into isolated git worktrees with automatic failover (Claudy ➔ Codex ➔ AGYD). | [epicsagas/kanban-dev-lane](https://github.com/epicsagas/kanban-dev-lane) |

---

## Installation

### Claude Code (recommended)

Register this marketplace once, then install any plugin:

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic-harness@epicsagas
claude plugin install llm-transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install obscura-plugin@epicsagas
claude plugin install episteme@epicsagas
claude plugin install obsidian-forge@epicsagas
claude plugin install epicsagas@epicsagas
claude plugin install research@epicsagas
claude plugin install byoh@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

All plugins are available immediately — no further steps needed.

### Hermes Agent

One command installs the full epiccounty suite — 6 plugins, 24 tools:

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
hermes plugins enable obscura
```

**Prerequisites:** Each plugin wraps a Rust CLI binary. Install the ones you need:

```bash
brew install epicsagas/tap/alcove          # alcove plugin
brew install epicsagas/tap/episteme        # episteme plugin (also needs `epis serve` running)
brew install epicsagas/tap/epic-harness    # epic-harness plugin
brew install epicsagas/tap/llm-transpile   # llm-transpile plugin
brew install epicsagas/tap/obsidian-forge  # obsidian-forge plugin
brew install epicsagas/tap/obscura         # obscura plugin
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

### obscura

```bash
brew install epicsagas/tap/obscura-plugin
cargo binstall obscura-plugin
cargo install obscura-plugin
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

### research

```bash
brew install epicsagas/tap/research-agent
cargo binstall research-agent
cargo install research-agent
```

### byoh

```bash
brew install epicsagas/tap/byoh
cargo binstall byoh
cargo install byoh
```

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

**AI-Native Publishing System**

Build books like software. Autonomous multi-phase workflows from blank page to publishable EPUB/PDF. Seven specialized agents handle structure, drafting, continuity, style, cover design, and marketing.

**When to use:**
- Writing structured long-form content (fiction, non-fiction, technical, academic)
- Maintaining cross-chapter consistency and voice across a full book
- Publishing to EPUB, PDF, MOBI, or Markdown

**Key features:**
- 6-phase pipeline: Onboarding → Ideation → Outlining → Drafting → Editing → Publishing
- 7 genre templates (fiction, non-fiction, technical, screenplay, poetry, game, academic)
- 5-stage editing pipeline with AI-slop detection
- EPUB, PDF, MOBI, TXT, Markdown output via Pandoc + Calibre

→ [Source & Docs](https://github.com/epicsagas/Velith)

---

### obscura-plugin

**Headless Browser as MCP Tools**

Gives AI agents direct access to the web via five MCP tools: fetch, scrape, serve, screenshot, and extract markdown. Auto-installs `obscura` and `obscura-worker` binaries on first load — no manual setup.

**When to use:**
- Agents that need to read web pages, scrape data, or run JS evals
- Batch URL processing with parallel scraping
- Providing a CDP WebSocket endpoint for Playwright/Puppeteer

**Key features:**
- Zero config — plugin auto-installs all required binaries
- `obscura_scrape` with configurable concurrency via `obscura-worker`
- `obscura_serve` exposes a CDP WebSocket server for Playwright/Puppeteer
- Stealth mode for anti-detection + tracker blocking

→ [Source & Docs](https://github.com/epicsagas/obscura-plugin)

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

### research

**Personal Academic Research Assistant**

A long-term research memory that indexes papers from arXiv, Semantic Scholar, and local PDFs, identifies knowledge gaps, and generates literature reports. Driven by an LLM agent via MCP tools (`research serve`) — the agent ingests, searches, analyzes gaps, and writes reports while you stay in the conversation.

**When to use:**
- Building a reading list or literature review on a topic
- Tracking what you've read, what's missing, and what to read next
- Letting an agent ingest and synthesize papers while you direct the research

**Key features:**
- 11 MCP tools: init · ingest · query_papers · analyze_gaps · list_gaps · generate_report · topics_list · topic_add · state · update_read · index_rebuild
- Adaptive dispatch — MCP is the primary interface for agent hosts, CLI is the fallback for terminals/CI
- Local SQLite index (FTS5) + real LLM via `~/.research/config.toml` `[llm]`

→ [Source & Docs](https://github.com/epicsagas/research-agent)

---

### byoh

**BuildYourOwnHarness**

Generate a personalized AI agent harness from an interview. BYOH interactively collects your tacit knowledge, data sources, genre, and goals, then compiles, deploys, and evolves a unique harness — not a fixed template. The whole pipeline is gated by three safety gates (Critic / Seesaw / Stagnation) that can never be bypassed.

**When to use:**
- Bootstrapping a custom agent harness tuned to your domain and workflow
- Evolving skills safely with measurable A/B evidence and rollback
- Driving the whole profile → compile → evolve flow from an LLM agent via MCP tools

**Key features:**
- 14 MCP tools: profile_create/scan/interview/confirm/read · compile · compile_dry_run · evolve_cycle · genre_list · registry_clone_skill · render_plugin · install_plugin · catalog_search · catalog_vendor
- Agent-driven mode (`byoh serve`) — control inversion, CLI is secondary
- No embedded knowledge base — point the generated harness at a doc server like [alcove](https://github.com/epicsagas/alcove) for retrieval

→ [Source & Docs](https://github.com/epicsagas/BuildYourOwnHarness)

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
