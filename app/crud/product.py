from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.parse import parse_data
from app.models.product import Product
from app.schemas.product import QuantityUpdate


async def create_product(
        id: int,
        session: AsyncSession):
    new_product_data = parse_data(id)
    if 'error' in new_product_data.keys():
        return new_product_data
    db_product = Product(**new_product_data)
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product


async def get_product(id: int, session: AsyncSession):
    db_product = await session.execute(
        select(Product).where(
            Product.nm_id == id,
        ),
    )
    return db_product.scalars().first()


async def read_all_products(session: AsyncSession):
    db_products = await session.execute(select(Product))
    return db_products.scalars().all()


async def delete_product(db_product, session: AsyncSession):
    await session.delete(db_product)
    await session.commit()
    return db_product


async def update_quantity(
        db_product: Product,
        quantity: QuantityUpdate,
        session: AsyncSession,
) -> Product:
    update_data = quantity.dict()
    setattr(db_product, 'quantity', update_data['quantity'])
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product
