from app.models.product import Product
from app.schemas.product import ProductCreate, ProductBase
from app.crud.parse import parse_data
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def create_product(
        db_product: ProductCreate,
        session: AsyncSession) -> Product:
    new_product_data = parse_data(id)
    db_product = Product(**new_product_data)
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product


async def get_product(id: int, session: AsyncSession):
    db_product = await session.execute(
        select(Product).where(
            Product.id == id,
        ),
    )
    return db_product.scalars().first()


async def get_all_products(session: AsyncSession):
    db_products = await session.execute(select(Product))
    return db_products.scalars().all()


async def delete_product(db_product: ProductBase, session: AsyncSession):
    await session.delete(db_product)
    await session.commit()
    return db_product
