# epicsagas 플러그인

> AI 기반 전문 개발을 위한 고품질 플러그인 모음 — 자율 에이전트, 컨텍스트 압축, 방해 없이 작동하는 도구들.

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

## 플러그인 목록

이 허브는 epiccounty 코어 라인업만 담습니다. 나머지는 각자의 레포지토리에 플러그인과 동일한 이름의 독립 마켓플레이스를 두고 분리 관리됩니다 ([개별화된 플러그인](#개별화된-플러그인) 참고).

| 플러그인 | 설명 | 소스 |
|--------|------|------|
| [epic-harness](#epic-harness) | 자율 에이전트 하니스 — 8개의 파워 커맨드, 자가 진화 스킬, 매 세션을 보호하고 성찰하는 보이지 않는 훅. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | 토큰 최적화 문서 리더 — `.md`, `.html`, `.txt` 파일을 자동 압축해 컨텍스트 사용량을 최대 40% 절감. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP 문서 서버 — BM25+벡터 하이브리드 검색, 린트, 프로젝트 문서를 위한 launchd 라이프사이클 관리. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI 네이티브 퍼블리싱 시스템 — 아이디에이션부터 EPUB/PDF까지 자율 멀티페이즈 워크플로우. 소프트웨어처럼 책을 제작. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | 소프트웨어 엔지니어링 지식 그래프 — 디자인 패턴, 코드 스멜, 리팩토링 및 아키텍처 원칙과 AI 기반 코드 리뷰. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | 옵시디언 볼트 라이프사이클 관리 — AI 인박스 분류, 지식 그래프 강화, MOC 재생성, 다중 볼트 동기화 스킬. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 개인 에이전트 스킬 컬렉션 — 문제 발견(5 Whys, JTBD, Fishbone), 인지 자기 분석, 오픈소스 출시 준비성 검사. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## 설치 가이드

### Claude Code (권장)

마켓플레이스를 등록한 후 필요한 플러그인을 설치합니다:

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

모든 플러그인을 즉시 사용할 수 있습니다.

### Hermes Agent

한 번의 명령으로 epiccounty 스위트(6개 플러그인, 32개 도구)를 설치합니다:

```bash
hermes plugins install epicsagas/plugins --enable
```

또는 개별 플러그인 설치 및 활성화:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane`은 Hermes 전용 — 이 레포 `.hermes/`에 번들되며 Claude/Codex 마켓플레이스에는 등록되지 않는다.

**사전 요구사항:** 각 플러그인은 Rust CLI 바이너리를 래핑합니다. 필요한 것만 설치하세요:

```bash
brew install epicsagas/tap/alcove          # alcove 플러그인
brew install epicsagas/tap/episteme        # episteme 플러그인 (`epis serve` 실행 필요)
brew install epicsagas/tap/epic-harness    # epic-harness 플러그인
brew install epicsagas/tap/llm-transpile   # llm-transpile 플러그인
brew install epicsagas/tap/obsidian-forge  # obsidian-forge 플러그인
```

**빠른 시작 — 한 번에 전부 설치:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## 단독 설치

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # 사전 빌드 바이너리
cargo install epic-harness    # 소스에서 빌드
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

## 개별화된 플러그인

허브에서 분리된 플러그인입니다. 각 레포지토리는 플러그인 자체와 동일한 이름의 마켓플레이스를 포함하고 있어 단독 설치가 가능합니다:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| 플러그인 | 레포지토리 | 설명 |
|--------|------------|------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | 헤드리스 브라우저 MCP 도구 — fetch, scrape, 마크다운 추출, JS eval. |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | 인터뷰로 맞춤형 AI 에이전트 하니스를 컴파일하고 진화. |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | 멀티 호스트 플러그인 관리자 — 스캐폴드, 닥터, 설치 검증, 퍼블리시. |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | GeekMagic SmallTV를 라이브 에이전트 상태 디스플레이로. |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | 로그인 필요 콘텐츠 수집기 — 숨은 API 정찰, 사람 속도 수집. |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | 업비트 코인 투자 분석가 — 불/베어 토론 파이프라인과 리스크 게이트. |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | KRX 주식 투자 분석가 — 투자자금/공매도 증거와 KRX 규칙을 반영한 불/베어 토론 구조, 토스증권 Open API 기반. |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | AI/테크 행사 인텔리전스 — 9개 소스 결정론적 수집기. |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | 로컬 LLM으로 TOEFL iBT 4개 섹션 오프라인 채점. |

---

## 플러그인 상세

### epic-harness

**자율 에이전트 하니스**

복잡한 다단계 작업을 독립적으로 처리하는 에이전트 워크플로우를 구축합니다. 8개 내장 파워 커맨드와 자율 `/orbit` 파이프라인 기반. 스킬은 사용할수록 진화하며, 세션 훅이 코드를 보호하고 결과를 다듬고 세션을 성찰합니다.

**활용 시점:**
- 반복적인 코드 리뷰, 커밋, 테스트 사이클 자동화
- 프로젝트별 커스텀 워크플로우 정의
- Claude 세션 전반의 일관된 동작 패턴 강제

**주요 기능:**
- `/orbit`(완전 자율 파이프라인) 포함 8개 파워 커맨드
- 자가 진화 스킬 시스템 — 사용 패턴에서 학습하며 지속 개선
- 세션 가드 훅 — 실수를 방지하고 품질을 자동 유지

→ [소스 & 문서](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**토큰 최적화 문서 리더**

Read 도구 호출 시 `.md`, `.html`, `.txt` 파일을 자동 압축해 컨텍스트 토큰 사용량을 최대 40% 절감합니다. 워크플로우 변경 없이 즉시 적용됩니다.

**활용 시점:**
- 대형 문서나 스펙을 자주 참조하는 프로젝트
- 컨텍스트 윈도우 한도에 자주 걸리는 경우
- 긴 세션의 토큰 비용 절감

**주요 기능:**
- 무음 압축 — 동일한 출력, 최대 40% 적은 토큰
- `.md` / `.html` / `.txt` 형식 자동 감지
- 기존 Read 도구 워크플로우와 완전 호환

→ [소스 & 문서](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP 문서 서버**

MCP를 통해 AI 코딩 에이전트에게 프라이빗 프로젝트 문서에 대한 온디맨드 접근을 제공합니다. BM25+벡터 하이브리드 검색, 시맨틱 린트, 문서 검증, 즉시 응답을 위한 프록시 모드 백그라운드 HTTP 서버.

**활용 시점:**
- 여러 AI 에이전트에 걸친 프라이빗 프로젝트 문서 관리
- 아키텍처 결정, PRD, 런북을 MCP 호환 에이전트에서 검색
- 정책 검증과 시맨틱 린트로 문서 표준 강제

**주요 기능:**
- 하이브리드 검색 — BM25 + 벡터 유사도, Reciprocal Rank Fusion
- 하나의 문서 레포, 모든 에이전트 — Claude Code, Cursor, Gemini CLI, Codex 등 5종 이상
- 프록시 모드 백그라운드 서버 — 신규 세션 콜드스타트 지연 제거
- 시맨틱 린트 — 깨진 링크, 고아 파일, 스테일 마커, 만료된 날짜 표기
- macOS launchd 통합 — enable/disable/start/stop/restart 라이프사이클 명령

→ [소스 & 문서](https://github.com/epicsagas/alcove)

---

### velith

**AI 네이티브 퍼블리싱 시스템**

소프트웨어처럼 책을 제작하세요. 백지에서 출판 가능한 EPUB/PDF까지 자율 멀티페이즈 워크플로우. 7개 전문 에이전트가 구조, 드래프팅, 연속성, 스타일, 표지 디자인, 마케팅을 담당합니다.

**활용 시점:**
- 구조화된 장문 콘텐츠 집필 (소설, 논픽션, 기술, 학술)
- 책 전체의 챕터 간 일관성과 문체 유지
- EPUB, PDF, MOBI, Markdown 출판

**주요 기능:**
- 6단계 파이프라인: 온보딩 → 아이디에이션 → 아웃라인 → 드래프팅 → 에디팅 → 퍼블리싱
- 7개 장르 템플릿 (소설, 논픽션, 기술, 시나리오, 시, 게임, 학술)
- AI-slop 탐지를 포함한 5단계 에디팅 파이프라인
- Pandoc + Calibre를 통한 EPUB, PDF, MOBI, TXT, Markdown 출력

→ [소스 & 문서](https://github.com/epicsagas/Velith)

---

### episteme

**소프트웨어 엔지니어링 지식 그래프**

디자인 패턴, 코드 스멜, 리팩토링, 아키텍처 법칙의 쿼리 가능한 지식 그래프. AI 기반 코드 분석이 품질 이슈를 탐지하고 개선안을 제안하며, 모든 권고를 확립된 엔지니어링 원칙에 근거합니다.

**활용 시점:**
- 디자인 패턴 오용, 코드 스멜, 아키텍처 위반 코드 리뷰
- 원칙 기반 트레이드오프 분석으로 리팩토링 전략 선택
- 소프트웨어 엔지니어링 법칙(Conway, Amdahl, Gall) 학습과 적용

**주요 기능:**
- 패턴, 스멜, 리팩토링, 법칙을 관통하는 그래프 순회 지식 그래프
- 스멜 탐지와 랭킹된 리팩토링 제안을 포함한 AI 코드 분석
- 다중 에이전트 페르소나 — 코드 리뷰어, 아키텍처 애널리스트, 엔지니어링 어드바이저

→ [소스 & 문서](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**옵시디언 볼트 라이프사이클 관리**

AI 에이전트에게 스킬 기반 옵시디언 볼트 조작을 제공 — PARA 라우팅을 통한 AI 인박스 분류, 지식 그래프 강화(백링크, 브리지 노트, 자동 태그), MOC 재생성, 태그/링크/프론트매터 수리, 전체 동기화 사이클. 단일 Rust 바이너리, 다중 볼트, 무설정 시작.

**활용 시점:**
- AI 에이전트 세션에서 옵시디언 볼트(세컨드 브레인, 젤텔카스텐, PARA) 관리
- AI 분류와 자동 라우팅으로 인박스 노트 처리
- 프로젝트와 개념 간 지식 그래프 연결 강화

**주요 기능:**
- 5개 에이전트 스킬 — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- 프론트매터 주입과 PARA 라우팅을 통한 AI 인박스 분류
- 전/후 메트릭 리포트를 포함한 지식 그래프 강화
- 공유 설정과 백그라운드 데몬(macOS)을 지원하는 다중 볼트

→ [소스 & 문서](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**개인 에이전트 스킬**

개인 및 팀 사용을 위한 엄선된 에이전트 스킬 모음 — 문제 발견, 인지 자기 분석, 오픈소스 출시 준비성. 바이너리 불필요, 마크다운 파일에서 직접 로드.

**활용 시점:**
- 빌드 전에 진짜 문제를 발견하고 정의하기 (개인, 팀, 스타트업)
- 대화 이력에서 자신의 사고 패턴과 인지 편향 분석
- 커뮤니티, README, 배포, 보안에 걸친 오픈소스 출시 준비성 감사

**주요 기능:**
- `discover` — 5 Whys, JTBD, Fishbone, 소크라테스식 질문, 가정 매핑
- `cognitive-audit` — 근거 기반 편향 탐지, 의사결정 분석, 실행 가능한 루틴 10종
- `oss-dist` — 커뮤니티 표준, README, 런칭 전략, i18n, 보안을 포함한 전체 출시 라이프사이클

→ [소스 & 문서](https://github.com/epicsagas/epicsagas)

---


## 기여하기

플러그인을 제출하거나 개선을 제안하려면:

1. 이 레포지토리를 포크합니다
2. `.claude-plugin/marketplace.json`과 `.agents/plugins/marketplace.json`에 플러그인 엔트리를 추가합니다
3. Pull Request를 엽니다

플러그인은 독립적인 GitHub 레포지토리로 유지보수됩니다. 이 마켓플레이스는 메타데이터만 담습니다.

---

## 라이선스

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
