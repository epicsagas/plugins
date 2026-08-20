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

| 플러그인 | 설명 | 소스 |
|--------|------|------|
| [epic-harness](#epic-harness) | 자율 에이전트 하니스 — 8개의 파워 커맨드, 자가 진화 스킬, 매 세션을 보호하고 성찰하는 보이지 않는 훅. | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | 토큰 최적화 문서 리더 — `.md`, `.html`, `.txt` 파일을 자동 압축해 컨텍스트 사용량을 최대 40% 절감. | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP 문서 서버 — BM25+벡터 하이브리드 검색, 린트, 프로젝트 문서를 위한 launchd 라이프사이클 관리. | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI 네이티브 퍼블리싱 시스템 — 아이디에이션부터 EPUB/PDF까지 자율 멀티페이즈 워크플로우. 소프트웨어처럼 책을 제작. | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | 헤드리스 브라우저 MCP 도구 — fetch, scrape, 마크다운 추출, JS eval. 무설정, 첫 로드 시 바이너리 자동 설치. | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | 소프트웨어 엔지니어링 지식 그래프 — 디자인 패턴, 코드 스멜, 리팩토링 및 아키텍처 원칙과 AI 기반 코드 리뷰. | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | 옵시디언 볼트 라이프사이클 관리 — AI 인박스 분류, 지식 그래프 강화, MOC 재생성, 다중 볼트 동기화 스킬. | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 개인 에이전트 스킬 컬렉션 — 문제 발견(5 Whys, JTBD, Fishbone), 인지 자기 분석, 오픈소스 출시 준비성 검사. | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | 학술 연구 어시스턴트 — arXiv/Semantic Scholar/PDF 논문 수집, LLM 갭 분석 및 리포트 작성 (`research serve`). | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — 인터뷰를 통해 암묵지와 목표를 수집하고 맞춤형 AI 에이전트 하니스를 컴파일/진화. | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | 자율 멀티 엔진 구현 레인 — 격리된 Git 워크트리에서 자동 폴백(Claudy ➔ Codex ➔ AGYD)으로 코딩 위임. | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |
| [site-harvester](#site-harvester) | 로그인 필요 콘텐츠 수집기 — 사이트의 숨은 JSON API를 찾아 본인 구독 토큰으로, 사람 속도로 전부 프라이빗 로컬 볼트에 수집. | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) |

---

## 설치 가이드

### Claude Code (권장)

마켓플레이스를 등록한 후 필요한 플러그인을 설치합니다:

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
claude plugin install site-harvester@epicsagas
```

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

모든 플러그인을 즉시 사용할 수 있습니다.

### Hermes Agent

한 번의 명령으로 전체 epiccounty 스위트(6개 플러그인, 24개 도구)를 설치합니다:

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
hermes plugins enable obscura
hermes plugins enable kanban-dev-lane
```

**사전 요구사항:** 각 플러그인은 Rust CLI 바이너리를 래핑합니다:

```bash
brew install epicsagas/tap/alcove          # alcove 플러그인
brew install epicsagas/tap/episteme        # episteme 플러그인 (`epis serve` 실행 필요)
brew install epicsagas/tap/epic-harness    # epic-harness 플러그인
brew install epicsagas/tap/llm-transpile   # llm-transpile 플러그인
brew install epicsagas/tap/obsidian-forge  # obsidian-forge 플러그인
brew install epicsagas/tap/obscura         # obscura 플러그인
```

**원클릭 전체 설치:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## 단독 설치 (Standalone)

### epic
```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # 사전 빌드 바이너리
cargo install epic-harness    # 소스 빌드
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

### obscura
```bash
brew install epicsagas/tap/obscura-plugin
cargo binstall obscura-plugin
cargo install obscura-plugin
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

### research
```bash
brew install epicsagas/tap/research-agent
cargo binstall research-agent
cargo install research-agent
```

### byoh
```bash
brew install epicsagas/tap/byoh
cargo binstall byoh
cargo install byoh
```

---

## 플러그인 상세 안내

### epic-harness

**자율 에이전트 하니스**

복잡한 다단계 작업을 독립적으로 처리하는 에이전트 워크플로우를 구축합니다. 8개의 내장 파워 커맨드와 자율 `/orbit` 파이프라인으로 구동되며, 사용할수록 스킬이 진화합니다. 세션 훅이 자동으로 작동하여 코드를 보호하고 출력을 다듬으며 세션을 성찰합니다.

**사용 시점:**
- 반복적인 코드 리뷰, 커밋, 테스트 주기 자동화
- 프로젝트별 맞춤형 워크플로우 정의
- Claude 세션 전반에서 일관된 행동 규칙 적용

**주요 기능:**
- `/orbit`을 포함한 8개의 내장 파워 커맨드
- 자가 진화 스킬 시스템 — 사용 패턴을 학습하여 지속적 개선
- 세션 가드 훅 — 실수 방지 및 품질 자동 유지

→ [Source & Docs](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**토큰 최적화 문서 리더**

Read 도구 호출 시 `.md`, `.html`, `.txt` 파일을 자동으로 압축하여 컨텍스트 토큰 사용량을 최대 40% 절감합니다. 워크플로우 변경 없이 즉시 적용됩니다.

**사용 시점:**
- 대규모 문서나 사양서를 자주 참조하는 프로젝트
- 컨텍스트 윈도우 한계에 자주 부딪힐 때
- 장시간 세션에서 토큰 비용 절감

**주요 기능:**
- 무음 압축 — 동일한 정보 전달, 최대 40% 토큰 절약
- `.md` / `.html` / `.txt` 형식 자동 감지
- 기존 Read 도구 워크플로우 완벽 호환

→ [Source & Docs](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP 문서 서버**

MCP를 통해 AI 코딩 에이전트에게 비공개 프로젝트 문서에 대한 즉각적인 접근 권한을 제공합니다. BM25+벡터 하이브리드 검색, 시맨틱 린트, 문서 유효성 검사, 백그라운드 프록시 서버를 지원합니다.

**사용 시점:**
- 여러 AI 에이전트 간 비공개 프로젝트 문서 공유
- MCP 호환 에이전트에서 아키텍처 결정(ADR), PRD, 런북 검색
- 정책 검증 및 시맨틱 린트로 문서 품질 표준 유지

**주요 기능:**
- 하이브리드 검색 — Reciprocal Rank Fusion 기반 BM25 + 벡터 유사도
- 단일 문서 저장소, 모든 에이전트 지원 — Claude Code, Cursor, Gemini CLI, Codex 등
- 프록시 모드 백그라운드 서버 — 콜드 스타트 지연 제거
- 시맨틱 린트 — 깨진 링크, 고립 파일, 오래된 주장 자동 탐지
- macOS launchd 연동 — 라이프사이클 관리

→ [Source & Docs](https://github.com/epicsagas/alcove)

---

### velith

**AI 네이티브 퍼블리싱 시스템**

소프트웨어 개발 방식으로 책을 집필합니다. 백지 상태에서 출판 가능한 EPUB/PDF까지 자율 멀티페이즈 워크플로우를 제공하며, 7개의 특화 에이전트가 구조, 초안, 일관성, 스타일, 표지 디자인, 마케팅을 전담합니다.

**사용 시점:**
- 구조화된 긴 글 작성 (소설, 논픽션, 기술서, 학술 논문)
- 전체 도서에 걸친 챕터 간 일관성 및 문체 유지
- EPUB, PDF, MOBI, Markdown 출력

**주요 기능:**
- 6단계 파이프라인: 온보딩 ➔ 아이디에이션 ➔ 아웃라인 ➔ 집필 ➔ 교정 ➔ 출판
- 7개 장르 템플릿 (소설, 비문학, 기술서, 각본, 시, 게임 시나리오, 학술)
- AI 상투어(slop) 감지 기능을 갖춘 5단계 교정 파이프라인
- Pandoc + Calibre 기반 멀티 포맷 출력

→ [Source & Docs](https://github.com/epicsagas/Velith)

---

### obscura-plugin

**헤드리스 브라우저 MCP 도구**

fetch, scrape, serve, screenshot, extract_markdown의 5개 MCP 도구를 통해 AI 에이전트에게 웹 접근 권한을 부여합니다. 첫 로드 시 바이너리가 자동 설치되므로 별도 설정이 필요 없습니다.

**사용 시점:**
- 웹페이지 조회, 데이터 스크래핑, JS 실행이 필요한 에이전트
- 병렬 스크래핑을 통한 대량 URL 처리
- Playwright/Puppeteer를 위한 CDP WebSocket 엔드포인트 제공

**주요 기능:**
- 무설정 자동 설치
- `obscura-worker`를 통한 동시성 제어 스크래핑
- Playwright/Puppeteer용 CDP WebSocket 서버 제공
- 봇 감지 방지 및 트래커 차단 스텔스 모드

→ [Source & Docs](https://github.com/epicsagas/obscura-plugin)

---

### episteme

**소프트웨어 엔지니어링 지식 그래프**

디자인 패턴, 코드 스멜, 리팩토링, 아키텍처 원칙을 질의할 수 있는 지식 그래프입니다. AI 코드 분석을 통해 품질 이슈를 감지하고 검증된 공학 원칙에 기반한 개선안을 제시합니다.

**사용 시점:**
- 디자인 패턴 오용, 코드 스멜, 아키텍처 위반 검토
- 트레이드오프 분석을 기반으로 리팩토링 전략 선택
- 소프트웨어 공학 법칙(콘웨이, 암달, 갈의 법칙) 학습 및 적용

**주요 기능:**
- 패턴, 스멜, 리팩토링, 법칙 간 그래프 탐색
- 스멜 감지 및 우선순위 리팩토링 제안
- 코드 리뷰어, 아키텍처 분석가 등 다중 에이전트 페르소나

→ [Source & Docs](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**옵시디언 볼트 라이프사이클 관리**

AI 에이전트가 옵시디언 볼트 작업을 스킬로 실행할 수 있도록 합니다. PARA 기반 AI 인박스 분류, 지식 그래프 강화(백링크, 브릿지 노트, 자동 태그), MOC 재생성, 태그/링크 복구, 완전한 동기화 주기를 지원합니다.

**사용 시점:**
- AI 세션에서 옵시디언 볼트(Second Brain, Zettelkasten, PARA) 관리
- AI 자동 분류 및 라우팅을 통한 인박스 정리
- 프로젝트와 개념 간 지식 그래프 연결 강화

**주요 기능:**
- 5대 에이전트 스킬: vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- 프론트매터 주입 및 PARA 라우팅 인박스 분류
- 전/후 메트릭 보고를 통한 지식 그래프 강화
- 다중 볼트 및 백그라운드 데몬(macOS) 지원

→ [Source & Docs](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**개인 에이전트 스킬 컬렉션**

개인 및 팀을 위한 선별된 에이전트 스킬 모음입니다. 문제 발견, 인지적 자기 분석, 오픈소스 릴리스 준비성을 평가합니다. 바이너리 없이 마크다운에서 직접 로드됩니다.

**사용 시점:**
- 개발 전 진짜 문제 정의 (개인, 팀, 스타트업)
- 대화 기록 분석을 통한 사고 패턴 및 인지 편향 감지
- 커뮤니티, 리드미, 배포, 보안에 걸친 OSS 출시 준비성 감사

**주요 기능:**
- `discover` — 5 Whys, JTBD, Fishbone, 소크라테스식 질문, 가설 매핑
- `cognitive-audit` — 증거 기반 편향 감지 및 10가지 실천 루틴
- `oss-dist` — 커뮤니티 표준, 문서, 출시 전략, 보안 감사

→ [Source & Docs](https://github.com/epicsagas/epicsagas)

---

### research

**학술 연구 어시스턴트**

arXiv, Semantic Scholar, 로컬 PDF 논문을 인덱싱하고 지식 공백을 식별하며 문헌 리포트를 작성하는 장기 연구 메모리입니다. MCP 도구(`research serve`)를 통해 에이전트가 주도적으로 논문을 수집하고 분석합니다.

**사용 시점:**
- 특정 주제의 추천 읽기 목록 또는 문헌 검토 구축
- 읽은 논문 추적 및 다음 읽을 논문 식별
- 에이전트에게 논문 수집 및 종합 위임

**주요 기능:**
- 11개 MCP 도구: init, ingest, query_papers, analyze_gaps, generate_report 등
- 적응형 디스패치 — MCP 기본 인터페이스, CLI 폴백
- 로컬 SQLite (FTS5) 인덱스 + LLM 연동

→ [Source & Docs](https://github.com/epicsagas/research-agent)

---

### byoh

**BuildYourOwnHarness**

인터뷰를 통해 맞춤형 AI 에이전트 하니스를 생성합니다. 암묵지, 데이터 소스, 장르, 목표를 수집하여 고유한 하니스를 컴파일, 배포, 진화시킵니다. 3대 안전 게이트(Critic / Seesaw / Stagnation)로 보호됩니다.

**사용 시점:**
- 도메인과 워크플로우에 특화된 커스텀 에이전트 하니스 구축
- A/B 증거와 롤백을 통한 안전한 스킬 진화
- MCP 도구를 통한 프로필 ➔ 컴파일 ➔ 진화 전체 제어

**주요 기능:**
- 14개 MCP 도구 제공
- 에이전트 주도 모드 (`byoh serve`)
- 외부 문서 서버([alcove](https://github.com/epicsagas/alcove)) 연동 지원

→ [Source & Docs](https://github.com/epicsagas/BuildYourOwnHarness)

---

### kanban-dev-lane

**Hermes Kanban 자율 멀티 엔진 구현 레인**

Hermes Kanban 워커의 구현 및 리팩토링 작업을 격리된 Git 워크트리에 위임하며, 외부 공급자의 쿼터/속도 제한 발생 시 자동 **3단계 폴백 체인**(`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`)으로 무중단 개발을 보장합니다.

**주요 기능:**
- 429 및 쿼터 소진 자동 감지 및 무중단 엔진 전환
- 격리된 Git 워크트리 생명주기 관리
- Hermes 워커의 엄격한 칸반 상태 관리, Diff 검증, 테스트 재실행
- 내장 CLI 러너: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

### site-harvester

**로그인 필요 콘텐츠 수집기**

회원제 사이트를 로컬 재개 가능 데이터 파이프라인으로 바꿉니다. SPA의 숨은 JSON API를 리콘하고, 실제 브라우저 로그인 한 번으로 본인 OAuth 토큰을 얻은 뒤, 평범한 API 호출로 전부 수집합니다 — 사람 속도(30–120초), 크래시 후에도 이어서, 신규 콘텐츠는 cron으로. 법률 가드레일이 내장되어 있습니다.

**주요 기능:**
- 사이트 JS 번들에서 숨은 API 리콘 — 수집 중 페이지 로드 없음
- 아이템 단위 재개 상태, flock 중복 실행 방지, 수집 기간 만료 자동 종료
- 설계부터 가드레일: 약관 확인 게이트, 속도 하한, 차단 시 정지, 공개 리포 커밋 거부 — CAPTCHA 우회·안티봇 회피·IP 로테이션·결제벽 우회 없음
- 원본 API JSON을 커밋된 원천 데이터로, 노트와 localhost 전용 사이트는 여기서 파생

→ [Source & Docs](https://github.com/epicsagas/site-harvester)

---

## 기여하기

1. 본 저장소를 Fork합니다.
2. `.claude-plugin/marketplace.json` 및 `.agents/plugins/marketplace.json`에 플러그인 항목을 추가합니다.
3. Pull Request를 생성합니다.

---

## 라이선스

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
