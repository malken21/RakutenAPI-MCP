import os
import asyncio
from typing import Optional
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from rakuten_api import RakutenClient

# 環境変数の読み込み
load_dotenv()

# MCPサーバーの初期化
mcp = FastMCP("Rakuten-API")

# 楽天APIクライアントの初期化
application_id = os.getenv("RAKUTEN_APPLICATION_ID")
access_key = os.getenv("RAKUTEN_ACCESS_KEY")

if not application_id:
    raise ValueError("RAKUTEN_APPLICATION_ID environment variable is required")
if not access_key:
    raise ValueError("RAKUTEN_ACCESS_KEY environment variable is required")

client = RakutenClient(application_id, access_key)

@mcp.tool()
async def search_ichiba_items(keyword: str, hits: int = 5) -> str:
    """
    楽天市場で商品を検索します。
    
    Args:
        keyword: 検索キーワード
        hits: 取得件数 (最大30)
    """
    try:
        data = await client.search_ichiba_item(keyword=keyword, hits=hits)
        items = data.get("Items", [])
        
        if not items:
            return "該当する商品が見つかりませんでした。"
            
        result = []
        for item_wrapper in items:
            item = item_wrapper.get("Item", {})
            result.append(
                f"商品名: {item.get('itemName')}\n"
                f"価格: {item.get('itemPrice')}円\n"
                f"URL: {item.get('itemUrl')}\n"
                f"店舗: {item.get('shopName')}\n"
                "---"
            )
        return "\n".join(result)
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

@mcp.tool()
async def search_books(title: str, hits: int = 5) -> str:
    """
    楽天ブックスで書籍を検索します。
    
    Args:
        title: 書籍タイトル
        hits: 取得件数 (最大30)
    """
    try:
        data = await client.search_books(title=title, hits=hits)
        items = data.get("Items", [])
        
        if not items:
            return "該当する書籍が見つかりませんでした。"
            
        result = []
        for item_wrapper in items:
            item = item_wrapper.get("Item", {})
            result.append(
                f"タイトル: {item.get('title')}\n"
                f"著者: {item.get('author')}\n"
                f"価格: {item.get('itemPrice')}円\n"
                f"出版社: {item.get('publisherName')}\n"
                f"発売日: {item.get('salesDate')}\n"
                f"URL: {item.get('itemUrl')}\n"
                "---"
            )
        return "\n".join(result)
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

if __name__ == "__main__":
    mcp.run()
