# epicsagas плагины

> Набор плагинов для профессиональной разработки с поддержкой ИИ — автономные агенты, сжатие контекста и инструменты, которые не мешают работе.

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

## Список плагинов

| Плагин | Описание | Источник |
|--------|----------|----------|
| [epic-harness](#epic-harness) | Каркас автономного агента — 8 команд, саморазвивающиеся навыки и невидимые хуки сессий. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Оптимизированный для токенов ридер — сжимает `.md`, `.html`, `.txt`, экономя до 40% контекста. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | Сервер документации MCP — гибридный поиск BM25+векторный, линтер и управление с помощью launchd. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | ИИ-нативная издательская система — автономный многофазный процесс от идеи до EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Headless браузер как инструменты MCP — fetch, scrape, извлечение markdown и запуск JS без настройки. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Граф знаний программной инженерии — паттерны проектирования, код-смеллы, рефакторинг и аудит кода. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Управление хранилищем Obsidian — ИИ-сортировка входящих, усиление графа и синхронизация. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Коллекция навыков агента — поиск проблем (5 Whys, JTBD), когнитивный самоанализ и аудит релизов OSS. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | Помощник в научных исследованиях — индексация статей (arXiv/Semantic Scholar/PDF), анализ пробелов и отчеты. | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — сбор неявных знаний через интервью для компиляции персонализированных каркасов агентов. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | Автономный мульти-движковый поток разработки — делегирование в Git worktree с аварийным переключением (Claudy ➔ Codex ➔ AGYD). | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## Установка

### Claude Code (рекомендуется)

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

## Описание плагина

### kanban-dev-lane

**Мульти-движковый поток реализации для Hermes Kanban**

Делегирует задачи разработки и рефакторинга в изолированное рабочее дерево Git с автоматической **3-уровневой цепочкой аварийного переключения** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`) при исчерпании лимитов или ошибках 429.

**Ключевые особенности:**
- Автоматическое обнаружение ошибок 429 и исчерпания квот с плавным переключением
- Управление жизненным циклом изолированного Git worktree
- Строгий контроль Hermes за статусом Kanban, диффами и тестами
- Встроенный раннер: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## Лицензия

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
