# epicsagas 插件

> 专为 AI 辅助开发精心打造的插件 — 自主代理、上下文压缩，以及不会干扰您工作流的工具。

[![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)](../LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green?style=flat)](https://github.com/epicsagas/claude-plugins)
[![Plugins](https://img.shields.io/badge/Plugins-5-blueviolet?style=flat)](https://github.com/epicsagas/claude-plugins)
[![GitHub Stars](https://img.shields.io/github/stars/epicsagas/claude-plugins?style=flat)](https://github.com/epicsagas/claude-plugins/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/epicsaga)

**翻译：** [English](../README.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [繁體中文](README.zh-tw.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## 插件列表

| 插件 | 描述 | 源码 |
|------|------|------|
| [epic-harness](#epic-harness) | 自主代理框架 — 6 个强力命令、自我进化的技能，以及每个会话自动运行的隐形钩子 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | 令牌优化文档阅读器 — 静默压缩 `.md`、`.html`、`.txt` 文件，上下文用量最多减少 40% | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCP文档服务器 — BM25+向量混合搜索、lint检查、项目文档的launchd生命周期管理 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AI原生出版系统 — 从创意到EPUB/PDF的自主多阶段工作流。像开发软件一样写书。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | 无头浏览器作为MCP工具 — fetch、scrape、提取Markdown、JS求值。零配置，自动安装二进制文件。 | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | 软件工程知识图谱 — 设计模式、代码坏味道、重构和架构分析，结合AI驱动的代码审查。 | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |

---

## 安装

### 通过 Claude Code（推荐）

添加市场后安装插件：

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

所有插件立即可用 — 无需额外配置。

### epic-harness — 独立安装

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall**（预构建二进制）：
```bash
cargo binstall epic-harness
```

**Cargo**（从源码构建）：
```bash
cargo install epic-harness
```

### llm-transpile — 独立安装

**cargo-binstall**（预构建二进制）：
```bash
cargo binstall llm-transpile
```

**Cargo**（从源码构建）：
```bash
cargo install llm-transpile
```

### alcove — 独立安装

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall**（预构建二进制）：
```bash
cargo binstall alcove
```

**Cargo**（从源码构建）：
```bash
cargo install alcove
```

### episteme — 独立安装

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/episteme
```

**cargo-binstall**（预构建二进制）：
```bash
cargo binstall episteme
```

**Cargo**（从源码构建）：
```bash
cargo install episteme
```

---

## 插件详情

### epic-harness

**自主代理框架**

构建能够独立处理复杂多步任务的代理工作流。内置 6 个强力命令，技能随使用而自我进化。会话钩子自动运行，守护代码、优化输出并反思每次会话。

**适用场景：**
- 自动化重复性代码审查、提交和测试周期
- 定义项目专属的自定义工作流
- 跨 Claude 会话执行一致的行为模式

**核心功能：**
- 6 个内置强力命令（commit、review、test、deploy 等）
- 自我进化技能系统 — 从使用模式中学习并持续改进
- 会话守护钩子 — 自动防止错误并维持质量

→ [源码与文档](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**令牌优化文档阅读器**

每次调用 Read 工具时自动压缩 `.md`、`.html`、`.txt` 文件，将上下文令牌用量最多减少 40%。无需修改工作流，立即生效。

**适用场景：**
- 频繁引用大型文档或规格说明的项目
- 经常触及上下文窗口限制时
- 希望降低长会话中的令牌成本

**核心功能：**
- 静默压缩 — 输出不变，令牌最多减少 40%
- 自动检测 `.md` / `.html` / `.txt` 格式
- 与现有 Read 工具工作流完全兼容

→ [源码与文档](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCP文档服务器**

通过 MCP 为 AI 编码代理提供对项目私有文档的按需访问。BM25+向量混合搜索、语义 lint 检查、文档验证，以及支持代理模式的后台 HTTP 服务器实现即时响应。

**适用场景：**
- 跨多个 AI 代理管理私有项目文档
- 从任何 MCP 兼容代理搜索架构决策、PRD 和运行手册
- 通过策略验证和语义 lint 检查执行文档标准

**核心功能：**
- 混合搜索 — BM25 + 向量相似度与 Reciprocal Rank Fusion
- 一个文档仓库，任意代理 — Claude Code、Cursor、Gemini CLI、Codex 等 5 种以上
- 代理模式后台服务器 — 消除新会话的冷启动延迟
- 语义 lint 检查 — 失效链接、孤立文件、过时标记、日期声明检查
- macOS launchd 集成 — enable/disable/start/stop/restart 生命周期命令

→ [源码与文档](https://github.com/epicsagas/alcove)

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

**软件工程知识图谱**

可查询的设计模式、代码坏味道、重构和架构法则知识图谱。AI驱动的代码分析检测质量问题，提出改进建议，并将每条建议建立在成熟的工程原则之上。

**适用场景：**
- 审查代码中的设计模式误用、代码坏味道或架构违规
- 基于原则的权衡分析来选择重构策略
- 学习和应用软件工程法则（康威定律、阿姆达尔定律、盖尔定律）

**核心功能：**
- 支持模式、坏味道、重构和法则之间图谱遍历的知识图谱
- 坏味道检测和分级重构建议的AI代码分析
- 多种智能体角色 — 代码审查员、架构分析师、工程顾问

→ [源码与文档](https://github.com/epicsagas/Episteme)

---

## 贡献

提交插件或建议改进：

1. Fork 本仓库
2. 在 `.claude-plugin/marketplace.json` 中添加插件信息
3. 提交 Pull Request

插件以独立 GitHub 仓库形式维护，市场仅包含元数据。

---

## 许可证

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
