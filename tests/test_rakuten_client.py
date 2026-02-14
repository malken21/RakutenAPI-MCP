from unittest.mock import patch, MagicMock
import pytest
from rakuten_api.client import RakutenClient

@pytest.mark.asyncio
async def test_ichiba_search_params():
    client = RakutenClient(application_id="test_id", access_key="test_access_key")
    
    mock_response = MagicMock()
    mock_response.json.return_value = {"Items": []}
    mock_response.raise_for_status = MagicMock()

    with patch("httpx.AsyncClient.get", return_value=mock_response) as mock_get:
        await client.search_ichiba_item(keyword="test")
        
        # パラメータが正しく渡されているか確認
        args, kwargs = mock_get.call_args
        params = kwargs.get("params")
        assert params["applicationId"] == "test_id"
        assert params["elements"] == "test_access_key"
        assert params["keyword"] == "test"
        assert params["format"] == "json"

@pytest.mark.asyncio
async def test_books_search_params():
    client = RakutenClient(application_id="test_id", access_key="test_access_key")
    
    mock_response = MagicMock()
    mock_response.json.return_value = {"Items": []}
    mock_response.raise_for_status = MagicMock()

    with patch("httpx.AsyncClient.get", return_value=mock_response) as mock_get:
        await client.search_books(title="test_book")
        
        args, kwargs = mock_get.call_args
        params = kwargs.get("params")
        assert params["applicationId"] == "test_id"
        assert params["elements"] == "test_access_key"
        assert params["title"] == "test_book"
