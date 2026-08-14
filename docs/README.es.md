# epicsagas plugins

> Plugins de alta calidad para desarrollo asistido por IA profesional — agentes autónomos, compresión de contexto y herramientas que no interfieren.

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

## Lista de Plugins

| Plugin | Descripción | Fuente |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Arnés de agente autónomo — 8 comandos, habilidades autoevolutivas y hooks de sesión invisibles. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Lector de documentos optimizado para tokens — comprime `.md`, `.html`, `.txt` automáticamente, ahorrando hasta un 40% de contexto. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Servidor de documentación MCP — búsqueda híbrida BM25+vectorial, linter y gestión de ciclo de vida con launchd. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Sistema de publicación nativo de IA — flujo multifase autónomo desde la concepción hasta EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Navegador headless como herramientas MCP — fetch, scrape, extracción de markdown y JS eval. Sin configuración previa. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Grafo de conocimiento de ingeniería de software — patrones de diseño, code smells, refactorizaciones y revisión de código asistida por IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Gestión de bóvedas de Obsidian — clasificación de bandeja de entrada por IA, fortalecimiento de grafo y sincronización. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Colección de habilidades de agentes — descubrimiento de problemas (5 Whys, JTBD), autoanálisis cognitivo y auditoría OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | Asistente de investigación académica — indexación de papers (arXiv/Semantic Scholar/PDF), análisis de brechas e informes. | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — recopila conocimiento tácito mediante entrevistas y compila arneses de agentes personalizados. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | Carril de implementación autónomo multimodelo — delegación en Git worktree con conmutación por error (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## Instalación

### Claude Code (recomendado)

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

## Detalles del Plugin

### kanban-dev-lane

**Carril de implementación multimodelo para Hermes Kanban**

Delega tareas de desarrollo y refactorización a un Git worktree aislado con una cadena automática de **3 niveles de conmutación por error** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`) ante agotamiento de cuota o errores 429.

**Características clave:**
- Detección automática de 429 y cuota agotada con conmutación fluida
- Gestión de ciclo de vida en Git worktree aislado
- Control estricto de Hermes sobre el estado Kanban, diffs y pruebas
- Runner CLI incluido: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## Licencia

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
