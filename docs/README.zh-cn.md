# epicsagas 插件

> 为严肃的 AI 辅助开发精心打造的插件 — 自主智能体、上下文压缩,以及不碍事的工具。

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

本中心只承载 epiccounty 核心产品线。其余插件在各自仓库中携带与插件同名的独立市场,单独管理 (参见 [已单独分发的插件](#已单独分发的插件))。

| 插件 | 说明 | 来源 |
|--------|------|------|
| [epic-harness](#epic-harness) | 自主智能体框架 — 8 个强力命令、自我进化技能,以及守护、打磨、复盘每次会话的无形钩子。 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | 令牌优化文档读取器 — 读取时静默压缩 `.md`、`.html`、`.txt` 文件,上下文用量最多减少 40%。 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP 文档服务器 — BM25+向量混合检索、lint,以及项目文档的 launchd 生命周期管理。 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI 原生出版系统 — 从构思到 EPUB/PDF 的自主多阶段工作流。像做软件一样做书。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | 软件工程知识图谱 — 设计模式、代码坏味道、重构与架构法则,配合 AI 代码审查。 | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian 库生命周期管理 — AI 收件箱分类、图谱强化、MOC 再生、多库同步技能。 | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 个人智能体技能集 — 问题发现(5 Whys、JTBD、Fishbone)、认知自我分析、OSS 发布就绪检查。 | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## 安装

### Claude Code (推荐)

注册一次市场,然后安装任意插件:

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

所有插件立即可用。

### Hermes Agent

一条命令安装整个 epiccounty 套件 — 6 个插件、32 个工具:

```bash
hermes plugins install epicsagas/plugins --enable
```

或单独安装并启用:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` 为 Hermes 专用 — 打包在本仓库 `.hermes/` 中,不发布到 Claude/Codex 市场。

**前置要求:** 每个插件包装一个 Rust CLI 二进制。按需安装:

```bash
brew install epicsagas/tap/alcove          # alcove 插件
brew install epicsagas/tap/episteme        # episteme 插件 (还需运行 `epis serve`)
brew install epicsagas/tap/epic-harness    # epic-harness 插件
brew install epicsagas/tap/llm-transpile   # llm-transpile 插件
brew install epicsagas/tap/obsidian-forge  # obsidian-forge 插件
```

**快速开始 — 一次性全部安装:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## 独立安装

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # 预编译二进制
cargo install epic-harness    # 从源码构建
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

## 已单独分发的插件

这些插件已移出中心。每个仓库都携带与插件自身同名的市场,可独立安装:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| 插件 | 仓库 | 说明 |
|--------|------------|------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | 无头浏览器 MCP 工具 — 抓取、爬取、提取 markdown、JS eval。 |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | 通过访谈编译并进化个性化的 AI 智能体框架。 |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | 多宿主插件管理器 — 脚手架、体检、安装校验、发布。 |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | 把 GeekMagic SmallTV 变成实时智能体状态显示器。 |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | 登录墙内容收割器 — 隐藏 API 侦察、拟人节奏采集。 |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Upbit 币种投资分析 — 多空辩论流水线加风险闸门。 |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | KRX 股票投资分析 — 融入资金流向/做空证据与 KRX 规则的多空辩论架构,基于 Toss 证券 Open API。 |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | AI/科技活动情报 — 9 源确定性聚合器。 |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | 用本地 LLM 离线批改 TOEFL iBT 全部 4 个部分。 |

---

## 插件详情

### epic-harness

**自主智能体框架**

构建独立处理复杂多步任务的智能体工作流。由 8 个内置强力命令和自主 `/orbit` 流水线驱动。技能越用越进化。会话钩子自动守护代码、打磨输出并复盘每次会话。

**适用场景:**
- 自动化重复的代码审查、提交、测试循环
- 定义项目级自定义工作流
- 在 Claude 会话间强制一致的行为模式

**主要特性:**
- 8 个内置强力命令,包括 `/orbit`(完全自主流水线)
- 自我进化技能系统 — 从使用模式中学习并持续改进
- 会话守护钩子 — 防止失误并自动维持质量

→ [源码与文档](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**令牌优化文档读取器**

在每次 Read 工具调用时自动压缩 `.md`、`.html`、`.txt` 文件,上下文令牌用量最多减少 40%。无需改变工作流,即时生效。

**适用场景:**
- 频繁引用大型文档或规格说明的项目
- 经常触及上下文窗口上限
- 降低长会话的令牌成本

**主要特性:**
- 静默压缩 — 输出不变,令牌最多省 40%
- 自动识别 `.md` / `.html` / `.txt` 格式
- 与现有 Read 工具工作流完全兼容

→ [源码与文档](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP 文档服务器**

通过 MCP 让 AI 编码智能体按需访问你的私有项目文档。BM25+向量混合检索、语义 lint、文档校验,以及代理模式的后台 HTTP 服务器,实现即时响应。

**适用场景:**
- 跨多个 AI 智能体管理私有项目文档
- 从任何 MCP 兼容智能体检索架构决策、PRD、运维手册
- 用策略校验和语义 lint 强制文档标准

**主要特性:**
- 混合检索 — BM25 + 向量相似度,Reciprocal Rank Fusion
- 一份文档仓库,任意智能体 — Claude Code、Cursor、Gemini CLI、Codex 等 5 种以上
- 代理模式后台服务器 — 消除新会话冷启动延迟
- 语义 lint — 失效链接、孤儿文件、过期标记、过时日期声明
- macOS launchd 集成 — enable/disable/start/stop/restart 生命周期命令

→ [源码与文档](https://github.com/epicsagas/alcove)

---

### velith

**AI 原生出版系统**

像做软件一样做书。从白纸到可出版 EPUB/PDF 的自主多阶段工作流。7 个专职智能体负责结构、起草、连续性、风格、封面设计和营销。

**适用场景:**
- 写结构化长篇内容(小说、非虚构、技术、学术)
- 在整本书中保持跨章节一致性与文风
- 出版到 EPUB、PDF、MOBI 或 Markdown

**主要特性:**
- 6 阶段流水线:入门 → 构思 → 大纲 → 起草 → 编辑 → 出版
- 7 种体裁模板(小说、非虚构、技术、剧本、诗歌、游戏、学术)
- 带 AI 垃圾文风检测的 5 段编辑流水线
- 通过 Pandoc + Calibre 输出 EPUB、PDF、MOBI、TXT、Markdown

→ [源码与文档](https://github.com/epicsagas/Velith)

---

### episteme

**软件工程知识图谱**

可查询的设计模式、代码坏味道、重构与架构法则知识图谱。AI 代码分析检测质量问题、提出改进建议,每条建议都锚定在成熟的工程原则之上。

**适用场景:**
- 审查设计模式误用、代码坏味道或架构违规
- 以原则性权衡分析选择重构策略
- 学习并应用软件工程法则(Conway、Amdahl、Gall)

**主要特性:**
- 跨模式、坏味道、重构、法则的图谱遍历
- 含坏味道检测与排序重构建议的 AI 代码分析
- 多种智能体角色 — 代码审查者、架构分析师、工程顾问

→ [源码与文档](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Obsidian 库生命周期管理**

让 AI 智能体以技能驱动的方式操作 Obsidian 库 — PARA 路由的 AI 收件箱分类、知识图谱强化(反向链接、桥梁笔记、自动标签)、MOC 再生、标签/链接/frontmatter 修复,以及完整同步周期。单个 Rust 二进制,多库,零配置起步。

**适用场景:**
- 在 AI 智能体会话中管理 Obsidian 库(第二大脑、卡片盒、PARA)
- 用 AI 分类与自动路由处理收件箱笔记
- 强化项目与概念间的知识图谱连接

**主要特性:**
- 5 个智能体技能 — vault-health、vault-sync、graph-strengthen、inbox-process、vault-fix
- 带 frontmatter 注入与 PARA 路由的 AI 收件箱分类
- 带前后指标报告的知识图谱强化
- 支持共享设置与后台守护进程(macOS)的多库管理

→ [源码与文档](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**个人智能体技能**

为个人与团队精选的智能体技能集 — 问题发现、认知自我分析、OSS 发布就绪。无需二进制,技能直接从 markdown 文件加载。

**适用场景:**
- 在动手构建之前发现并定义真正的问题(个人、团队、创业公司)
- 从对话历史分析自己的思维模式与认知偏差
- 审计 OSS 项目在社区、README、分发、安全上的发布就绪度

**主要特性:**
- `discover` — 5 Whys、JTBD、Fishbone、苏格拉底式提问、假设映射
- `cognitive-audit` — 基于证据的偏差检测、决策分析、10 条可执行例程
- `oss-dist` — 完整发布生命周期:社区标准、README、上线策略、i18n、安全

→ [源码与文档](https://github.com/epicsagas/epicsagas)

---

### kanban-dev-lane

**Hermes Kanban 的自主多引擎实现通道**

把 Hermes Kanban worker 中范围受限的实现与重构任务委托到隔离的 git worktree,配合自动 **3 级故障转移链** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`),即使外部供应商配额/限流也能持续推进。

**主要特性:**
- 自动检测 429 与配额耗尽,零停机故障转移
- 隔离的 git worktree 生命周期管理
- Hermes 严格持有 Kanban 状态、diff 调节与回归测试
- 内置 CLI 运行器: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [源码与文档](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## 贡献

提交插件或建议改进:

1. Fork 本仓库
2. 在 `.claude-plugin/marketplace.json` 和 `.agents/plugins/marketplace.json` 中添加插件条目
3. 发起 Pull Request

插件以独立 GitHub 仓库维护。本市场只包含元数据。

---

## 许可证

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
