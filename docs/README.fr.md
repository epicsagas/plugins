# epicsagas plugins

> Suite de plugins haut de gamme pour le développement assisté par IA — agents autonomes, compression de contexte et outils non intrusifs.

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

## Liste des Plugins

| Plugin | Description | Source |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Harnais d'agent autonome — 8 commandes, compétences auto-évolutives et hooks de session invisibles. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Lecteur de documents optimisé pour les tokens — compresse `.md`, `.html`, `.txt` automatiquement, économisant jusqu'à 40% de contexte. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Serveur de documentation MCP — recherche hybride BM25+vectorielle, lint sémantique et gestion launchd. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Système d'édition natif IA — flux de travail autonome multiphasé du brouillon à l'EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Navigateur headless comme outils MCP — fetch, scrape, extraction markdown et exécution JS sans configuration. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Graphe de connaissances en génie logiciel — design patterns, code smells, refactorisations et revue de code IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Gestion de coffres Obsidian — tri IA de la boîte de réception, renforcement du graphe et synchronisation. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Collection de compétences d'agent — découverte de problèmes (5 Whys, JTBD), auto-analyse cognitive et audit OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | Assistant de recherche académique — indexation d'articles (arXiv/Semantic Scholar/PDF), analyse des lacunes et rapports. | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — collecte les connaissances tacites via des entretiens pour compiler des harnais personnalisés. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | Voie de développement autonome multi-moteur — délégation sur Git worktree avec basculement automatique (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## Installation

### Claude Code (recommandé)

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

## Détails du Plugin

### kanban-dev-lane

**Voie d'implémentation multi-moteur autonome pour Hermes Kanban**

Délègue les tâches de développement et de refactorisation à un arbre de travail Git isolé avec une chaîne de **basculement automatique à 3 niveaux** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`) en cas d'épuisement des quotas ou d'erreurs 429.

**Fonctionnalités clés :**
- Détection automatique des erreurs 429 et des quotas épuisés avec basculement fluide
- Gestion du cycle de vie du Git worktree isolé
- Contrôle strict par Hermes de l'état du Kanban, des diffs et des tests
- Script d'exécution inclus : `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## Licence

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
