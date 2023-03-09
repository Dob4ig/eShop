from pydantic import BaseModel, Field


class ProductAdd(BaseModel):
    name: str = Field(max_length=50)
    description: str
    seller_id: int = Field(ge=0)
    price: float = Field(ge=0)
