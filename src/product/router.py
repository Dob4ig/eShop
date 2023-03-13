from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from product.schemas import ProductAdd
from product.models import Product
from database import get_async_session
from product.schemas import ProductGet
router = APIRouter()


@router.post("/add")
async def add_product(new_product: ProductAdd,
                      session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Product).values(**new_product.dict())
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

    query = select(Product).where(Product.c.id == id)
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


@router.get("/seller/{id}", response_model=ProductGet)
async def get_products_by_seller_id(
        id: int,
        limit: int,
        offset: int,
        session: AsyncSession = Depends(get_async_session)):

    if limit < 0 or limit > 100:
        raise HTTPException(400, detail={
            "status": "error",
            "data": None,
            "details": "Limit must be >0 and < 100"
        })
    if offset < 0:
        raise HTTPException(400, detail={
            "status": "error",
            "data": None,
            "details": "offset must be greater then 0"})

    query = select(Product).where(Product.seller_id ==
                                  id).limit(limit).offset(offset)

    result = await session.execute(query)
    result: List = [x[0].serialize for x in result.all()]

    return {
        "status": "succes",
        "data": result,
        "details": None
    }
