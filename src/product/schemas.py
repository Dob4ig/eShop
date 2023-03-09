from pydantic import BaseModel, Field
from typing import Optional


class ProductAdd(BaseModel):
    id: Optional[int] = Field(ge=0)
    name: str = Field(max_length=50)
    description: str
    seller_id: int = Field(ge=0)
