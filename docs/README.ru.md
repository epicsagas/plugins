# плагины epicsagas

> Тщательно сделанные плагины для серьёзной AI-разработки — автономные агенты, сжатие контекста и инструменты, которые не мешают работе.

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

## Плагины

Хаб несёт только основную линейку epiccounty. Всё остальное живёт в собственном репозитории с одноимённым независимым маркетплейсом (см. [Индивидуализированные плагины](#индивидуализированные-плагины)).

| Плагин | Описание | Источник |
|--------|-------------|--------|
| [epic-harness](#epic-harness) | Харнес автономных агентов — 8 команд, саморазвивающиеся навыки и невидимые хуки, которые охраняют, шлифуют и осмысляют каждую сессию. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Оптимизированный по токенам читатель документов — незаметно сжимает `.md`, `.html` и `.txt` при чтении, снижая расход контекста до 40%. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP-сервер документации — гибридный BM25+векторный поиск, линт и управление жизненным циклом launchd для документации проектов. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI-нативная система публикации — автономные многофазные процессы от идеи до EPUB/PDF. Создавайте книги как софт. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | Граф знаний программной инженерии — паттерны, код-смелы, рефакторинги и анализ архитектуры с AI-ревью кода. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Управление жизненным циклом хранилищ Obsidian — AI-классификация входящих, усиление графа, регенерация MOC и синхронизация нескольких хранилищ как навыки агента. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | Личная коллекция навыков агента — обнаружение проблем (5 Whys, JTBD, Fishbone), интроспекция и готовность OSS-релиза. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## Установка

### Claude Code (рекомендуется)

Зарегистрируйте маркетплейс один раз, затем ставьте любые плагины:

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

Все плагины доступны сразу.

### Hermes Agent

Одна команда ставит весь набор epiccounty — 6 плагинов, 32 инструмента:

```bash
hermes plugins install epicsagas/plugins --enable
```

Или установите и включите плагины по отдельности:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` — только для Hermes — bundled в `.hermes/` этого репозитория, не публикуется в маркетплейсах Claude/Codex.

**Предварительные требования:** Каждый плагин оборачивает Rust CLI-бинарник. Ставьте только нужные:

```bash
brew install epicsagas/tap/alcove          # плагин alcove
brew install epicsagas/tap/episteme        # плагин episteme (нужен запущенный `epis serve`)
brew install epicsagas/tap/epic-harness    # плагин epic-harness
brew install epicsagas/tap/llm-transpile   # плагин llm-transpile
brew install epicsagas/tap/obsidian-forge  # плагин obsidian-forge
```

**Быстрый старт — установить всё сразу:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## Автономная установка

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # готовый бинарник
cargo install epic-harness    # сборка из исходников
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

## Индивидуализированные плагины

Эти плагины покинули хаб. Каждый репозиторий несёт собственный маркетплейс с именем плагина, поэтому они устанавливаются автономно:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| Плагин | Репозиторий | Что делает |
|--------|------------|-----------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | Headless-браузер как MCP-инструменты — fetch, scrape, извлечение markdown, JS eval. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | Компилирует и развивает персональный AI-харнес агента из интервью. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | Мультихостовый менеджер плагинов — скаффолд, доктор, проверка установки, публикация. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | Превращает GeekMagic SmallTV в живой дисплей состояния агента. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | Сборщик контента за логином — разведка скрытого API, сбор в человеческом темпе. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Аналитик инвестиций Upbit — пайплайн дебатов быков/медведей с риск-гейтами. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | Аналитик инвестиций в акции KRX — дебаты быков/медведей с данными о потоках и коротких продажах и правилами KRX, через Open API Toss Securities. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | Разведка AI/tech-событий — детерминированный агрегатор из 9 источников. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | Офлайн-проверка TOEFL iBT по всем 4 секциям с локальным LLM. |
| wishket-radar | [epicsagas/wishket-radar](https://github.com/epicsagas/wishket-radar) | Радар проектов Wishket — поиск, глубокий анализ и техническое сопоставление аутсорс-проектов. |

---

## Подробности

### epic-harness

**Харнес автономных агентов**

Стройте агентные процессы, которые самостоятельно выполняют сложные многошаговые задачи. В основе — 8 встроенных power-команд и автономный пайплайн `/orbit`. Навыки развиваются по мере использования. Сессионные хуки автоматически охраняют код, шлифуют вывод и осмысляют каждую сессию.

**Когда использовать:**
- Автоматизация повторяющихся циклов ревью, коммитов и тестов
- Определение кастомных процессов под проект
- Принуждение к согласованным паттернам поведения между сессиями Claude

**Ключевые возможности:**
- 8 встроенных power-команд, включая `/orbit` (полностью автономный пайплайн)
- Саморазвивающаяся система навыков — учится на паттернах использования и улучшается
- Сессионные охранные хуки — предотвращает ошибки и автоматически держит качество

→ [Исходники и документация](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Оптимизированный по токенам читатель документов**

Автоматически сжимает файлы `.md`, `.html` и `.txt` при каждом вызове инструмента Read, снижая расход токенов контекста до 40%. Действует сразу, без изменения процессов.

**Когда использовать:**
- Проекты, часто обращающиеся к большим документам или спекам
- Когда регулярно упираетесь в лимиты окна контекста
- Снижение стоимости токенов в длинных сессиях

**Ключевые возможности:**
- Тихое сжатие — тот же вывод, до 40% меньше токенов
- Автоопределение форматов `.md` / `.html` / `.txt`
- Полная совместимость с существующими процессами инструмента Read

→ [Исходники и документация](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP-сервер документации**

Даёт AI-агентам для кодинга доступ по требованию к приватной документации проекта через MCP. Гибридный BM25+векторный поиск, семантический линт, валидация документов и фоновый HTTP-сервер с прокси-режимом для мгновенного ответа.

**Когда использовать:**
- Управление приватной документацией проекта между несколькими AI-агентами
- Поиск архитектурных решений, PRD и рунбуков из любого MCP-совместимого агента
- Принуждение к стандартам документации через проверку политик и семантический линт

**Ключевые возможности:**
- Гибридный поиск — BM25 + векторное сходство с Reciprocal Rank Fusion
- Один репозиторий docs, любой агент — Claude Code, Cursor, Gemini CLI, Codex и ещё 5+
- Фоновый сервер с прокси-режимом — убирает задержку холодного старта новых сессий
- Семантический линт — битые ссылки, файлы-сироты, устаревшие маркеры, просроченные даты
- Интеграция с launchd macOS — команды жизненного цикла enable/disable/start/stop/restart

→ [Исходники и документация](https://github.com/epicsagas/alcove)

---

### velith

**AI-нативная система публикации**

Создавайте книги как софт. Автономные многофазные процессы от чистого листа до готового к публикации EPUB/PDF. Семь специализированных агентов ведут структуру, черновики, преемственность, стиль, обложку и маркетинг.

**Когда использовать:**
- Написание структурированного длинного контента (художка, нон-фикшн, техника, наука)
- Поддержание согласованности и голоса между главами во всей книге
- Публикация в EPUB, PDF, MOBI или Markdown

**Ключевые возможности:**
- Пайплайн из 6 фаз: Онбординг → Идеи → План → Черновик → Редактура → Публикация
- 7 шаблонов жанров (художка, нон-фикшн, техника, сценарий, поэзия, игра, наука)
- 5-этапная редактура с детекцией AI-штампов
- Вывод в EPUB, PDF, MOBI, TXT, Markdown через Pandoc + Calibre

→ [Исходники и документация](https://github.com/epicsagas/Velith)

---

### episteme

**Граф знаний программной инженерии**

Опрашиваемый граф знаний из паттернов проектирования, код-смелов, рефакторингов и законов архитектуры. AI-анализ кода находит проблемы качества, предлагает улучшения и привязывает каждую рекомендацию к устоявшимся инженерным принципам.

**Когда использовать:**
- Ревью кода на misuse паттернов, код-смелы или нарушения архитектуры
- Выбор стратегии рефакторинга с принципиальным анализом компромиссов
- Изучение и применение законов софтверной инженерии (Конвея, Амдала, Галла)

**Ключевые возможности:**
- Граф знаний с обходом через паттерны, смелы, рефакторинги и законы
- AI-анализ кода с детекцией смелов и ранжированными предложениями рефакторинга
- Несколько персон агента — ревьюер кода, аналитик архитектуры, инженерный советник

→ [Исходники и документация](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Управление жизненным циклом хранилищ Obsidian**

Даёт AI-агентам доступ через навыки к операциям с хранилищами Obsidian — AI-классификация входящих с PARA-маршрутизацией, усиление графа знаний (обратные ссылки, мостовые заметки, автотеги), регенерация MOC, починка тегов/ссылок/frontmatter и полные циклы синхронизации. Один Rust-бинарник, несколько хранилищ, ноль конфигурации для старта.

**Когда использовать:**
- Управление хранилищем Obsidian (Second Brain, Zettelkasten, PARA) из сессий AI-агентов
- Обработка входящих заметок с AI-классификацией и автоматической маршрутизацией
- Усиление связей графа знаний между проектами и концептами

**Ключевые возможности:**
- 5 навыков агента — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- AI-классификация входящих с инъекцией frontmatter и PARA-маршрутизацией
- Усиление графа знаний с отчётом метрик до/после
- Поддержка нескольких хранилищ с общими настройками и фоновым демоном (macOS)

→ [Исходники и документация](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**Личные навыки агента**

Курированный набор навыков агента для личного и командного использования — обнаружение проблем, когнитивный самоанализ и готовность OSS-релиза. Бинарник не нужен; навыки грузятся прямо из markdown-файлов.

**Когда использовать:**
- Обнаружение и определение настоящих проблем до начала строительства (личности, команды, стартапы)
- Анализ собственных паттернов мышления и когнитивных искажений по истории диалогов
- Аудит готовности OSS-проекта к релизу: сообщество, README, дистрибуция, безопасность

**Ключевые возможности:**
- `discover` — 5 Whys, JTBD, Fishbone, сократический опрос, отображение допущений
- `cognitive-audit` — основанная на доказательствах детекция искажений, анализ решений, 10 действенных рутин
- `oss-dist` — полный цикл релиза: стандарты сообщества, README, стратегия запуска, i18n, безопасность

→ [Исходники и документация](https://github.com/epicsagas/epicsagas)

---


## Участие

Чтобы отправить плагин или предложить улучшения:

1. Сделайте форк этого репозитория
2. Добавьте запись плагина в `.claude-plugin/marketplace.json` и `.agents/plugins/marketplace.json`
3. Откройте Pull Request

Плагины поддерживаются как независимые GitHub-репозитории. Этот маркетплейс содержит только метаданные.

---

## Лицензия

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
