from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from product.schemas import ProductAdd
from product.models import product
from database import get_async_session
from product.schemas import ProductGet
router = APIRouter()


@router.post("/add")
async def add_product(new_product: ProductAdd,
                      session: AsyncSession = Depends(get_async_session)):
    stmt = insert(product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        "status": "success",
        "data": new_product.dict(),
        "details": "New product added"}


@router.get("/{id}")
async def get_product(id: int,
                      session: AsyncSession = Depends(get_async_session)):
    if id < 0:
        raise HTTPException(400, detail={
            "status": "error",
            "data": None,
            "details": "Product id cannot be negative number"
        })

    query = select(product).where(product.c.id == id)
    result = await session.execute(query)
    result = result.fetchone()

    if result is None:
        raise HTTPException(404, detail={
            "status": "error",
            "data": None,
            "details": f"Post with id={id} not found"
        })

    return {
        "status": "success",
        "data": tuple(result),
        "details": None}


@router.get("/seller/{id}", response_model=List[ProductGet])
async def get_product_by_seller_id(
        id: int,
        session: AsyncSession = Depends(get_async_session)):

    query = select(product).where(product.c.seller_id == id)
    result = await session.execute(query)
    return result.all()
