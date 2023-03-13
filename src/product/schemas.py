from pydantic import BaseModel, Field
from typing import Optional, List
from response import ResponseBaseSchema


class ProductAdd(BaseModel):
    name: str = Field(max_length=50)
    description: str
    seller_id: int = Field(ge=0)
    price: float = Field(ge=0)


class Product(BaseModel):
    id: int = Field(ge=0)
    name: str
    description: str
    price: float = Field(ge=0)
    seller_id: int = Field(ge=0)


class ProductGet(ResponseBaseSchema):
    data: Optional[List[Product]]
