# plugins epicsagas

> Des plugins artisanaux pour le développement sérieux assisté par IA — agents autonomes, compression de contexte et des outils qui ne vous gênent pas.

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

## Plugins

Le hub ne porte que la gamme cœur d'epiccounty. Tout le reste vit dans son propre dépôt avec un marketplace indépendant du même nom (voir [Plugins individualisés](#plugins-individualisés)).

| Plugin | Description | Source |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Harness d'agents autonomes — 8 commandes, des compétences auto-évolutives et des hooks invisibles qui protègent, peaufinent et réfléchissent chaque session. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Lecteur de documents optimisé en tokens — compresse silencieusement `.md`, `.html` et `.txt` à la lecture, réduisant le contexte jusqu'à 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Serveur MCP de documentation — recherche hybride BM25+vectorielle, lint et gestion du cycle de vie launchd pour la doc de projet. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Système de publication natif IA — flux autonomes multiphasés de l'idéation à l'EPUB/PDF. Construire des livres comme des logiciels. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | Graphe de connaissances en génie logiciel — patterns, code smells, refactorings et analyse d'architecture avec revue de code par IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Gestion du cycle de vie des coffres Obsidian — classification de boîte de réception par IA, renforcement du graphe, régénération des MOC et synchronisation multi-coffres. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Collection de compétences d'agent personnelles — découverte de problèmes (5 Whys, JTBD, Fishbone), introspection et préparation de publication OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [kanban-dev-lane](#kanban-dev-lane) | Couloir d'implémentation multi-moteur autonome — délègue le code dans des worktrees isolés avec basculement automatique (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## Installation

### Claude Code (recommandé)

Enregistrez le marketplace une fois, puis installez n'importe quel plugin :

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic@epicsagas
claude plugin install llm-transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install episteme@epicsagas
claude plugin install obsidian-forge@epicsagas
claude plugin install epicsagas@epicsagas
claude plugin install kanban-dev-lane@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

Tous les plugins sont immédiatement disponibles.

### Hermes Agent

Une commande installe la suite epiccounty complète — 6 plugins, 32 outils :

```bash
hermes plugins install epicsagas/plugins --enable
```

Ou installez et activez des plugins individuels :

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

**Prérequis :** Chaque plugin encapsule un binaire CLI Rust. Installez ceux dont vous avez besoin :

```bash
brew install epicsagas/tap/alcove          # plugin alcove
brew install epicsagas/tap/episteme        # plugin episteme (nécessite `epis serve` en cours)
brew install epicsagas/tap/epic-harness    # plugin epic-harness
brew install epicsagas/tap/llm-transpile   # plugin llm-transpile
brew install epicsagas/tap/obsidian-forge  # plugin obsidian-forge
```

**Démarrage rapide — tout installer d'un coup :**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## Installation autonome

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # binaire précompilé
cargo install epic-harness    # compiler depuis les sources
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

## Plugins individualisés

Ces plugins ont quitté le hub. Chaque dépôt embarque son propre marketplace portant le nom du plugin, donc ils s'installent de façon autonome :

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| Plugin | Dépôt | Ce qu'il fait |
|--------|------------|--------------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | Navigateur headless en outils MCP — fetch, scrape, extraction markdown, JS eval. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | Compile et fait évoluer un harness d'agent IA personnalisé depuis un entretien. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | Gestionnaire de plugins multi-hôtes — scaffold, doctor, validation d'installation, publication. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | Transforme une GeekMagic SmallTV en écran d'état d'agent en direct. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | Collecteur de contenu derrière login — reconnaissance d'API cachée, collecte au rythme humain. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Analyste d'investissement crypto Upbit — pipeline de débat haussier/baissier avec portes de risque. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | Analyste d'investissement actions KRX — débat haussier/baissier avec preuves de flux et ventes à découvert et règles KRX, via l'Open API de Toss Securities. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | Veille d'événements IA/tech — agrégateur déterministe de 9 sources. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | Correction hors-ligne du TOEFL iBT sur les 4 sections avec un LLM local. |

---

## Détails des plugins

### epic-harness

**Harness d'agents autonomes**

Construisez des flux d'agents qui traitent seuls des tâches complexes multi-étapes. Propulsé par 8 commandes puissance intégrées et un pipeline `/orbit` autonome. Les compétences évoluent à l'usage. Les hooks de session s'exécutent automatiquement pour protéger votre code, peaufiner la sortie et réfléchir à chaque session.

**Quand l'utiliser :**
- Automatiser les cycles répétitifs de revue, commit et tests
- Définir des flux de travail personnalisés par projet
- Imposer des comportements cohérents entre sessions Claude

**Fonctionnalités clés :**
- 8 commandes puissance intégrées dont `/orbit` (pipeline pleinement autonome)
- Système de compétences auto-évolutives — apprend des motifs d'usage et s'améliore
- Hooks de garde de session — prévient les erreurs et maintient la qualité automatiquement

→ [Sources et documentation](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Lecteur de documents optimisé en tokens**

Compresse automatiquement les fichiers `.md`, `.html` et `.txt` à chaque appel de l'outil Read, réduisant l'usage de tokens de contexte jusqu'à 40%. Prend effet immédiatement, sans changer vos flux.

**Quand l'utiliser :**
- Projets qui référencent souvent de gros documents ou spécifications
- Quand vous atteignez régulièrement les limites de fenêtre de contexte
- Réduire les coûts de tokens sur les longues sessions

**Fonctionnalités clés :**
- Compression silencieuse — même sortie, jusqu'à 40% de tokens en moins
- Détection automatique des formats `.md` / `.html` / `.txt`
- Entièrement compatible avec les flux existants de l'outil Read

→ [Sources et documentation](https://github.com/epicsagas/llm-transpile)

---

### alcove

**Serveur MCP de documentation**

Donne aux agents de codage IA un accès à la demande à votre documentation de projet privée via MCP. Recherche hybride BM25+vectorielle, lint sémantique, validation de documents et serveur HTTP en arrière-plan avec mode proxy pour une réponse instantanée.

**Quand l'utiliser :**
- Gérer la documentation privée de projet à travers plusieurs agents IA
- Chercher décisions d'architecture, PRDs et runbooks depuis tout agent compatible MCP
- Imposer des standards de documentation avec validation de politiques et lint sémantique

**Fonctionnalités clés :**
- Recherche hybride — BM25 + similarité vectorielle avec Reciprocal Rank Fusion
- Un dépôt de docs, tous les agents — Claude Code, Cursor, Gemini CLI, Codex et 5+ autres
- Serveur en arrière-plan avec mode proxy — élimine la latence de démarrage à froid
- Lint sémantique — liens cassés, fichiers orphelins, marqueurs obsolètes, dates périmées
- Intégration launchd macOS — commandes de cycle de vie enable/disable/start/stop/restart

→ [Sources et documentation](https://github.com/epicsagas/alcove)

---

### velith

**Système de publication natif IA**

Construisez des livres comme des logiciels. Flux autonomes multiphasés de la page blanche à l'EPUB/PDF publiable. Sept agents spécialisés gèrent structure, rédaction, continuité, style, couverture et marketing.

**Quand l'utiliser :**
- Écrire du contenu long structuré (fiction, non-fiction, technique, académique)
- Maintenir la cohérence et la voix entre chapitres sur tout un livre
- Publier en EPUB, PDF, MOBI ou Markdown

**Fonctionnalités clés :**
- Pipeline en 6 phases : Onboarding → Idéation → Plan → Rédaction → Édition → Publication
- 7 gabarits par genre (fiction, non-fiction, technique, scénario, poésie, jeu, académique)
- Pipeline d'édition en 5 étapes avec détection de AI-slop
- Sortie EPUB, PDF, MOBI, TXT, Markdown via Pandoc + Calibre

→ [Sources et documentation](https://github.com/epicsagas/Velith)

---

### episteme

**Graphe de connaissances en génie logiciel**

Un graphe de connaissances interrogeable de patterns de conception, code smells, refactorings et lois d'architecture. L'analyse de code par IA détecte les problèmes de qualité, suggère des améliorations et ancre chaque recommandation dans des principes d'ingénierie établis.

**Quand l'utiliser :**
- Relire du code pour mauvais usage de patterns, code smells ou violations d'architecture
- Choisir des stratégies de refactoring avec analyse de compromis principielle
- Apprendre et appliquer les lois du génie logiciel (Conway, Amdahl, Gall)

**Fonctionnalités clés :**
- Graphe de connaissances avec traversée across patterns, smells, refactorings et lois
- Analyse de code par IA avec détection de smells et suggestions de refactoring classées
- Plusieurs personas d'agent — relecteur de code, analyste d'architecture, conseiller en ingénierie

→ [Sources et documentation](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Gestion du cycle de vie des coffres Obsidian**

Donne aux agents IA un accès par compétences aux opérations de coffres Obsidian — classification de boîte de réception par IA avec routage PARA, renforcement du graphe de connaissances (backlinks, notes pont, tags automatiques), régénération des MOC, réparation tags/liens/frontmatter et cycles de synchronisation complets. Binaire Rust unique, multi-coffres, zéro configuration pour démarrer.

**Quand l'utiliser :**
- Gérer un coffre Obsidian (Second Brain, Zettelkasten, PARA) depuis des sessions d'agents IA
- Traiter les notes de boîte de réception avec classification IA et routage automatique
- Renforcer les connexions du graphe de connaissances entre projets et concepts

**Fonctionnalités clés :**
- 5 compétences d'agent — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- Classification de boîte de réception par IA avec injection de frontmatter et routage PARA
- Renforcement du graphe avec rapport de métriques avant/après
- Support multi-coffres avec réglages partagés et daemon en arrière-plan (macOS)

→ [Sources et documentation](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**Compétences d'agent personnelles**

Un ensemble curated de compétences d'agent pour usage personnel et d'équipe — découverte de problèmes, auto-analyse cognitive et préparation de publication OSS. Aucun binaire requis ; les compétences se chargent directement depuis des fichiers markdown.

**Quand l'utiliser :**
- Découvrir et définir de vrais problèmes avant de construire (individus, équipes, startups)
- Analyser vos propres schémas de pensée et biais cognitifs depuis l'historique de conversation
- Auditer la préparation de publication d'un projet OSS : communauté, README, distribution, sécurité

**Fonctionnalités clés :**
- `discover` — 5 Whys, JTBD, Fishbone, questionnement socratique, cartographie des hypothèses
- `cognitive-audit` — détection de biais fondée sur preuves, analyse de décisions, 10 routines actionnables
- `oss-dist` — cycle de publication complet : standards communauté, README, stratégie de lancement, i18n, sécurité

→ [Sources et documentation](https://github.com/epicsagas/epicsagas)

---

### kanban-dev-lane

**Couloir d'implémentation multi-moteur autonome pour Hermes Kanban**

Délègue des tâches d'implémentation et de refactoring bornées depuis un worker Hermes Kanban vers un git worktree isolé avec une **chaîne de basculement à 3 niveaux** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`), garantissant une progression continue même en cas d'épuisement de quotas de fournisseurs externes.

**Fonctionnalités clés :**
- Détection automatique des 429 et épuisement de quota avec basculement sans interruption
- Gestion du cycle de vie des git worktrees isolés
- Hermes garde la propriété stricte de l'état Kanban, de la réconciliation des diffs et des tests de régression
- Runner CLI embarqué : `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Sources et documentation](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## Contribuer

Pour soumettre un plugin ou suggérer des améliorations :

1. Forkez ce dépôt
2. Ajoutez votre entrée de plugin à `.claude-plugin/marketplace.json` et `.agents/plugins/marketplace.json`
3. Ouvrez un Pull Request

Les plugins sont maintenus comme des dépôts GitHub indépendants. Ce marketplace ne contient que des métadonnées.

---

## Licence

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
