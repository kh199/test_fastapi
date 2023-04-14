from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_for_create, check_product_exists
from app.core.db import get_async_session
from app.crud.product import (create_product, delete_product, get_product,
                              read_all_products, update_quantity)
from app.schemas.product import ProductDB, QuantityUpdate

router = APIRouter(prefix='/api/products', tags=['Products'])


@router.post(
        '/',
        response_model=ProductDB | dict,
        response_model_exclude_none=True,
        status_code=HTTPStatus.OK,
        summary='Создание товара по id',
        )
async def create_new_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    product_id = await check_for_create(product_id, session)
    new_product = await create_product(product_id, session)
    return new_product


@router.get(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary='Просмотр товара по id',
)
async def get_one_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    product = await check_product_exists(product_id, session)
    product = await get_product(product_id, session)
    return product


@router.get(
    '/',
    response_model=list[ProductDB],
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary='Просмотр списка товаров',
)
async def get_all_products(
        session: AsyncSession = Depends(get_async_session),
):
    all_products = await read_all_products(session)
    return all_products


@router.delete(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary='Удаление товара по id',
)
async def remove_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    product = await check_product_exists(product_id, session)
    product = await delete_product(product, session)
    return product


@router.patch(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True,
    status_code=HTTPStatus.OK,
    summary='Обновление количества товара',
)
async def update_product(
        product_id: int,
        quantity: QuantityUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    db_product = await check_product_exists(product_id, session)
    updated_product = await update_quantity(db_product, quantity, session)
    return updated_product
