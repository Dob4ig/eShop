from fastapi import APIRouter
from product.schemas import ProductAdd

router = APIRouter()


@router.post("/add")
async def add_product(product: ProductAdd):
    return {
        "status": "success"
    }
