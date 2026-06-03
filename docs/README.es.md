# epicsagas plugins

> Plugins artesanales para el desarrollo serio asistido por IA — agentes autónomos, compresión de contexto y herramientas que no interrumpen tu flujo.

[![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)](../LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green?style=flat)](https://github.com/epicsagas/claude-plugins)
[![Plugins](https://img.shields.io/badge/Plugins-6-blueviolet?style=flat)](https://github.com/epicsagas/claude-plugins)
[![GitHub Stars](https://img.shields.io/github/stars/epicsagas/claude-plugins?style=flat)](https://github.com/epicsagas/claude-plugins/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/epicsaga)

**Traducciones:** [English](../README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [简体中文](README.zh-cn.md) · [繁體中文](README.zh-tw.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## Plugins

| Plugin | Descripción | Fuente |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Arnés de agente autónomo — 6 comandos potentes, habilidades auto-evolutivas y hooks invisibles que protegen, pulen y reflexionan en cada sesión. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Lector de documentos optimizado en tokens — comprime silenciosamente archivos `.md`, `.html` y `.txt`, reduciendo el uso de contexto hasta un 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Servidor MCP de documentación — búsqueda híbrida BM25+vectorial, lint y gestión del ciclo de vida launchd para documentos de proyecto | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Sistema de publicación nativo de IA — flujos de trabajo autónomos multifase desde la ideación hasta EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Navegador headless como herramientas MCP — fetch, scrape, extracción de markdown, eval JS. Sin configuración, instalación automática. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Grafo de conocimiento de ingenieria de software — patrones de diseno, code smells, refactorizaciones y analisis de arquitectura con revision de codigo impulsada por IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |

---

## Instalación

### Mediante Claude Code (recomendado)

Agrega el marketplace y luego instala los plugins:

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic-harness@epicsagas
claude plugin install llm-transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install obscura-plugin@epicsagas
claude plugin install episteme@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

Todos los plugins listos para usar — sin configuración adicional.

### epic-harness — instalación independiente

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall** (binario precompilado):
```bash
cargo binstall epic-harness
```

**Cargo** (compilar desde fuente):
```bash
cargo install epic-harness
```

### llm-transpile — instalación independiente

**cargo-binstall** (binario precompilado):
```bash
cargo binstall llm-transpile
```

**Cargo** (compilar desde fuente):
```bash
cargo install llm-transpile
```

### alcove — instalación independiente

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall** (binario precompilado):
```bash
cargo binstall alcove
```

**Cargo** (compilar desde fuente):
```bash
cargo install alcove
```

### episteme — instalación independiente

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/episteme
```

**cargo-binstall** (binario precompilado):
```bash
cargo binstall episteme
```

**Cargo** (compilar desde fuente):
```bash
cargo install episteme
```

---

## Detalles de los plugins

### epic-harness

**Arnés de Agente Autónomo**

Construye flujos de trabajo de agentes que manejan tareas complejas y de múltiples pasos de forma independiente. Equipado con 6 comandos potentes integrados, las habilidades evolucionan con el uso. Los hooks de sesión se ejecutan automáticamente para proteger tu código, pulir la salida y reflexionar sobre cada sesión.

**Cuándo usarlo:**
- Automatizar ciclos repetitivos de revisión de código, commits y pruebas
- Definir flujos de trabajo personalizados por proyecto
- Aplicar patrones de comportamiento consistentes en las sesiones de Claude

**Características principales:**
- 6 comandos potentes integrados (commit, review, test, deploy y más)
- Sistema de habilidades auto-evolutivas — aprende de los patrones de uso y mejora continuamente
- Hooks de guardia de sesión — previene errores y mantiene la calidad automáticamente

→ [Fuente y Documentación](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Lector de Documentos Optimizado en Tokens**

Comprime automáticamente archivos `.md`, `.html` y `.txt` en cada llamada a la herramienta Read, reduciendo el uso de tokens de contexto hasta un 40%. Efecto inmediato sin cambios en el flujo de trabajo.

**Cuándo usarlo:**
- Proyectos que referencian frecuentemente documentos grandes o especificaciones
- Cuando alcanzas regularmente los límites de la ventana de contexto
- Para reducir costos de tokens en sesiones largas

**Características principales:**
- Compresión silenciosa — misma salida, hasta 40% menos tokens
- Detecta automáticamente formatos `.md` / `.html` / `.txt`
- Totalmente compatible con los flujos de trabajo existentes de la herramienta Read

→ [Fuente y Documentación](https://github.com/epicsagas/llm-transpile)

---

### alcove

**Servidor MCP de Documentación**

Proporciona a los agentes de codificación IA acceso bajo demanda a la documentación privada de tu proyecto a través de MCP. Búsqueda híbrida BM25+vectorial, lint semántico, validación de documentos y servidor HTTP en segundo plano con modo proxy para respuesta instantánea.

**Cuándo usarlo:**
- Gestionar documentación privada de proyectos entre múltiples agentes IA
- Buscar decisiones de arquitectura, PRDs y runbooks desde cualquier agente compatible con MCP
- Aplicar estándares de documentación con validación de políticas y lint semántico

**Características principales:**
- Búsqueda híbrida — BM25 + similitud vectorial con Reciprocal Rank Fusion
- Un repositorio de documentos, cualquier agente — Claude Code, Cursor, Gemini CLI, Codex y más de 5 más
- Servidor en segundo plano con modo proxy — elimina la latencia de inicio en frío en nuevas sesiones
- Lint semántico — enlaces rotos, archivos huérfanos, marcadores obsoletos, declaraciones de fechas desactualizadas
- Integración con macOS launchd — comandos de ciclo de vida enable/disable/start/stop/restart

→ [Fuente y Documentación](https://github.com/epicsagas/alcove)

---

### velith

**AI-Native Publishing System**

Build books like software. Autonomous multi-phase workflows from blank page to publishable EPUB/PDF.

**Key features:**
- 6-phase pipeline: Onboarding → Ideation → Outlining → Drafting → Editing → Publishing
- 7 genre templates (fiction, non-fiction, technical, screenplay, poetry, game, academic)
- 5-stage editing pipeline with AI-slop detection
- EPUB, PDF, MOBI, TXT, Markdown output

→ [Source & Docs](https://github.com/epicsagas/Velith)

---

### obscura-plugin

**Headless Browser as MCP Tools**

Gives AI agents direct access to the web via five MCP tools. Auto-installs required binaries on first load.

**Key features:**
- Zero config — plugin auto-installs all required binaries
- `obscura_scrape` with configurable concurrency via `obscura-worker`
- `obscura_serve` exposes a CDP WebSocket server for Playwright/Puppeteer
- Stealth mode for anti-detection

→ [Source & Docs](https://github.com/epicsagas/obscura-plugin)

---

### episteme

**Grafo de Conocimiento de Ingenieria de Software**

Un grafo de conocimiento consultable de patrones de diseno, code smells, refactorizaciones y leyes de arquitectura. El analisis de codigo impulsado por IA detecta problemas de calidad, sugiere mejoras y fundamenta cada recomendacion en principios de ingenieria establecidos.

**Cuando usarlo:**
- Revision de codigo por uso incorrecto de patrones, code smells o violaciones de arquitectura
- Eleccion de estrategias de refactorizacion con analisis de compensaciones basado en principios
- Aprendizaje y aplicacion de leyes de ingenieria de software (Ley de Conway, Ley de Amdahl, Ley de Gall)

**Caracteristicas clave:**
- Grafo de conocimiento con recorrido entre patrones, smells, refactorizaciones y leyes
- Analisis de codigo IA con deteccion de smells y sugerencias de refactorizacion priorizadas
- Multiples personalidades de agente — revisor de codigo, analista de arquitectura, asesor de ingenieria

→ [Codigo fuente y documentacion](https://github.com/epicsagas/Episteme)

---

## Contribuir

Para enviar un plugin o sugerir mejoras:

1. Haz un fork de este repositorio
2. Agrega tu entrada de plugin en `.claude-plugin/marketplace.json`
3. Abre un Pull Request

Los plugins se mantienen como repositorios independientes de GitHub. Este marketplace contiene solo metadatos.

---

## Licencia

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
