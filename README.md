# Rakuten API MCP

楽天のAPIを介して楽天市場や楽天ブックスの情報を検索する MCP サーバーです。

## 機能

- 楽天市場の商品検索: キーワードによる商品情報の取得 (名称、価格、URL等)
- 楽天ブックスの検索: 書籍タイトルによる情報の取得 (タイトル、著者、価格等)

## インストール

```bash
uv venv
uv sync
```

## 使い方

Claude Desktop などの MCP クライアントの設定に以下を追加してください：

```json
{
  "mcpServers": {
    "rakuten-api": {
      "command": "python",
      "args": ["[リポジトリのパス]/src/main.py"],
      "env": {
        "RAKUTEN_APPLICATION_ID": "あなたのアプリID",
        "RAKUTEN_ACCESS_KEY": "あなたのアクセスキー"
      }
    }
  }
}
```

## 構成

- `src/main.py`: MCP サーバーのエントリーポイント、ツールの定義
- `src/rakuten_api/client.py`: 楽天APIとの通信を行うクライアント
- `src/rakuten_api/models.py`: Pydantic モデルによるデータ定義
