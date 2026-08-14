# epicsagas プラグイン

> AI駆動の本格開発のための高品質プラグイン集 — 自律エージェント、コンテキスト圧縮、邪魔にならないツール群。

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

## プラグイン一覧

| プラグイン | 説明 | ソース |
|-----------|------|--------|
| [epic-harness](#epic-harness) | 自律エージェントハーネス — 8つのコマンド、自己進化スキル、各セッションを守護するフック。 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | トークン最適化ドキュメントリーダー — `.md`, `.html`, `.txt` を自動圧縮し、コンテキスト使用量を最大40%削減。 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCPドキュメントサーバー — BM25+ベクトルハイブリッド検索、リント、launchdライフサイクル管理。 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AIネイティブ出版システム — アイデア出しからEPUB/PDFまで自律マルチフェーズワークフロー。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [obscura-plugin](#obscura-plugin) | ヘッドレスブラウザMCPツール — fetch、scrape、Markdown抽出、JS実行。設定不要で自動インストール。 | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) |
| [episteme](#episteme) | ソフトウェアエンジニアリング知識グラフ — デザインパターン、コードスメル、リファクタリング、AIコードレビュー。 | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidian Vaultライフサイクル管理 — AI受信トレイ分類、ナレッジグラフ強化、MOC再生成、Vault同期。 | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 個人エージェントスキル集 — 問題発見（5 Whys, JTBD）、自己認知分析、OSS公開準備性チェック。 | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |
| [research](#research) | 学術研究アシスタント — arXiv/Semantic Scholar/PDF論文の収集、ギャップ分析、レポート生成。 | [epicsagas/research-agent](https://github.com/epicsagas/research-agent) |
| [byoh](#byoh) | BuildYourOwnHarness — 対話形式で暗黙知と目標を抽出し、専用AIエージェントハーネスを構築・進化。 | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) |
| [kanban-dev-lane](#kanban-dev-lane) | 自律マルチエンジン開発レーン — 隔離Git Worktreeで自動フォールバック（Claudy ➔ Codex ➔ AGYD）委譲。 | [epicsagas/plugins/.hermes/kanban-dev-lane](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane) |

---

## インストール

### Claude Code（推奨）

マーケットプレイスを追加し、必要なプラグインをインストールします：

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

### Codex CLI

```bash
codex plugin marketplace add epicsagas/plugins
```

### Hermes Agent

```bash
hermes plugins install epicsagas/plugins --enable
```

または個別プラグインの有効化：

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

---

## プラグイン詳細

### kanban-dev-lane

**Hermes Kanban 向け自律マルチエンジン実装レーン**

Hermes Kanbanワーカーの実装・リファクタリング作業を隔離されたGitワークツリーに委譲し、外部プロバイダーのクォータ枯渇やレート制限（429）発生時に自動**3段階フォールバック**（`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`）を実行します。

**主な特徴:**
- 429・クォータ枯渇の自動検知とシームレスなエンジン切り替え
- 隔離Git Worktreeのライフサイクル管理
- Hermesワーカーによる厳格なレビュー、Diff検証、テスト再実行
- 同梱ランナー: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [Source & Docs](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## ライセンス

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
