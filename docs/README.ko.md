# epicsagas 플러그인

> AI 기반 개발을 위해 정성껏 제작된 플러그인 — 자율 에이전트, 컨텍스트 압축, 방해 없이 작동하는 도구들.

[![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)](../LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green?style=flat)](https://github.com/epicsagas/claude-plugins)
[![Plugins](https://img.shields.io/badge/Plugins-5-blueviolet?style=flat)](https://github.com/epicsagas/claude-plugins)
[![GitHub Stars](https://img.shields.io/github/stars/epicsagas/claude-plugins?style=flat)](https://github.com/epicsagas/claude-plugins/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/epicsaga)

**번역:** [English](../README.md) · [日本語](README.ja.md) · [简体中文](README.zh-cn.md) · [繁體中文](README.zh-tw.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## 플러그인 목록

| 플러그인 | 설명 | 소스 |
|---------|------|------|
| [epic](#epic) | 자율 에이전트 하니스 — 6개의 파워 커맨드, 자가 진화 스킬, 세션마다 작동하는 보이지 않는 훅 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [transpile](#transpile) | 토큰 최적화 문서 리더 — `.md`, `.html`, `.txt` 파일을 자동 압축해 컨텍스트 사용량 최대 40% 절감 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP 문서 서버 — BM25+벡터 하이브리드 검색, 린트, 프로젝트 문서용 launchd 라이프사이클 관리 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI 네이티브 퍼블리싱 시스템 — 아이디에이션부터 EPUB/PDF까지 자율 멀티페이즈 워크플로우. 소프트웨어처럼 책을 만드세요. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura](#obscura) | 헤드리스 브라우저를 MCP 툴로 — fetch, scrape, 마크다운 추출, JS eval. 제로 설정, 바이너리 자동 설치. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |

---

## 설치

### Claude Code 사용 (권장)

마켓플레이스 추가 후 플러그인을 설치합니다:

```bash
claude plugin marketplace add epicsagas/plugins
claude plugin install epic@epicsagas
claude plugin install transpile@epicsagas
claude plugin install alcove@epicsagas
claude plugin install velith@epicsagas
claude plugin install obscura@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

모든 플러그인을 바로 사용할 수 있습니다 — 추가 설정 불필요.

### epic — 독립 설치

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall** (사전 빌드 바이너리):
```bash
cargo binstall epic-harness
```

**Cargo** (소스 빌드):
```bash
cargo install epic-harness
```

### transpile — 독립 설치

**cargo-binstall** (사전 빌드 바이너리):
```bash
cargo binstall llm-transpile
```

**Cargo** (소스 빌드):
```bash
cargo install llm-transpile
```

### alcove — 독립 설치

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall** (사전 빌드 바이너리):
```bash
cargo binstall alcove
```

**Cargo** (소스 빌드):
```bash
cargo install alcove
```

---

## 플러그인 상세

### epic

**자율 에이전트 하니스**

복잡한 멀티스텝 작업을 독립적으로 수행하는 에이전트 워크플로우를 구축합니다. 6개의 파워 커맨드로 구성되어 있으며, 스킬이 사용될수록 자가 진화합니다. 세션마다 자동으로 실행되는 훅이 코드를 보호하고, 다듬고, 반성합니다.

**언제 사용하나요?**
- 반복적인 코드 리뷰, 커밋, 테스트 사이클을 자동화할 때
- 프로젝트별 커스텀 워크플로우를 정의하고 싶을 때
- Claude 세션 전반에 걸쳐 일관된 행동 패턴이 필요할 때

**주요 기능:**
- 6개 내장 파워 커맨드 (commit, review, test, deploy 등)
- 자가 진화 스킬 시스템 — 사용 패턴을 학습하여 점진적으로 개선
- 세션 가드 훅 — 실수를 방지하고 품질을 자동으로 유지

→ [소스 및 문서](https://github.com/epicsagas/epic-harness)

---

### transpile

**토큰 최적화 문서 리더**

Read 툴 호출 시 `.md`, `.html`, `.txt` 파일을 자동으로 압축하여 컨텍스트 토큰 사용량을 최대 40% 절감합니다. 워크플로우 변경 없이 즉시 효과가 나타납니다.

**언제 사용하나요?**
- 대형 문서나 레퍼런스를 자주 참조하는 프로젝트에서
- 컨텍스트 윈도우 한계에 자주 도달할 때
- 긴 세션에서 토큰 비용을 줄이고 싶을 때

**주요 기능:**
- 무음 압축 — 출력은 동일하게, 토큰은 최대 40% 절감
- `.md` / `.html` / `.txt` 포맷 자동 감지
- 기존 Read 툴 워크플로우와 완전 호환

→ [소스 및 문서](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP 문서 서버**

AI 코딩 에이전트에게 MCP를 통해 프로젝트 비공개 문서에 대한 온디맨드 액세스를 제공합니다. BM25+벡터 하이브리드 검색, 시맨틱 린트, 문서 유효성 검증, 프록시 모드를 갖춘 백그라운드 HTTP 서버로 즉각적인 응답을 제공합니다.

**언제 사용하나요?**
- 여러 AI 에이전트에서 비공개 프로젝트 문서를 관리할 때
- MCP 호환 에이전트에서 아키텍처 결정, PRD, 런북을 검색할 때
- 정책 유효성 검증과 시맨틱 린트로 문서 표준을 적용할 때

**주요 기능:**
- 하이브리드 검색 — BM25 + 벡터 유사도 및 Reciprocal Rank Fusion
- 하나의 문서 저장소, 모든 에이전트 — Claude Code, Cursor, Gemini CLI, Codex 등 5개 이상 지원
- 프록시 모드 백그라운드 서버 — 새 세션의 콜드 스타트 지연 제거
- 시맨틱 린트 — 깨진 링크, 고아 파일, 오래된 마커, 날짜 관련 클레임 검사
- macOS launchd 통합 — enable/disable/start/stop/restart 라이프사이클 커맨드

→ [소스 및 문서](https://github.com/epicsagas/alcove)

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

### obscura

**Headless Browser as MCP Tools**

Gives AI agents direct access to the web via five MCP tools. Auto-installs required binaries on first load.

**Key features:**
- Zero config — plugin auto-installs all required binaries
- `obscura_scrape` with configurable concurrency via `obscura-worker`
- `obscura_serve` exposes a CDP WebSocket server for Playwright/Puppeteer
- Stealth mode for anti-detection

→ [Source & Docs](https://github.com/epicsagas/obscura-plugin)

---

## 기여하기

플러그인을 제출하거나 개선을 제안하려면:

1. 이 레포지토리를 포크합니다
2. `.claude-plugin/marketplace.json`에 플러그인 정보를 추가합니다
3. Pull Request를 제출합니다

플러그인은 독립적인 GitHub 레포지토리로 관리되며, 마켓플레이스는 메타데이터만 포함합니다.

---

## 라이선스

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
