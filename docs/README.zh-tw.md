# epicsagas 插件

> 專為 AI 輔助開發精心打造的插件 — 自主代理、上下文壓縮，以及不會干擾您工作流程的工具。

[![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)](../LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green?style=flat)](https://github.com/epicsagas/claude-plugins)
[![Plugins](https://img.shields.io/badge/Plugins-5-blueviolet?style=flat)](https://github.com/epicsagas/claude-plugins)
[![GitHub Stars](https://img.shields.io/github/stars/epicsagas/claude-plugins?style=flat)](https://github.com/epicsagas/claude-plugins/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/epicsaga)

**翻譯：** [English](../README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [简体中文](README.zh-cn.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## 插件列表

| 插件 | 描述 | 原始碼 |
|------|------|--------|
| [epic](#epic) | 自主代理框架 — 6 個強力指令、自我進化的技能，以及每個工作階段自動執行的隱形鉤子 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [transpile](#transpile) | 令牌最佳化文件閱讀器 — 靜默壓縮 `.md`、`.html`、`.txt` 檔案，上下文用量最多減少 40% | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP文件伺服器 — BM25+向量混合搜尋、lint檢查、專案文件的launchd生命週期管理 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI原生出版系統 — 從構思到EPUB/PDF的自主多階段工作流程。像開發軟體一樣寫書。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura](#obscura) | 無頭瀏覽器作為MCP工具 — fetch、scrape、提取Markdown、JS求值。零配置，自動安裝二進位檔。 | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |

---

## 安裝

### 透過 Claude Code（推薦）

新增市場後安裝插件：

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

所有插件立即可用 — 無需額外設定。

### epic — 獨立安裝

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall**（預建置二進位）：
```bash
cargo binstall epic-harness
```

**Cargo**（從原始碼建置）：
```bash
cargo install epic-harness
```

### transpile — 獨立安裝

**cargo-binstall**（預建置二進位）：
```bash
cargo binstall llm-transpile
```

**Cargo**（從原始碼建置）：
```bash
cargo install llm-transpile
```

### alcove — 獨立安裝

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall**（預建置二進位）：
```bash
cargo binstall alcove
```

**Cargo**（從原始碼建置）：
```bash
cargo install alcove
```

---

## 插件詳情

### epic

**自主代理框架**

建構能夠獨立處理複雜多步驟任務的代理工作流程。內建 6 個強力指令，技能隨使用而自我進化。工作階段鉤子自動執行，守護程式碼、最佳化輸出並反思每次工作階段。

**適用場景：**
- 自動化重複性程式碼審查、提交和測試週期
- 定義專案專屬的自訂工作流程
- 跨 Claude 工作階段執行一致的行為模式

**核心功能：**
- 6 個內建強力指令（commit、review、test、deploy 等）
- 自我進化技能系統 — 從使用模式中學習並持續改進
- 工作階段守護鉤子 — 自動防止錯誤並維持品質

→ [原始碼與文件](https://github.com/epicsagas/epic-harness)

---

### transpile

**令牌最佳化文件閱讀器**

每次呼叫 Read 工具時自動壓縮 `.md`、`.html`、`.txt` 檔案，將上下文令牌用量最多減少 40%。無需修改工作流程，立即生效。

**適用場景：**
- 頻繁參照大型文件或規格說明的專案
- 經常觸及上下文視窗限制時
- 希望降低長工作階段中的令牌成本

**核心功能：**
- 靜默壓縮 — 輸出不變，令牌最多減少 40%
- 自動偵測 `.md` / `.html` / `.txt` 格式
- 與現有 Read 工具工作流程完全相容

→ [原始碼與文件](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP文件伺服器**

透過 MCP 為 AI 編碼代理提供對專案私有文件的隨選存取。BM25+向量混合搜尋、語義 lint 檢查、文件驗證，以及支援代理模式的背景 HTTP 伺服器實現即時回應。

**適用場景：**
- 跨多個 AI 代理管理私有專案文件
- 從任何 MCP 相容代理搜尋架構決策、PRD 和執行手冊
- 透過策略驗證和語義 lint 檢查執行文件標準

**核心功能：**
- 混合搜尋 — BM25 + 向量相似度與 Reciprocal Rank Fusion
- 一個文件儲存庫，任意代理 — Claude Code、Cursor、Gemini CLI、Codex 等 5 種以上
- 代理模式背景伺服器 — 消除新工作階段的冷啟動延遲
- 語義 lint 檢查 — 失效連結、孤立檔案、過時標記、日期聲明檢查
- macOS launchd 整合 — enable/disable/start/stop/restart 生命週期指令

→ [原始碼與文件](https://github.com/epicsagas/alcove)

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

## 貢獻

提交插件或建議改進：

1. Fork 本儲存庫
2. 在 `.claude-plugin/marketplace.json` 中新增插件資訊
3. 提交 Pull Request

插件以獨立 GitHub 儲存庫形式維護，市場僅包含中繼資料。

---

## 授權條款

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
