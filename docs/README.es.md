# plugins de epicsagas

> Plugins artesanales para desarrollo serio asistido por IA — agentes autónomos, compresión de contexto y herramientas que no estorban.

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

El hub lleva solo el lineup central de epiccounty. El resto vive en su propio repositorio con un marketplace independiente del mismo nombre (ver [Plugins individualizados](#plugins-individualizados)).

| Plugin | Descripción | Fuente |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Harness de agentes autónomos — 8 comandos, habilidades autoevolutivas y hooks invisibles que protegen, pulen y reflexionan cada sesión. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Lector de documentos optimizado para tokens — comprime silenciosamente `.md`, `.html` y `.txt` al leer, reduciendo el contexto hasta 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Servidor MCP de documentación — búsqueda híbrida BM25+vector, lint y gestión de ciclo de vida launchd para docs de proyecto. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | Sistema de publicación AI-nativo — flujos autónomos multifase desde la ideación hasta EPUB/PDF. Construye libros como software. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | Grafo de conocimiento de ingeniería de software — patrones, code smells, refactorings y análisis arquitectónico con revisión de código por IA. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Gestión del ciclo de vida de bóvedas Obsidian — clasificación de bandeja con IA, refuerzo del grafo, regeneración de MOCs y sincronización multibóveda. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Colección de habilidades de agente personales — descubrimiento de problemas (5 Whys, JTBD, Fishbone), introspección y preparación para publicar OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [kanban-dev-lane](#kanban-dev-lane) | Carril de implementación multimotor autónomo — delega código en worktrees aislados con conmutación automática (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## Instalación

### Claude Code (recomendado)

Registra el marketplace una vez y luego instala cualquier plugin:

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

Todos los plugins quedan disponibles de inmediato.

### Hermes Agent

Un comando instala el suite epiccounty completo — 6 plugins, 32 herramientas:

```bash
hermes plugins install epicsagas/plugins --enable
```

O instala y activa plugins individuales:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

**Requisitos previos:** Cada plugin envuelve un binario CLI de Rust. Instala los que necesites:

```bash
brew install epicsagas/tap/alcove          # plugin alcove
brew install epicsagas/tap/episteme        # plugin episteme (requiere `epis serve` en ejecución)
brew install epicsagas/tap/epic-harness    # plugin epic-harness
brew install epicsagas/tap/llm-transpile   # plugin llm-transpile
brew install epicsagas/tap/obsidian-forge  # plugin obsidian-forge
```

**Inicio rápido — instalar todo de una vez:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## Instalación independiente

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # binario precompilado
cargo install epic-harness    # compilar desde fuente
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

## Plugins individualizados

Estos plugins salieron del hub. Cada repositorio incluye su propio marketplace con el nombre del plugin, así que se instalan de forma independiente:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| Plugin | Repositorio | Qué hace |
|--------|------------|----------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | Navegador headless como herramientas MCP — fetch, scrape, extracción markdown, JS eval. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | Compila y evoluciona un harness de agente IA personalizado desde una entrevista. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | Gestor de plugins multihuésped — scaffold, doctor, validación de instalación, publicación. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | Convierte una GeekMagic SmallTV en pantalla de estado de agente en vivo. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | Cosechador de contenido tras login — reconocimiento de API oculta, recolección a ritmo humano. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Analista de inversión en cripto de Upbit — pipeline de debate alcista/bajista con compuertas de riesgo. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | Analista de inversión en bolsa KRX — debate alcista/bajista con evidencia de flujos y ventas en corto y reglas KRX, vía la Open API de Toss Securities. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | Inteligencia de eventos AI/tech — agregador determinista de 9 fuentes. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | Corrección offline de TOEFL iBT en las 4 secciones con LLM local. |

---

## Detalles de los plugins

### epic-harness

**Harness de agentes autónomos**

Construye flujos de agente que manejan tareas complejas multipaso de forma independiente. Impulsado por 8 comandos de potencia integrados y un pipeline `/orbit` autónomo. Las habilidades evolucionan cuanto más las usas. Los hooks de sesión se ejecutan automáticamente para proteger tu código, pulir la salida y reflexionar sobre cada sesión.

**Cuándo usarlo:**
- Automatizar ciclos repetitivos de revisión, commit y pruebas
- Definir flujos de trabajo personalizados por proyecto
- Imponer patrones de comportamiento consistentes entre sesiones de Claude

**Características clave:**
- 8 comandos de potencia integrados incluido `/orbit` (pipeline totalmente autónomo)
- Sistema de habilidades autoevolutivas — aprende de patrones de uso y mejora con el tiempo
- Hooks de guarda de sesión — previene errores y mantiene la calidad automáticamente

→ [Código y documentación](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Lector de documentos optimizado para tokens**

Comprime automáticamente archivos `.md`, `.html` y `.txt` en cada llamada a la herramienta Read, reduciendo el uso de tokens de contexto hasta 40%. Surte efecto de inmediato sin cambios en tu flujo de trabajo.

**Cuándo usarlo:**
- Proyectos que referencian frecuentemente documentos o especificaciones grandes
- Cuando alcanzas los límites de ventana de contexto con regularidad
- Reducir costos de tokens en sesiones largas

**Características clave:**
- Compresión silenciosa — misma salida, hasta 40% menos tokens
- Detección automática de formatos `.md` / `.html` / `.txt`
- Totalmente compatible con los flujos existentes de la herramienta Read

→ [Código y documentación](https://github.com/epicsagas/llm-transpile)

---

### alcove

**Servidor MCP de documentación**

Da a los agentes de codificación IA acceso bajo demanda a tu documentación privada de proyecto vía MCP. Búsqueda híbrida BM25+vector, lint semántico, validación de documentos y servidor HTTP en segundo plano con modo proxy para respuesta instantánea.

**Cuándo usarlo:**
- Gestionar documentación privada de proyecto entre múltiples agentes IA
- Buscar decisiones de arquitectura, PRDs y runbooks desde cualquier agente compatible con MCP
- Imponer estándares de documentación con validación de políticas y lint semántico

**Características clave:**
- Búsqueda híbrida — BM25 + similitud vectorial con Reciprocal Rank Fusion
- Un repositorio de docs, cualquier agente — Claude Code, Cursor, Gemini CLI, Codex y 5+ más
- Servidor en segundo plano con modo proxy — elimina la latencia de arranque en frío
- Lint semántico — enlaces rotos, archivos huérfanos, marcadores obsoletos, fechas desactualizadas
- Integración launchd de macOS — comandos de ciclo de vida enable/disable/start/stop/restart

→ [Código y documentación](https://github.com/epicsagas/alcove)

---

### velith

**Sistema de publicación AI-nativo**

Construye libros como software. Flujos multifase autónomos desde página en blanco hasta EPUB/PDF publicable. Siete agentes especializados manejan estructura, borradores, continuidad, estilo, diseño de portada y marketing.

**Cuándo usarlo:**
- Escribir contenido largo estructurado (ficción, no ficción, técnico, académico)
- Mantener consistencia y voz entre capítulos en todo un libro
- Publicar a EPUB, PDF, MOBI o Markdown

**Características clave:**
- Pipeline de 6 fases: Onboarding → Ideación → Esquema → Borrador → Edición → Publicación
- 7 plantillas por género (ficción, no ficción, técnico, guion, poesía, juego, académico)
- Pipeline de edición de 5 etapas con detección de AI-slop
- Salida EPUB, PDF, MOBI, TXT, Markdown vía Pandoc + Calibre

→ [Código y documentación](https://github.com/epicsagas/Velith)

---

### episteme

**Grafo de conocimiento de ingeniería de software**

Un grafo de conocimiento consultable de patrones de diseño, code smells, refactorings y leyes de arquitectura. El análisis de código con IA detecta problemas de calidad, sugiere mejoras y fundamenta cada recomendación en principios de ingeniería establecidos.

**Cuándo usarlo:**
- Revisar código por mal uso de patrones, code smells o violaciones de arquitectura
- Elegir estrategias de refactoring con análisis de trade-offs con principios
- Aprender y aplicar leyes de ingeniería de software (Conway, Amdahl, Gall)

**Características clave:**
- Grafo de conocimiento con recorrido por patrones, smells, refactorings y leyes
- Análisis de código con IA con detección de smells y sugerencias de refactoring clasificadas
- Múltiples personas de agente — revisor de código, analista de arquitectura, asesor de ingeniería

→ [Código y documentación](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Gestión del ciclo de vida de bóvedas Obsidian**

Da a los agentes IA acceso por habilidades a operaciones de bóvedas Obsidian — clasificación de bandeja con IA y enrutado PARA, refuerzo del grafo de conocimiento (backlinks, notas puente, etiquetas automáticas), regeneración de MOCs, reparación de etiquetas/enlaces/frontmatter y ciclos completos de sincronización. Un solo binario Rust, multibóveda, cero configuración para empezar.

**Cuándo usarlo:**
- Gestionar una bóveda Obsidian (Second Brain, Zettelkasten, PARA) desde sesiones de agentes IA
- Procesar notas de bandeja con clasificación IA y enrutado automático
- Reforzar conexiones del grafo de conocimiento entre proyectos y conceptos

**Características clave:**
- 5 habilidades de agente — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- Clasificación de bandeja con IA con inyección de frontmatter y enrutado PARA
- Refuerzo del grafo de conocimiento con métricas antes/después
- Soporte multibóveda con ajustes compartidos y demonio en segundo plano (macOS)

→ [Código y documentación](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**Habilidades de agente personales**

Un conjunto curado de habilidades de agente para uso personal y de equipo — descubrimiento de problemas, autoanálisis cognitivo y preparación para publicación OSS. Sin binario requerido; las habilidades se cargan directamente desde archivos markdown.

**Cuándo usarlo:**
- Descubrir y definir problemas reales antes de construir (individuos, equipos, startups)
- Analizar tus propios patrones de pensamiento y sesgos cognitivos desde el historial de conversación
- Auditar la preparación de publicación de un proyecto OSS en comunidad, README, distribución y seguridad

**Características clave:**
- `discover` — 5 Whys, JTBD, Fishbone, interrogación socrática, mapeo de supuestos
- `cognitive-audit` — detección de sesgos basada en evidencia, análisis de decisiones, 10 rutinas accionables
- `oss-dist` — ciclo de publicación completo: estándares de comunidad, README, estrategia de lanzamiento, i18n, seguridad

→ [Código y documentación](https://github.com/epicsagas/epicsagas)

---

### kanban-dev-lane

**Carril de implementación multimotor autónomo para Hermes Kanban**

Delega tareas acotadas de implementación y refactoring desde un worker de Hermes Kanban a un git worktree aislado con una **cadena de conmutación de 3 niveles** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`), garantizando progreso continuo incluso al agotar cuotas o límites de proveedores externos.

**Características clave:**
- Detección automática de 429 y agotamiento de cuota con conmutación sin tiempo de inactividad
- Gestión del ciclo de vida de git worktrees aislados
- Hermes mantiene propiedad estricta del estado Kanban, reconciliación de diffs y pruebas de regresión
- Runner CLI incluido: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Código y documentación](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## Contribuir

Para enviar un plugin o sugerir mejoras:

1. Haz fork de este repositorio
2. Añade tu entrada de plugin a `.claude-plugin/marketplace.json` y `.agents/plugins/marketplace.json`
3. Abre un Pull Request

Los plugins se mantienen como repositorios GitHub independientes. Este marketplace solo contiene metadatos.

---

## Licencia

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
