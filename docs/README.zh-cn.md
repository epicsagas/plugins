# epicsagas 插件集

> 为专业 AI 辅助开发精心打造的插件合集 — 自主 Agent、上下文压缩与零干扰工具链。

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

## 插件列表

| 插件 | 描述 | 来源 |
|------|------|------|
| [epic-harness](#epic-harness) | 自主 Agent 框架 — 8 个核心指令、自我进化技能与全程守护 Hook。 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | Token 优化文档读取器 — 自动压缩 `.md`、`.html`、`.txt`，减少高达 40% 上下文消耗。 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP 文档服务器 — BM25 + 向量混合检索、Lint 校验与 launchd 生命周期管理。 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI 原生出版系统 — 从构思到 EPUB/PDF 的全流程多阶段工作流。像构建软件一样写书。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | 无头浏览器 MCP 工具 — fetch、scrape、Markdown 提取与 JS 执行。零配置自动安装。 | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | 软件工程知识图谱 — 设计模式、代码坏味道、重构法则与 AI 代码审查。 | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian 知识库管理 — AI 收件箱分类、知识图谱强化、MOC 重建与多库同步。 | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 个人 Agent 技能集 — 问题发现（5 Whys, JTBD）、认知反思与开源发布评估。 | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | 学术研究助手 — arXiv/Semantic Scholar/PDF 论文索引、知识缺口分析与文献报告生成。 | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — 通过结构化访谈抽取隐性知识，编译并进化个性化 Agent 框架。 | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | 自主多引擎开发通道 — 在隔离 Git Worktree 中实现三级自动故障转移（Claudy ➔ Codex ➔ AGYD）。 | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## 安装指南

### Claude Code (推荐)

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

## 插件详情

### kanban-dev-lane

**面向 Hermes 看板的自主多引擎实现通道**

将 Hermes Kanban Worker 的代码实现与重构任务委托给隔离的 Git 工作树，并在外部模型提供商遇到额度耗尽（429 / Quota Exhausted）时自动执行**三级故障转移**（`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`）。

**核心特性:**
- 自动检测 429 与额度耗尽，无缝切换引擎
- 隔离 Git Worktree 全生命周期管理
- Hermes Worker 保持严格的代码审查、Diff 验证与测试复核
- 内置运行脚本: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## 许可证

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
