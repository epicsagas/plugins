# epicsagas 外掛

> 為嚴肅的 AI 輔助開發精心打造的外掛 — 自主智能體、上下文壓縮,以及不礙事的工具。

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

## 外掛列表

本中心只承載 epiccounty 核心產品線。其餘外掛在各自儲存庫中攜帶與外掛同名的獨立市集,分開管理 (參見 [已個別化的外掛](#已個別化的外掛))。

| 外掛 | 說明 | 來源 |
|--------|------|------|
| [epic-harness](#epic-harness) | 自主智能體框架 — 8 個強力命令、自我進化技能,以及守護、打磨、復盤每次工作階段的無形鉤子。 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Token 最佳化文件讀取器 — 讀取時靜默壓縮 `.md`、`.html`、`.txt` 檔案,上下文用量最多減少 40%。 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP 文件伺服器 — BM25+向量混合檢索、lint,以及專案文件的 launchd 生命週期管理。 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI 原生出版系統 — 從構想到 EPUB/PDF 的自主多階段工作流。像做軟體一樣做書。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | 軟體工程知識圖譜 — 設計模式、程式碼壞味道、重構與架構法則,搭配 AI 程式碼審查。 | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian 庫生命週期管理 — AI 收件匣分類、圖譜強化、MOC 再生、多庫同步技能。 | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 個人智能體技能集 — 問題發現(5 Whys、JTBD、Fishbone)、認知自我分析、OSS 發布就緒檢查。 | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## 安裝

### Claude Code (建議)

註冊一次市集,然後安裝任意外掛:

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

所有外掛立即可用。

### Hermes Agent

一條命令安裝整個 epiccounty 套件 — 6 個外掛、32 個工具:

```bash
hermes plugins install epicsagas/plugins --enable
```

或單獨安裝並啟用:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` 為 Hermes 專用 — 打包在本儲存庫 `.hermes/` 中,不發布到 Claude/Codex 市集。

**前置需求:** 每個外掛包裝一個 Rust CLI 二進位檔。按需安裝:

```bash
brew install epicsagas/tap/alcove          # alcove 外掛
brew install epicsagas/tap/episteme        # episteme 外掛 (還需執行 `epis serve`)
brew install epicsagas/tap/epic-harness    # epic-harness 外掛
brew install epicsagas/tap/llm-transpile   # llm-transpile 外掛
brew install epicsagas/tap/obsidian-forge  # obsidian-forge 外掛
```

**快速開始 — 一次全部安裝:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## 獨立安裝

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # 預編譯二進位檔
cargo install epic-harness    # 從原始碼建置
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

## 已個別化的外掛

這些外掛已移出中心。每個儲存庫都攜帶與外掛自身同名的市集,可獨立安裝:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| 外掛 | 儲存庫 | 說明 |
|--------|------------|------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | 無頭瀏覽器 MCP 工具 — 擷取、爬取、抽取 markdown、JS eval。 |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | 透過訪談編譯並進化個人化的 AI 智能體框架。 |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | 多宿主外掛管理器 — 腳手架、體檢、安裝驗證、發布。 |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | 把 GeekMagic SmallTV 變成即時智能體狀態顯示器。 |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | 登入牆內容收割器 — 隱藏 API 偵察、擬人節奏採集。 |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Upbit 幣種投資分析 — 多空辯論管線加風險閘門。 |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | KRX 股票投資分析 — 融入資金流向/放空證據與 KRX 規則的多空辯論架構,基於 Toss 證券 Open API。 |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | AI/科技活動情報 — 9 來源確定性聚合器。 |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | 用本地 LLM 離線批改 TOEFL iBT 全部 4 個部分。 |

---

## 外掛詳情

### epic-harness

**自主智能體框架**

建構獨立處理複雜多步任務的智能體工作流。由 8 個內建強力命令與自主 `/orbit` 管線驅動。技能越用越進化。工作階段鉤子自動守護程式碼、打磨輸出並復盤每次工作階段。

**適用場景:**
- 自動化重複的程式碼審查、提交、測試循環
- 定義專案級自訂工作流
- 在 Claude 工作階段之間強制一致的行為模式

**主要特性:**
- 8 個內建強力命令,包含 `/orbit`(完全自主管線)
- 自我進化技能系統 — 從使用模式中學習並持續改進
- 工作階段守護鉤子 — 防止失誤並自動維持品質

→ [原始碼與文件](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**Token 最佳化文件讀取器**

在每次 Read 工具呼叫時自動壓縮 `.md`、`.html`、`.txt` 檔案,上下文 Token 用量最多減少 40%。無需改變工作流,即刻生效。

**適用場景:**
- 經常引用大型文件或規格說明的專案
- 經常觸及上下文視窗上限
- 降低長工作階段的 Token 成本

**主要特性:**
- 靜默壓縮 — 輸出不變,Token 最多省 40%
- 自動偵測 `.md` / `.html` / `.txt` 格式
- 與現有 Read 工具工作流完全相容

→ [原始碼與文件](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP 文件伺服器**

透過 MCP 讓 AI 編碼智能體按需存取你的私有專案文件。BM25+向量混合檢索、語意 lint、文件校驗,以及代理模式的背景 HTTP 伺服器,實現即時回應。

**適用場景:**
- 跨多個 AI 智能體管理私有專案文件
- 從任何 MCP 相容智能體檢索架構決策、PRD、維運手冊
- 用策略校驗與語意 lint 強制文件標準

**主要特性:**
- 混合檢索 — BM25 + 向量相似度,Reciprocal Rank Fusion
- 一份文件儲存庫,任意智能體 — Claude Code、Cursor、Gemini CLI、Codex 等 5 種以上
- 代理模式背景伺服器 — 消除新工作階段冷啟動延遲
- 語意 lint — 失效連結、孤兒檔案、過期標記、過時日期聲明
- macOS launchd 整合 — enable/disable/start/stop/restart 生命週期命令

→ [原始碼與文件](https://github.com/epicsagas/alcove)

---

### velith

**AI 原生出版系統**

像做軟體一樣做書。從白紙到可出版 EPUB/PDF 的自主多階段工作流。7 個專職智能體負責結構、起草、連續性、風格、封面設計與行銷。

**適用場景:**
- 撰寫結構化長篇內容(小說、非虛構、技術、學術)
- 在整本書中維持跨章節一致性與文風
- 出版到 EPUB、PDF、MOBI 或 Markdown

**主要特性:**
- 6 階段管線:入門 → 構想 → 大綱 → 起草 → 編輯 → 出版
- 7 種體裁模板(小說、非虛構、技術、劇本、詩、遊戲、學術)
- 带 AI 垃圾文風偵測的 5 段編輯管線
- 透過 Pandoc + Calibre 輸出 EPUB、PDF、MOBI、TXT、Markdown

→ [原始碼與文件](https://github.com/epicsagas/Velith)

---

### episteme

**軟體工程知識圖譜**

可查詢的設計模式、程式碼壞味道、重構與架構法則知識圖譜。AI 程式碼分析偵測品質問題、提出改進建議,每條建議都錨定在成熟的工程原則之上。

**適用場景:**
- 審查設計模式誤用、程式碼壞味道或架構違規
- 以原則性權衡分析選擇重構策略
- 學習並應用軟體工程法則(Conway、Amdahl、Gall)

**主要特性:**
- 跨模式、壞味道、重構、法則的圖譜遍歷
- 含壞味道偵測與排序重構建議的 AI 程式碼分析
- 多種智能體角色 — 程式碼審查者、架構分析師、工程顧問

→ [原始碼與文件](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Obsidian 庫生命週期管理**

讓 AI 智能體以技能驅動的方式操作 Obsidian 庫 — PARA 路由的 AI 收件匣分類、知識圖譜強化(反向連結、橋接筆記、自動標籤)、MOC 再生、標籤/連結/frontmatter 修復,以及完整同步循環。單一 Rust 二進位檔,多庫,零設定起步。

**適用場景:**
- 在 AI 智能體工作階段中管理 Obsidian 庫(第二大腦、卡片盒、PARA)
- 用 AI 分類與自動路由處理收件匣筆記
- 強化專案與概念間的知識圖譜連結

**主要特性:**
- 5 個智能體技能 — vault-health、vault-sync、graph-strengthen、inbox-process、vault-fix
- 带 frontmatter 注入與 PARA 路由的 AI 收件匣分類
- 帶前後指標報告的知識圖譜強化
- 支援共享設定與背景常駐程式(macOS)的多庫管理

→ [原始碼與文件](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**個人智能體技能**

為個人與團隊精選的智能體技能集 — 問題發現、認知自我分析、OSS 發布就緒。無需二進位檔,技能直接從 markdown 檔案載入。

**適用場景:**
- 在動手建構之前發現並定義真正的問題(個人、團隊、新創)
- 從對話歷史分析自己的思維模式與認知偏誤
- 稽核 OSS 專案在社群、README、散布、安全上的發布就緒度

**主要特性:**
- `discover` — 5 Whys、JTBD、Fishbone、蘇格拉底式提問、假設映射
- `cognitive-audit` — 基於證據的偏誤偵測、決策分析、10 條可執行例程
- `oss-dist` — 完整發布生命週期:社群標準、README、上線策略、i18n、安全

→ [原始碼與文件](https://github.com/epicsagas/epicsagas)

---

### kanban-dev-lane

**Hermes Kanban 的自主多引擎實作通道**

把 Hermes Kanban worker 中範圍受限的實作與重構任務委派到隔離的 git worktree,搭配自動 **3 級故障轉移鏈** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`),即使外部供應商配額/限流也能持續推進。

**主要特性:**
- 自動偵測 429 與配額耗盡,零停機故障轉移
- 隔離的 git worktree 生命週期管理
- Hermes 嚴格持有 Kanban 狀態、diff 調節與回歸測試
- 內建 CLI 執行器: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [原始碼與文件](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## 貢獻

提交外掛或建議改進:

1. Fork 本儲存庫
2. 在 `.claude-plugin/marketplace.json` 與 `.agents/plugins/marketplace.json` 中加入外掛條目
3. 發起 Pull Request

外掛以獨立 GitHub 儲存庫維護。本市集只包含詮釋資料。

---

## 授權條款

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
