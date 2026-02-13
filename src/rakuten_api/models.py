from typing import List, Optional
from pydantic import BaseModel, Field

class RakutenItem(BaseModel):
    item_name: str = Field(alias="itemName")
    item_price: int = Field(alias="itemPrice")
    item_url: str = Field(alias="itemUrl")
    shop_name: str = Field(alias="shopName")
    item_caption: str = Field(alias="itemCaption")
    image_url: Optional[str] = Field(None, alias="mediumImageUrls") # Simplify for now

class IchibaSearchResponse(BaseModel):
    count: int
    page: int
    first: int
    last: int
    hits: int
    carrier: int
    page_count: int = Field(alias="pageCount")
    items: List[dict] = Field(alias="Items") # Raw items for further parsing if needed

class RakutenBook(BaseModel):
    title: str
    author: str
    item_price: int = Field(alias="itemPrice")
    item_url: str = Field(alias="itemUrl")
    publisher_name: str = Field(alias="publisherName")
    sales_date: str = Field(alias="salesDate")
