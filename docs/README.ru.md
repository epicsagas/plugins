# epicsagas плагины

> Тщательно созданные плагины для серьёзной разработки с поддержкой ИИ — автономные агенты, сжатие контекста и инструменты, которые не мешают вашему процессу.

[![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)](../LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green?style=flat)](https://github.com/epicsagas/claude-plugins)
[![Plugins](https://img.shields.io/badge/Plugins-6-blueviolet?style=flat)](https://github.com/epicsagas/claude-plugins)
[![GitHub Stars](https://img.shields.io/github/stars/epicsagas/claude-plugins?style=flat)](https://github.com/epicsagas/claude-plugins/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/epicsaga)

**Переводы:** [English](../README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [简体中文](README.zh-cn.md) · [繁體中文](README.zh-tw.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [العربية](README.ar.md)

---

## Плагины

| Плагин | Описание | Источник |
|--------|----------|----------|
| [epic-harness](#epic-harness) | Автономный агентский фреймворк — 6 мощных команд, самоэволюционирующие навыки и невидимые хуки, которые защищают, улучшают и анализируют каждую сессию. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Оптимизированный по токенам считыватель документов — беззвучно сжимает файлы `.md`, `.html` и `.txt`, сокращая использование контекста до 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP-сервер документации — гибридный поиск BM25+векторный, линтинг и управление жизненным циклом launchd для проектной документации. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | ИИ-нативная издательская система — автономные многофазные рабочие процессы от идеи до EPUB/PDF. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | Безголовый браузер как MCP-инструменты — fetch, scrape, извлечение Markdown, JS eval. Без настройки, автоматическая установка. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | Граф знаний программной инженерии — шаблоны проектирования, код-смеллы, рефакторинги и анализ архитектуры с ИИ-ревью кода. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |

---

## Установка

### Через Claude Code (рекомендуется)

Добавьте маркетплейс и установите плагины:

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

Все плагины сразу доступны — дополнительная настройка не требуется.

### epic-harness — автономная установка

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall** (готовый бинарник):
```bash
cargo binstall epic-harness
```

**Cargo** (сборка из исходников):
```bash
cargo install epic-harness
```

### llm-transpile — автономная установка

**cargo-binstall** (готовый бинарник):
```bash
cargo binstall llm-transpile
```

**Cargo** (сборка из исходников):
```bash
cargo install llm-transpile
```

### alcove — автономная установка

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall** (готовый бинарник):
```bash
cargo binstall alcove
```

**Cargo** (сборка из исходников):
```bash
cargo install alcove
```

### episteme — автономная установка

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/episteme
```

**cargo-binstall** (готовый бинарник):
```bash
cargo binstall episteme
```

**Cargo** (сборка из исходников):
```bash
cargo install episteme
```

---

## Подробности о плагинах

### epic-harness

**Автономный Агентский Фреймворк**

Создавайте рабочие процессы агентов, которые самостоятельно справляются со сложными многоэтапными задачами. Оснащён 6 встроенными мощными командами, навыки эволюционируют по мере использования. Хуки сессии запускаются автоматически, защищая ваш код, улучшая вывод и анализируя каждую сессию.

**Когда использовать:**
- Автоматизация повторяющихся циклов проверки кода, коммитов и тестов
- Определение пользовательских рабочих процессов для отдельных проектов
- Применение единообразных паттернов поведения в сессиях Claude

**Ключевые возможности:**
- 6 встроенных мощных команд (commit, review, test, deploy и другие)
- Самоэволюционирующая система навыков — учится на паттернах использования и постоянно улучшается
- Хуки защиты сессии — автоматически предотвращают ошибки и поддерживают качество

→ [Исходный код и документация](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Оптимизированный по Токенам Считыватель Документов**

Автоматически сжимает файлы `.md`, `.html` и `.txt` при каждом вызове инструмента Read, сокращая использование токенов контекста до 40%. Немедленный эффект без изменений рабочего процесса.

**Когда использовать:**
- Проекты, часто ссылающиеся на большие документы или спецификации
- Когда вы регулярно достигаете ограничений окна контекста
- Для снижения затрат на токены в длительных сессиях

**Ключевые возможности:**
- Беззвучное сжатие — тот же вывод, до 40% меньше токенов
- Автоматическое определение форматов `.md` / `.html` / `.txt`
- Полная совместимость с существующими рабочими процессами инструмента Read

→ [Исходный код и документация](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP-сервер Документации**

Предоставляет ИИ-агентам для кодирования доступ к вашим приватным проектным документам по запросу через MCP. Гибридный поиск BM25+векторный, семантический линтинг, валидация документов и фоновый HTTP-сервер с режимом прокси для мгновенного отклика.

**Когда использовать:**
- Управление приватной проектной документацией через несколько ИИ-агентов
- Поиск архитектурных решений, PRD и runbook-ов из любого MCP-совместимого агента
- Применение стандартов документации с валидацией политик и семантическим линтингом

**Ключевые возможности:**
- Гибридный поиск — BM25 + векторное сходство с Reciprocal Rank Fusion
- Один doc-репозиторий, любой агент — Claude Code, Cursor, Gemini CLI, Codex и более 5 других
- Фоновый сервер с режимом прокси — устраняет задержку холодного старта при новых сессиях
- Семантический линтинг — битые ссылки, осиротевшие файлы, устаревшие маркеры, неактуальные даты
- Интеграция с macOS launchd — команды жизненного цикла enable/disable/start/stop/restart

→ [Исходный код и документация](https://github.com/epicsagas/alcove)

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

**Граф знаний программной инженерии**

Запрашиваемый граф знаний шаблонов проектирования, код-смеллов, рефакторингов и архитектурных законов. ИИ-анализ кода выявляет проблемы качества, предлагает улучшения и обосновывает каждую рекомендацию устоявшимися инженерными принципами.

**Когда использовать:**
- Ревью кода на неправильное использование паттернов, код-смеллы или архитектурные нарушения
- Выбор стратегий рефакторинга с принципиальным анализом компромиссов
- Изучение и применение законов программной инженерии (Закон Конвея, Закон Амдала, Закон Галла)

**Ключевые возможности:**
- Граф знаний с обходом между паттернами, смеллами, рефакторингами и законами
- ИИ-анализ кода с обнаружением смеллов и ранжированными предложениями по рефакторингу
- Несколько персон агентов — ревьюер кода, архитектурный аналитик, инженерный консультант

→ [Исходный код и документация](https://github.com/epicsagas/Episteme)

---

## Участие в разработке

Для отправки плагина или предложений по улучшению:

1. Сделайте форк этого репозитория
2. Добавьте запись о плагине в `.claude-plugin/marketplace.json`
3. Откройте Pull Request

Плагины поддерживаются как независимые репозитории GitHub. Этот маркетплейс содержит только метаданные.

---

## Лицензия

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
