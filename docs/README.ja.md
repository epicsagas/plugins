# epicsagas プラグイン

> 本格的なAI支援開発のための手作りプラグイン — 自律エージェント、コンテキスト圧縮、邪魔にならないツール群。

[![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)](../LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green?style=flat)](https://github.com/epicsagas/claude-plugins)
[![Plugins](https://img.shields.io/badge/Plugins-5-blueviolet?style=flat)](https://github.com/epicsagas/claude-plugins)
[![GitHub Stars](https://img.shields.io/github/stars/epicsagas/claude-plugins?style=flat)](https://github.com/epicsagas/claude-plugins/stargazers)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/epicsaga)

**翻訳:** [English](../README.md) · [한국어](README.ko.md) · [简体中文](README.zh-cn.md) · [繁體中文](README.zh-tw.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

---

## プラグイン一覧

| プラグイン | 説明 | ソース |
|-----------|------|--------|
| [epic](#epic) | 自律エージェントハーネス — 6つのパワーコマンド、自己進化スキル、毎セッション動作する不可視フック | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [transpile](#transpile) | トークン最適化ドキュメントリーダー — `.md`、`.html`、`.txt`ファイルを自動圧縮し、コンテキスト使用量を最大40%削減 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCPドキュメントサーバー — BM25+ベクトルハイブリッド検索、リント、プロジェクトドキュメント向けlaunchd管理 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AIネイティブ出版システム — アイデア出しからEPUB/PDFまで自律マルチフェーズワークフロー。ソフトウェアのように本を作ります。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura](#obscura) | ヘッドレスブラウザをMCPツールとして — fetch、scrape、Markdown抽出、JS eval。設定不要、バイナリ自動インストール。 | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |

---

## インストール

### Claude Code を使う（推奨）

マーケットプレイスを追加してからプラグインをインストール:

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

すべてのプラグインがすぐに利用可能 — 追加設定不要。

### epic — スタンドアロンインストール

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/epic-harness
```

**cargo-binstall** (ビルド済みバイナリ):
```bash
cargo binstall epic-harness
```

**Cargo** (ソースからビルド):
```bash
cargo install epic-harness
```

### transpile — スタンドアロンインストール

**cargo-binstall** (ビルド済みバイナリ):
```bash
cargo binstall llm-transpile
```

**Cargo** (ソースからビルド):
```bash
cargo install llm-transpile
```

### alcove — スタンドアロンインストール

**Homebrew** (macOS):
```bash
brew install epicsagas/tap/alcove
```

**cargo-binstall** (ビルド済みバイナリ):
```bash
cargo binstall alcove
```

**Cargo** (ソースからビルド):
```bash
cargo install alcove
```

---

## プラグイン詳細

### epic

**自律エージェントハーネス**

複雑なマルチステップタスクを独立して処理するエージェントワークフローを構築します。6つの組み込みパワーコマンドを備え、スキルは使用するほど自己進化します。セッションフックが自動実行され、コードを保護し、出力を洗練し、各セッションを振り返ります。

**使用場面:**
- コードレビュー、コミット、テストサイクルの繰り返し自動化
- プロジェクト固有のカスタムワークフロー定義
- Claudeセッション全体での一貫した動作パターンの適用

**主な機能:**
- 6つの組み込みパワーコマンド（commit、review、test、deployなど）
- 自己進化スキルシステム — 使用パターンを学習して継続的に改善
- セッションガードフック — ミスを防ぎ品質を自動維持

→ [ソース & ドキュメント](https://github.com/epicsagas/epic-harness)

---

### transpile

**トークン最適化ドキュメントリーダー**

Readツール呼び出し時に`.md`、`.html`、`.txt`ファイルを自動圧縮し、コンテキストトークン使用量を最大40%削減します。ワークフローの変更なしに即効果が現れます。

**使用場面:**
- 大規模ドキュメントや仕様書を頻繁に参照するプロジェクト
- コンテキストウィンドウの上限に頻繁に達する場合
- 長いセッションでのトークンコスト削減

**主な機能:**
- サイレント圧縮 — 同じ出力、最大40%少ないトークン
- `.md` / `.html` / `.txt`フォーマットの自動検出
- 既存のReadツールワークフローと完全互換

→ [ソース & ドキュメント](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCPドキュメントサーバー**

AIコーディングエージェントにMCPを通じてプライベートプロジェクトドキュメントへのオンデマンドアクセスを提供します。BM25+ベクトルハイブリッド検索、セマンティックリント、ドキュメント検証、プロキシモード対応のバックグラウンドHTTPサーバーで即座に応答します。

**使用場面:**
- 複数のAIエージェント間でプライベートプロジェクトドキュメントを管理する場合
- MCP対応エージェントからアーキテクチャ決定、PRD、ランブックを検索する場合
- ポリシー検証とセマンティックリントでドキュメント標準を適用する場合

**主な機能:**
- ハイブリッド検索 — BM25 + ベクトル類似度とReciprocal Rank Fusion
- 1つのドキュメントリポジトリ、あらゆるエージェント — Claude Code、Cursor、Gemini CLI、Codex、その他5つ以上に対応
- プロキシモード対応バックグラウンドサーバー — 新しいセッションのコールドスタート遅延を解消
- セマンティックリント — 壊れたリンク、孤立ファイル、古いマーカー、日付関連の主張を検査
- macOS launchd統合 — enable/disable/start/stop/restartライフサイクルコマンド

→ [ソース & ドキュメント](https://github.com/epicsagas/alcove)

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

## コントリビューション

プラグインの提出や改善提案:

1. このリポジトリをフォーク
2. `.claude-plugin/marketplace.json`にプラグイン情報を追加
3. Pull Requestを作成

プラグインは独立したGitHubリポジトリで管理され、マーケットプレイスはメタデータのみを含みます。

---

## ライセンス

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
