# epicsagas プラグイン

> AI支援開発のための厳選プラグイン集 — 自律エージェント、コンテキスト圧縮、邪魔にならないツール群。

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

このハブは epiccounty コアラインナップのみを扱います。その他は各リポジトリにプラグインと同名の独立マーケットプレイスを置いて分離管理されます ([個別化されたプラグイン](#個別化されたプラグイン) 参照)。

| プラグイン | 説明 | ソース |
|--------|------|------|
| [epic-harness](#epic-harness) | 自律エージェントハーネス — 8個のパワーコマンド、自己進化スキル、毎セッションを保護・省察する見えないフック。 | [epicsagas/epic-harness](https://github.com/epicsagas/epic-harness) |
| [llm-transpile](#llm-transpile) | トークン最適化ドキュメントリーダー — `.md`, `.html`, `.txt` を自動圧縮しコンテキスト使用量を最大40%削減。 | [epicsagas/llm-transpile](https://github.com/epicsagas/llm-transpile) |
| [alcove](#alcove) | MCPドキュメントサーバー — BM25+ベクターハイブリッド検索、リント、プロジェクトドキュメントのlaunchdライフサイクル管理。 | [epicsagas/alcove](https://github.com/epicsagas/alcove) |
| [velith](#velith) | AIネイティブ出版システム — アイデア出しからEPUB/PDFまで自律マルチフェーズワークフロー。ソフトウェアのように本を作る。 | [epicsagas/Velith](https://github.com/epicsagas/Velith) |
| [episteme](#episteme) | ソフトウェアエンジニアリングナレッジグラフ — デザインパターン、コードスメル、リファクタリング、アーキテクチャ原則とAIコードレビュー。 | [epicsagas/Episteme](https://github.com/epicsagas/Episteme) |
| [obsidian-forge](#obsidian-forge) | Obsidianボールトライフサイクル管理 — AIインボックス分類、ナレッジグラフ強化、MOC再生成、マルチボールト同期スキル。 | [epicsagas/obsidian-forge](https://github.com/epicsagas/obsidian-forge) |
| [epicsagas](#epicsagas) | 個人エージェントスキルコレクション — 問題発見(5 Whys, JTBD, Fishbone)、認知自己分析、OSS公開準備チェック。 | [epicsagas/epicsagas](https://github.com/epicsagas/epicsagas) |

---

## インストール

### Claude Code (推奨)

マーケットプレイスを登録後、必要なプラグインをインストールします:

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

すべてのプラグインが即時利用可能です。

### Hermes Agent

1コマンドでepiccountyスイート(6プラグイン、32ツール)をインストール:

```bash
hermes plugins install epicsagas/plugins --enable
```

または個別にインストール・有効化:

```bash
hermes plugins install epicsagas/plugins
hermes plugins enable alcove
hermes plugins enable episteme
hermes plugins enable epic-harness
hermes plugins enable llm-transpile
hermes plugins enable obsidian-forge
hermes plugins enable kanban-dev-lane
```

> `kanban-dev-lane` は Hermes 専用 — このリポジトリの `.hermes/` にバンドルされ、Claude/Codex のマーケットプレイスには登録されません。

**前提条件:** 各プラグインはRust CLIバイナリをラップします。必要なものだけインストールしてください:

```bash
brew install epicsagas/tap/alcove          # alcove プラグイン
brew install epicsagas/tap/episteme        # episteme プラグイン (`epis serve` の実行が必要)
brew install epicsagas/tap/epic-harness    # epic-harness プラグイン
brew install epicsagas/tap/llm-transpile   # llm-transpile プラグイン
brew install epicsagas/tap/obsidian-forge  # obsidian-forge プラグイン
```

**クイックスタート — 一括インストール:**

```bash
curl -fsSL https://github.com/epicsagas/epiccounty.com/releases/latest/download/epiccounty-installer.sh | sh
epiccounty install all
```

---

## 単体インストール

### epic

```bash
brew install epicsagas/tap/epic-harness
cargo binstall epic-harness   # ビルド済みバイナリ
cargo install epic-harness    # ソースからビルド
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

## 個別化されたプラグイン

ハブから分離されたプラグインです。各リポジトリはプラグイン自体と同名のマーケットプレイスを同梱しており、単体でインストールできます:

```bash
claude plugin marketplace add epicsagas/<repo>
claude plugin install <plugin>@<plugin>
```

| プラグイン | リポジトリ | 説明 |
|--------|------------|------|
| obscura-plugin | [epicsagas/obscura-plugin](https://github.com/epicsagas/obscura-plugin) | ヘッドレスブラウザMCPツール — fetch, scrape, マークダウン抽出, JS eval。 |
| byoh | [epicsagas/BuildYourOwnHarness](https://github.com/epicsagas/BuildYourOwnHarness) | インタビューからパーソナライズドAIエージェントハーネスをコンパイル・進化。 |
| plugin-forge | [epicsagas/plugin-forge](https://github.com/epicsagas/plugin-forge) | マルチホストプラグインマネージャー — スキャフォールド、ドクター、インストール検証、公開。 |
| agent-glance | [epicsagas/AgentGlance](https://github.com/epicsagas/AgentGlance) | GeekMagic SmallTVをライブエージェント状態ディスプレイに。 |
| site-harvester | [epicsagas/site-harvester](https://github.com/epicsagas/site-harvester) | ログイン必須コンテンツハーベスター — 隠しAPI偵察、人間ペース収集。 |
| upbit-investor | [epicsagas/upbit-invester](https://github.com/epicsagas/upbit-invester) | Upbitコイン投資アナリスト — ブル/ベアディベートパイプラインとリスクゲート。 |
| toss-investor | [epicsagas/toss-invester](https://github.com/epicsagas/toss-invester) | KRX株式投資アナリスト — 投資資金/空売りエビデンスとKRXルールを反映したブル/ベアディベート構造、Toss証券Open API経由。 |
| tech-event-scout | [epicsagas/tech-event-scout](https://github.com/epicsagas/tech-event-scout) | AI/テックイベントインテリジェンス — 9ソース決定論的アグリゲーター。 |
| toefl-prep | [epicsagas/toefl-prep](https://github.com/epicsagas/toefl-prep) | ローカルLLMでTOEFL iBT全4セクションをオフライン採点。 |

---

## プラグイン詳細

### epic-harness

**自律エージェントハーネス**

複雑なマルチステップタスクを自律的に処理するエージェントワークフローを構築します。8個の内蔵パワーコマンドと自律 `/orbit` パイプラインを基盤とし、スキルは使用するほど進化します。セッションフックがコードを保護し、出力を磨き、セッションを省察します。

**活用場面:**
- 反復的なコードレビュー、コミット、テストサイクルの自動化
- プロジェクトごとのカスタムワークフロー定義
- Claudeセッション全体で一貫した動作パターンの強制

**主な機能:**
- `/orbit`(完全自律パイプライン)を含む8個のパワーコマンド
- 自己進化スキルシステム — 使用パターンから学習し継続改善
- セッションガードフック — ミスを防ぎ品質を自動維持

→ [ソース & ドキュメント](https://github.com/epicsagas/epic-harness)

---

### llm-transpile

**トークン最適化ドキュメントリーダー**

Readツール呼び出し時に `.md`, `.html`, `.txt` ファイルを自動圧縮し、コンテキストトークン使用量を最大40%削減します。ワークフロー変更なしで即時適用されます。

**活用場面:**
- 大型ドキュメントやスペックを頻繁に参照するプロジェクト
- コンテキストウィンドウ上限に頻繁に達する場合
- 長時間セッションのトークンコスト削減

**主な機能:**
- サイレント圧縮 — 同じ出力でトークン最大40%減
- `.md` / `.html` / `.txt` フォーマット自動検出
- 既存のReadツールワークフローと完全互換

→ [ソース & ドキュメント](https://github.com/epicsagas/llm-transpile)

---

### alcove

**MCPドキュメントサーバー**

MCPを通じてAIコーディングエージェントにプライベートプロジェクトドキュメントへの編集アクセスを提供します。BM25+ベクターハイブリッド検索、セマンティックリント、ドキュメント検証、即時応答のためのプロキシモード付きバックグラウンドHTTPサーバー。

**活用場面:**
- 複数AIエージェントにまたがるプライベートプロジェクトドキュメント管理
- アーキテクチャ決定、PRD、ランブックをMCP対応エージェントから検索
- ポリシー検証とセマンティックリントによるドキュメント標準の強制

**主な機能:**
- ハイブリッド検索 — BM25 + ベクター類似度、Reciprocal Rank Fusion
- 1つのドキュメントリポジトリ、全エージェント — Claude Code, Cursor, Gemini CLI, Codex など5種以上
- プロキシモード付きバックグラウンドサーバー — 新規セッションのコールドスタート遅延を解消
- セマンティックリント — 壊れたリンク、孤立ファイル、古いマーカー、期限切れの日付表記
- macOS launchd統合 — enable/disable/start/stop/restart ライフサイクルコマンド

→ [ソース & ドキュメント](https://github.com/epicsagas/alcove)

---

### velith

**AIネイティブ出版システム**

ソフトウェアのように本を作りましょう。白紙から出版可能なEPUB/PDFまでの自律マルチフェーズワークフロー。7個の専門エージェントが構造、ドラフト、連続性、スタイル、表紙デザイン、マーケティングを担当します。

**活用場面:**
- 構造化された長編コンテンツの執筆 (小説、ノンフィクション、技術、学術)
- 本全体のチャプター間一貫性と文体の維持
- EPUB, PDF, MOBI, Markdownへの出版

**主な機能:**
- 6フェーズパイプライン: オンボーディング → アイデア出し → アウトライン → ドラフト → 編集 → 出版
- 7ジャンルテンプレート (小説、ノンフィクション、技術、脚本、詩、ゲーム、学術)
- AIスロップ検出を含む5段階編集パイプライン
- Pandoc + CalibreによるEPUB, PDF, MOBI, TXT, Markdown出力

→ [ソース & ドキュメント](https://github.com/epicsagas/Velith)

---

### episteme

**ソフトウェアエンジニアリングナレッジグラフ**

デザインパターン、コードスメル、リファクタリング、アーキテクチャ法則のクエリ可能なナレッジグラフ。AIコード分析が品質問題を検出し改善案を提案、すべての推奨を確立されたエンジニアリング原則に基づ付けます。

**活用場面:**
- デザインパターン誤用、コードスメル、アーキテクチャ違反のコードレビュー
- 原則に基づくトレードオフ分析によるリファクタリング戦略の選択
- ソフトウェアエンジニアリング法則(Conway, Amdahl, Gall)の学習と適用

**主な機能:**
- パターン、スメル、リファクタリング、法則を横断するグラフトラバーサル
- スメル検出とランク付けされたリファクタリング提案を含むAIコード分析
- 複数エージェントペルソナ — コードレビュー担当、アーキテクトアナリスト、エンジニアリングアドバイザー

→ [ソース & ドキュメント](https://github.com/epicsagas/Episteme)

---

### obsidian-forge

**Obsidianボールトライフサイクル管理**

AIエージェントにスキル駆動のObsidianボールト操作を提供 — PARAルーティングによるAIインボックス分類、ナレッジグラフ強化(バックリンク、ブリッジノート、自動タグ)、MOC再生成、タグ/リンク/フロントマター修復、完全同期サイクル。単一Rustバイナリ、マルチボールト、設定なしで開始可能。

**活用場面:**
- AIエージェントセッションからのObsidianボールト(セカンドブレイン、ツェッテルカステン、PARA)管理
- AI分類と自動ルーティングによるインボックスノート処理
- プロジェクトと概念間のナレッジグラフ接続の強化

**主な機能:**
- 5個のエージェントスキル — vault-health, vault-sync, graph-strengthen, inbox-process, vault-fix
- フロントマター注入とPARAルーティングによるAIインボックス分類
- 前後メトリクスレポート付きナレッジグラフ強化
- 共有設定とバックグラウンドデーモン(macOS)を備えたマルチボールト対応

→ [ソース & ドキュメント](https://github.com/epicsagas/obsidian-forge)

---

### epicsagas

**個人エージェントスキル**

個人・チーム利用のための厳選エージェントスキル集 — 問題発見、認知自己分析、OSS公開準備。バイナリ不要、マークダウンファイルから直接ロードします。

**活用場面:**
- 構築前に本当の問題を発見・定義する (個人、チーム、スタートアップ)
- 会話履歴から自分の思考パターンと認知バイアスを分析
- コミュニティ、README、配布、セキュリティにわたるOSS公開準備の監査

**主な機能:**
- `discover` — 5 Whys, JTBD, Fishbone, ソクラテス式質問、仮定マッピング
- `cognitive-audit` — 証拠に基づくバイアス検出、意思決定分析、実行可能な10のルーティン
- `oss-dist` — コミュニティ標準、README、ローンチ戦略、i18n、セキュリティを含む公開ライフサイクル全体

→ [ソース & ドキュメント](https://github.com/epicsagas/epicsagas)

---

### kanban-dev-lane

**Hermes Kanban用自律マルチエンジン実装レーン**

Hermes Kanbanワーカーの境界付けされた実装・リファクタリングタスクを分離されたGitワークツリーに委譲し、自動 **3段階フェイルオーバーチェーン** (`Claudy` ➔ `Codex --yolo` ➔ `AGYD` ➔ `Hermes Direct`) により、外部プロバイダのクォータ/レート制限到達時も進行を継続します。

**主な機能:**
- 429およびクォータ枯渇の自動検出、ダウンタイムゼロのフェイルオーバー
- 分離されたGitワークツリーのライフサイクル管理
- HermesがKanban状態、diff調整、回帰テストの厳格な所有権を維持
- 同梱CLIランナー: `python3 .hermes/kanban-dev-lane/scripts/lane_runner.py`

→ [ソース & ドキュメント](https://github.com/epicsagas/plugins/tree/main/.hermes/kanban-dev-lane)

---

## コントリビュート

プラグインの提出や改善の提案:

1. このリポジトリをフォークします
2. `.claude-plugin/marketplace.json` と `.agents/plugins/marketplace.json` にプラグインエントリを追加します
3. Pull Requestを開きます

プラグインは独立したGitHubリポジトリとして保守されます。このマーケットプレイスはメタデータのみを保持します。

---

## ライセンス

Apache-2.0 © [epicsagas](https://github.com/epicsagas)
