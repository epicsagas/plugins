# epicsagas Plugins

> Handgefertigte Plugins für professionelle KI-gestützte Entwicklung — autonome Agenten, Kontextkomprimierung und Werkzeuge, die nicht im Weg stehen.

<p align="center">
  <a href="https://github.com/epicsagas/plugins/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=ffd700&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=2ecc71&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/issues"><img alt="Issues" src="https://img.shields.io/github/issues/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=ff6b6b&logo=github&logoColor=white" /></a>
  <a href="https://github.com/epicsagas/plugins/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/epicsagas/plugins?style=for-the-badge&labelColor=0d1117&color=58a6ff&logo=git&logoColor=white" /></a>
</p>
<p align="center">
  <a href="../LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-3fb950?style=for-the-badge&labelColor=0d1117" /></a>
  <a href="https://buymeacoffee.com/epicsaga"><img alt="Buy Me a Coffee" src="https://img.shields.io/badge/buy_me_a_coffee-FFDD00?style=for-the-badge&labelColor=0d1117&logo=buymeacoffee&logoColor=black" /></a>
</p>

**Translations:** [English](../README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [简体中文](README.zh-cn.md) · [繁體中文](README.zh-tw.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## Plugin-Übersicht

| Plugin | Beschreibung | Quelle |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Autonomes Agenten-Harness — 8 Befehle, selbstentwickelnde Fähigkeiten und unsichtbare Session-Hooks. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Token-optimierter Dokumentenleser — komprimiert `.md`, `.html`, `.txt` automatisch und spart bis zu 40% Kontext. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP-Dokumentationsserver — hybride BM25+Vektorsuche, semantischer Linter und launchd-Lebenszyklusverwaltung. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | KI-natives Publikationssystem — autonomer mehrphasiger Workflow von der Idee bis zum fertigen EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Headless-Browser als MCP-Tools — Fetch, Scrape, Markdown-Extraktion und JS-Ausführung ohne Konfiguration. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Software-Engineering-Wissensgraph — Entwurfsmuster, Code Smells, Refactorings und KI-Code-Review. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian-Vault-Management — KI-Posteingangsklassifizierung, Wissensgraph-Verstärkung und Multi-Vault-Synchronisation. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Persönliche Agentenfähigkeiten — Problemerkennung (5 Whys, JTBD), kognitive Selbstanalyse und OSS-Release-Audits. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | Akademischer Forschungsassistent — Indizierung von Artikeln (arXiv/Semantic Scholar/PDF), Lückenanalyse und Berichte. | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — extrahiert implizites Wissen durch Interviews zur Erstellung maßgeschneiderter Harnesses. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | Autonome Multi-Engine-Entwicklungsspur — Delegation in isolierte Git-Worktrees mit Failover (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## Installation

### Claude Code (empfohlen)

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

### Hermes Agent

```bash
hermes plugins install epicsagas/plugins --enable
hermes plugins enable kanban-dev-lane
```

---

## Plugin-Details

### kanban-dev-lane

**Autonome Multi-Engine-Implementierungsspur für Hermes Kanban**

Delegiert Entwicklungs- und Refactoring-Aufgaben an isolierte Git-Worktrees mit einer automatischen **3-stufigen Ausfallkette** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`) bei Erreichen von Kontingentgrenzen oder 429-Fehlern.

**Hauptmerkmale:**
- Automatische Erkennung von 429- und Quotenfehlern mit nahtloser Umschaltung
- Verwaltung isolierter Git-Worktrees
- Strikte Hermes-Kontrolle über Kanban-Status, Diffs und Tests
- Enthaltenes Skript: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## Lizenz

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
