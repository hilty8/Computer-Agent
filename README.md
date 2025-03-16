# Computer-Agent (Forked Version)

このリポジトリは[オリジナルのComputer-Agent](https://github.com/Computer-Agent/Computer-Agent)のフォークです。
オリジナルの機能に加えて、以下の拡張機能を実装しています。

## 追加機能

1. 入力モード専用アプリケーション
- `text_app.py`: テキスト入力に特化
- `voice_app.py`: 音声入力に特化

2. プロンプトファイルのサポート
- `prompts`ディレクトリでプロンプトを管理
- ファイルからプロンプトを読み込んで実行可能

## アーキテクチャ
（以下、[オリジナルのドキュメント](docs/README.md)より引用）

以下の図は、異なるエージェント間の高レベルな相互作用を示しています：

![アーキテクチャ図](docs/diagram.svg)

### プロジェクトコンポーネント

システムは以下のエージェントで構成されており、それぞれが専門的な役割を持っています：

1. **System Agent**  
   GUIベースのタスク（ファイルを開く、ウィンドウを操作する、デスクトップ要素と対話するなど）を処理します。現在はWindowsのみサポートされています。

2. **Web Search Agent**  
   オンラインリソースを使用してデータを収集またはタスクを解決するために、Webブラウジングを自動化します。

3. **Terminal Agent**  
   高度な操作のためのターミナルコマンドを実行します。

4. **Memory Agent**  
   意思決定を改善し、冗長な操作を避けるために、過去のアクションを保存および呼び出します。

### ワークフロー

1. **Memory Agent**（または各エージェント固有のメモリ）がタスク解決に使用された方法とステップを保存します。
2. 新しいクエリを受信すると、システムは過去の保存されたアクションをチェックして、同様の解決策を複製または適応します。
3. システムは必要に応じて**System**、**Web Search**、**Terminal Agent**を統合して、人間のアプローチを模倣してタスクを解決します。

## セットアップ

1. リポジトリのクローン
```bash
git clone https://github.com/hilty8/Computer-Agent.git
cd Computer-Agent
```

2. 環境変数の設定
`.env`ファイルをプロジェクトルートに作成し、以下の環境変数を設定：
```
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

## 使用方法

### テキスト入力モード
```bash
# 対話モード
python text_app.py

# ファイル入力モード（プロンプトファイルから実行）
python text_app.py prompts/example.txt
```

### 音声入力モード
```bash
python voice_app.py
```
※ Enterキーを押すまで録音を続けます

## リポジトリ管理

### リモートリポジトリの設定
```bash
# originを自分のフォークに設定
git remote set-url origin https://github.com/hilty8/Computer-Agent.git

# upstreamとして元のリポジトリを追加
git remote add upstream https://github.com/Computer-Agent/Computer-Agent.git
```

### 開発フロー
```bash
# 自分の変更をプッシュ
git push origin main

# 元リポジトリの更新を取り込む
git fetch upstream
git merge upstream/main
```

## オリジナルのドキュメント

オリジナルの完全なドキュメントは[docs/README.md](docs/README.md)を参照してください。
このフォークバージョンでは、オリジナルの機能をすべて継承しつつ、上記の拡張機能を追加しています。

## ライセンス

このプロジェクトは、オリジナルのライセンスに従います。詳細は[docs/LICENSE](docs/LICENSE)を参照してください。