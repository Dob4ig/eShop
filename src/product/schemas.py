from pydantic import BaseModel, Field


class ProductAdd(BaseModel):
    name: str = Field(max_length=50)
    description: str
    seller_id: int = Field(ge=0)
    price: float = Field(ge=0)


class ProductGet(BaseModel):
    id: int = Field(ge=0)
    name: str
    description: str
    price: float = Field(ge=0)
    seller_id: int = Field(ge=0)
