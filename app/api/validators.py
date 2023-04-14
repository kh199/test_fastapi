from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.product import get_product
from app.models.product import Product


async def check_product_exists(
        product_id: int,
        session: AsyncSession,
) -> Product:
    product = await get_product(product_id, session)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail='Product not found'
        )
    return product


async def check_for_create(
        product_id: int,
        session: AsyncSession,
) -> Product:
    product = await get_product(product_id, session)
    if product is not None:
        raise HTTPException(
            status_code=404,
            detail='Product already exists'
        )
    return product_id
