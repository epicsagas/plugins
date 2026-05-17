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
| [epic](#epic) | Autonomous agent harness — 6 power commands, self-evolving skills, and invisible hooks that guard, polish, and reflect on every session. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [transpile](#transpile) | Token-optimized document reader — silently compresses `.md`, `.html`, and `.txt` files on Read, cutting context usage by up to 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP documentation server — hybrid BM25+vector search, lint, and launchd lifecycle management for project docs. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |

---

## Installation

### Via Claude Code (recommended)

Add this marketplace, then install plugins:

```bash
claude marketplace add epicsagas/plugins
claude plugin install epic
claude plugin install transpile
claude plugin install alcove
```

### epic — standalone install

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall** (pre-built binary):
```bash
cargo binstall epic-harness
```

**Cargo** (build from source):
```bash
cargo install epic-harness
```

### transpile — standalone install

**cargo-binstall** (pre-built binary):
```bash
cargo binstall llm-transpile
```

**Cargo** (build from source):
```bash
cargo install llm-transpile
```

### alcove — standalone install

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall** (pre-built binary):
```bash
cargo binstall alcove
```

**Cargo** (build from source):
```bash
cargo install alcove
```

---

## Plugin Details

### epic

**Autonomous Agent Harness**

Build agent workflows that handle complex, multi-step tasks independently. Powered by 6 built-in power commands, skills evolve the more you use them. Session hooks run automatically to guard your code, polish output, and reflect on each session.

**When to use:**
- Automating repetitive code review, commit, and test cycles
- Defining custom per-project workflows
- Enforcing consistent behavior patterns across Claude sessions

**Key features:**
- 6 built-in power commands (commit, review, test, deploy, and more)
- Self-evolving skill system — learns from usage patterns and improves over time
- Session guard hooks — prevents mistakes and maintains quality automatically

→ [Source & Docs](https://github.com/epicsagas/epic-harness)

---

### transpile

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

## Contributing

To submit a plugin or suggest improvements:

1. Fork this repository
2. Add your plugin entry to `.claude-plugin/marketplace.json`
3. Open a Pull Request

Plugins are maintained as independent GitHub repositories. This marketplace contains metadata only.

---

## License

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
