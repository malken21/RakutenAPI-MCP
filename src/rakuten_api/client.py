import httpx
from typing import Dict, Any, Optional
from .models import IchibaSearchResponse

class RakutenClient:
    BASE_URL = "https://app.rakuten.co.jp/services/api"

    def __init__(self, application_id: str, access_key: str):
        self.application_id = application_id
        self.access_key = access_key

    async def _get(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        params["applicationId"] = self.application_id
        params["elements"] = self.access_key
        params["format"] = "json"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}{endpoint}", params=params)
            response.raise_for_status()
            return response.json()

    async def search_ichiba_item(self, keyword: str, hits: int = 10, **kwargs) -> Dict[str, Any]:
        """
        楽天市場の商品検索APIを呼び出す（version:2022-06-01相当の最新URLを使用）
        """
        params = {
            "keyword": keyword,
            "hits": hits,
            **kwargs
        }
        return await self._get("/IchibaItem/Search/20220601", params)

    async def search_books(self, title: str, hits: int = 10, **kwargs) -> Dict[str, Any]:
        """
        楽天ブックスの書籍検索APIを呼び出す
        """
        params = {
            "title": title,
            "hits": hits,
            **kwargs
        }
        return await self._get("/BooksBook/Search/20170404", params)
