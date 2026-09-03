# epicsagas Plugins

> Handgefertigte Plugins für ernsthaftes KI-gestütztes Entwickeln — autonome Agenten, Kontextkomprimierung und Werkzeuge, die nicht im Weg stehen.

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

Der Hub trägt nur die Kern-Linie von epiccounty. Alles andere lebt im eigenen Repository mit einem gleichnamigen eigenständigen Marketplace (siehe [Individualisierte Plugins](#individualisierte-plugins)).

| Plugin | Beschreibung | Quelle |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Autonomes Agenten-Harness — 8 Befehle, sich selbst weiterentwickelnde Skills und unsichtbare Hooks, die jede Session bewachen, polieren und reflektieren. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Token-optimierter Dokumentenleser — komprimiert `.md`, `.html` und `.txt` beim Lesen unbemerkt und senkt den Kontextverbrauch um bis zu 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP-Dokumentationsserver — hybride BM25+Vektor-Suche, Lint und launchd-Lebenszyklusverwaltung für Projektdokumentation. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | KI-natives Publikationssystem — autonome mehrphasige Workflows von der Ideation bis EPUB/PDF. Baue Bücher wie Software. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | Wissensgraph für Software Engineering — Entwurfsmuster, Code Smells, Refactorings und Architekturanalyse mit KI-gestützter Codeprüfung. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Lebenszyklusverwaltung für Obsidian-Tresore — KI-Posteingangsklassifikation, Graphverstärkung, MOC-Regenerierung und Multi-Tresor-Sync als Agenten-Skills. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Persönliche Agenten-Skill-Sammlung — Problementdeckung (5 Whys, JTBD, Fishbone), Introspektion und OSS-Veröffentlichungsbereitschaft. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## Installation

### Claude Code (empfohlen)

Marketplace einmal registrieren, dann beliebige Plugins installieren:

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

Alle Plugins stehen sofort zur Verfügung.

### Hermes Agent

Ein Befehl installiert die komplette epiccounty-Suite — 6 Plugins, 32 Werkzeuge:

```bash
hermes plugins install epicsagas/plugins --enable
```

Oder einzelne Plugins installieren und aktivieren:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` ist Hermes-exklusiv — in `.hermes/` dieses Repos gebündelt, nicht in den Claude/Codex-Marketplaces veröffentlicht.

**Voraussetzungen:** Jedes Plugin umhüllt ein Rust-CLI-Binary. Installiere nur die benötigten:

```bash
brew install epicsagas/tap/alcove          # Plugin alcove
brew install epicsagas/tap/episteme        # Plugin episteme (benötigt laufendes `epis serve`)
brew install epicsagas/tap/epic-harness    # Plugin epic-harness
brew install epicsagas/tap/llm-transpile   # Plugin llm-transpile
brew install epicsagas/tap/obsidian-forge  # Plugin obsidian-forge
```

**Schnellstart — alles auf einmal installieren:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## Eigenständige Installation

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # vorkompiliertes Binary
cargo install epic-harness    # aus dem Quellcode bauen
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

## Individualisierte Plugins

Diese Plugins haben den Hub verlassen. Jedes Repository bringt einen eigenen, nach dem Plugin benannten Marketplace mit und ist damit eigenständig installierbar:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| Plugin | Repository | Was es tut |
|--------|------------|-----------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | Headless-Browser als MCP-Werkzeuge — fetch, scrape, Markdown-Extraktion, JS eval. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | Kompiliert und entwickelt aus einem Interview ein personalisiertes KI-Agenten-Harness. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | Multi-Host-Plugin-Manager — Scaffold, Doctor, Installationsvalidierung, Publish. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | Macht eine GeekMagic SmallTV zum Live-Statusdisplay für Agenten. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | Content-Ernter hinter Login — versteckte-API-Aufklärung, Sammeln im menschlichen Tempo. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Upbit-Krypto-Investitionsanalyst — Bullen/Bären-Debatten-Pipeline mit Risiko-Gates. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | KRX-Aktienanalyst — Bullen/Bären-Debatte mit Geldfluss/Leerverkaufs-Evidenz und KRX-Regeln, über die Toss Securities Open API. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | KI/Tech-Event-Intelligenz — deterministischer 9-Quellen-Aggregator. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | Offline-Bewertung des TOEFL iBT in allen 4 Bereichen mit einem lokalen LLM. |
| wishket-radar | [epicsagas/wishket-radar](https://github.com/epicsagas/wishket-radar) | Wishket-Projektradar — Suche, Tiefenanalyse und Tech-Matching von Outsourcing-Projekten. |

---

## Plugin-Details

### epic-harness

**Autonomes Agenten-Harness**

Baue Agenten-Workflows, die komplexe mehrstufige Aufgaben selbstständig abarbeiten. Angetrieben von 8 eingebauten Power-Befehlen und einer autonomen `/orbit`-Pipeline. Skills entwickeln sich mit der Nutzung weiter. Session-Hooks laufen automatisch und bewachen den Code, polieren die Ausgabe und reflektieren jede Session.

**Wann einsetzen:**
- Wiederkehrende Zyklen aus Codeprüfung, Commit und Tests automatisieren
- Projektbezogene Custom-Workflows definieren
- Konsistente Verhaltensmuster über Claude-Sessions hinweg erzwingen

**Zentrale Funktionen:**
- 8 eingebaute Power-Befehle, darunter `/orbit` (vollautonome Pipeline)
- Selbst-evolvierendes Skill-System — lernt aus Nutzungsmustern und verbessert sich
- Session-Guard-Hooks — verhindert Fehler und hält die Qualität automatisch aufrecht

→ [Quelle & Dokumentation](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Token-optimierter Dokumentenleser**

Komprimiert `.md`-, `.html`- und `.txt`-Dateien bei jedem Read-Aufruf automatisch und senkt den Kontext-Token-Verbrauch um bis zu 40%. Wirkt sofort, ohne Workflow-Änderungen.

**Wann einsetzen:**
- Projekte, die häufig große Dokumente oder Specs referenzieren
- Wenn du regelmäßig an Kontextfenster-Grenzen stößt
- Token-Kosten in langen Sessions senken

**Zentrale Funktionen:**
- Stille Komprimierung — gleiche Ausgabe, bis zu 40% weniger Tokens
- Erkennt `.md` / `.html` / `.txt`-Formate automatisch
- Vollständig kompatibel mit bestehenden Read-Tool-Workflows

→ [Quelle & Dokumentation](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP-Dokumentationsserver**

Gibt KI-Coding-Agenten bedarfsgesteuerten Zugriff auf deine private Projektdokumentation per MCP. Hybride BM25+Vektor-Suche, semantischer Lint, Dokumentenvalidierung und ein HTTP-Hintergrundserver mit Proxy-Modus für sofortige Antworten.

**Wann einsetzen:**
- Private Projektdokumentation über mehrere KI-Agenten hinweg verwalten
- Architekturentscheidungen, PRDs und Runbooks aus jedem MCP-fähigen Agenten durchsuchen
- Dokumentationsstandards mit Policy-Validierung und semantischem Lint durchsetzen

**Zentrale Funktionen:**
- Hybride Suche — BM25 + Vektorähnlichkeit mit Reciprocal Rank Fusion
- Ein Doc-Repo, jeder Agent — Claude Code, Cursor, Gemini CLI, Codex und 5+ weitere
- Hintergrundserver mit Proxy-Modus — beseitigt Kaltstart-Latenz neuer Sessions
- Semantischer Lint — tote Links, verwaiste Dateien, veraltete Marker, überholte Datumsangaben
- macOS-launchd-Integration — Lebenszyklusbefehle enable/disable/start/stop/restart

→ [Quelle & Dokumentation](https://github.com/epicsagas/alcove)

---

### velith

**KI-natives Publikationssystem**

Baue Bücher wie Software. Autonome mehrphasige Workflows vom leeren Blatt bis zur publizierbaren EPUB/PDF. Sieben spezialisierte Agenten übernehmen Struktur, Entwurf, Kontinuität, Stil, Coverdesign und Marketing.

**Wann einsetzen:**
- Strukturierte Langform-Inhalte schreiben (Fiktion, Sachbuch, Technik, Wissenschaft)
- Kapitelübergreifende Konsistenz und Stimme im ganzen Buch halten
- Nach EPUB, PDF, MOBI oder Markdown publizieren

**Zentrale Funktionen:**
- 6-Phasen-Pipeline: Onboarding → Ideation → Gliederung → Entwurf → Redaktion → Publikation
- 7 Genre-Vorlagen (Fiktion, Sachbuch, Technik, Drehbuch, Poesie, Spiel, Wissenschaft)
- 5-stufige Redaktionspipeline mit KI-Slop-Erkennung
- EPUB-, PDF-, MOBI-, TXT-, Markdown-Ausgabe über Pandoc + Calibre

→ [Quelle & Dokumentation](https://github.com/epicsagas/Velith)

---

### episteme

**Wissensgraph für Software Engineering**

Ein abfragbarer Wissensgraph aus Entwurfsmustern, Code Smells, Refactorings und Architekturgesetzen. KI-gestützte Codeanalyse erkennt Qualitätsprobleme, schlägt Verbesserungen vor und verankert jede Empfehlung in etablierten Engineering-Prinzipien.

**Wann einsetzen:**
- Code auf Muster-Missbrauch, Code Smells oder Architekturverletzungen prüfen
- Refactoring-Strategien mit prinzipienbasierter Trade-off-Analyse wählen
- Software-Engineering-Gesetze (Conway, Amdahl, Gall) lernen und anwenden

**Zentrale Funktionen:**
- Wissensgraph mit Graph-Traversal über Muster, Smells, Refactorings und Gesetze
- KI-Codeanalyse mit Smell-Erkennung und gerankten Refactoring-Vorschlägen
- Mehrere Agenten-Personas — Code-Reviewer, Architektur-Analyst, Engineering-Berater

→ [Quelle & Dokumentation](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Lebenszyklusverwaltung für Obsidian-Tresore**

Gibt KI-Agenten skill-gesteuerten Zugriff auf Obsidian-Tresor-Operationen — KI-Posteingangsklassifikation mit PARA-Routing, Wissensgraph-Verstärkung (Backlinks, Bridge-Notes, Auto-Tags), MOC-Regenerierung, Tag/Link/Frontmatter-Reparatur und vollständige Sync-Zyklen. Ein einzelnes Rust-Binary, Multi-Tresor, ohne Konfiguration startklar.

**Wann einsetzen:**
- Einen Obsidian-Tresor (Second Brain, Zettelkasten, PARA) aus KI-Agenten-Sessions verwalten
- Posteingangs-Notizen mit KI-Klassifikation und automatischem Routing verarbeiten
- Wissensgraph-Verbindungen zwischen Projekten und Konzepten verstärken

**Zentrale Funktionen:**
- 5 Agenten-Skills — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- KI-Posteingangsklassifikation mit Frontmatter-Injektion und PARA-Routing
- Wissensgraph-Verstärkung mit Vorher/Nachher-Metriken
- Multi-Tresor-Support mit gemeinsamen Einstellungen und Hintergrund-Daemon (macOS)

→ [Quelle & Dokumentation](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**Persönliche Agenten-Skills**

Eine kuratierte Sammlung von Agenten-Skills für persönliche und Team-Nutzung — Problementdeckung, kognitive Selbstanalyse und OSS-Veröffentlichungsbereitschaft. Kein Binary nötig; Skills laden direkt aus Markdown-Dateien.

**Wann einsetzen:**
- Echte Probleme entdecken und definieren, bevor gebaut wird (Einzelpersonen, Teams, Startups)
- Eigene Denkmuster und kognitive Verzerrungen aus dem Gesprächsverlauf analysieren
- OSS-Veröffentlichungsbereitschaft eines Projekts über Community, README, Distribution und Sicherheit auditen

**Zentrale Funktionen:**
- `discover` — 5 Whys, JTBD, Fishbone, sokratisches Fragen, Annahmen-Mapping
- `cognitive-audit` — evidenzbasierte Bias-Erkennung, Entscheidungsanalyse, 10 umsetzbare Routinen
- `oss-dist` — kompletter Veröffentlichungszyklus: Community-Standards, README, Launch-Strategie, i18n, Sicherheit

→ [Quelle & Dokumentation](https://github.com/epicsagas/epicsagas)

---


## Mitwirken

Um ein Plugin einzureichen oder Verbesserungen vorzuschlagen:

1. Forke dieses Repository
2. Füge deinen Plugin-Eintrag zu `.claude-plugin/marketplace.json` und `.agents/plugins/marketplace.json` hinzu
3. Öffne einen Pull Request

Plugins werden als eigenständige GitHub-Repositories gepflegt. Dieser Marketplace enthält nur Metadaten.

---

## Lizenz

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
