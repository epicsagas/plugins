# epicsagas 外掛集

> 為專業 AI 輔助開發精心打造的外掛合集 — 自主 Agent、上下文壓縮與零干擾工具鏈。

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

| 外掛 | 描述 | 來源 |
|------|------|------|
| [epic-harness](#epic-harness) | 自主 Agent 框架 — 8 個核心指令、自我進化技能與全程守護 Hook。 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Token 最佳化文件讀取器 — 自動壓縮 `.md`、`.html`、`.txt`，減少高達 40% 上下文消耗。 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP 文件伺服器 — BM25 + 向量混合檢索、Lint 檢查與 launchd 生命週期管理。 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI 原生出版系統 — 從構思到 EPUB/PDF 的全流程多階段工作流。像構建軟體一樣寫書。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | 無頭瀏覽器 MCP 工具 — fetch、scrape、Markdown 提取與 JS 執行。零配置自動安裝。 | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | 軟體工程知識圖譜 — 設計模式、程式碼壞味道、重構法則與 AI 程式碼審查。 | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian 知識庫管理 — AI 收件匣分類、知識圖譜強化、MOC 重建與多庫同步。 | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 個人 Agent 技能集 — 問題發現（5 Whys, JTBD）、認知反思與開源發布評估。 | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | 學術研究助手 — arXiv/Semantic Scholar/PDF 論文索引、知識缺口分析與文獻報告生成。 | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — 透過結構化訪談抽取隱性知識，編譯並進化個性化 Agent 框架。 | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | 自主多引擎開發通道 — 在隔離 Git Worktree 中實現三級自動故障轉移（Claudy ➔ Codex ➔ AGYD）。 | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## 安裝指南

### Claude Code (推薦)

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

## 外掛詳情

### kanban-dev-lane

**面向 Hermes 看板的自主多引擎實現通道**

將 Hermes Kanban Worker 的程式碼實現與重構任務委託給隔離的 Git 工作區，並在外部模型提供商遇到額度耗盡（429 / Quota Exhausted）時自動執行**三級故障轉移**（`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`）。

**核心特性:**
- 自動檢測 429 與額度耗盡，無縫切換引擎
- 隔離 Git Worktree 全生命週期管理
- Hermes Worker 保持嚴格的程式碼審查、Diff 驗證與測試複核
- 內建執行腳本: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## 許可證

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
