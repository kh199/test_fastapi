from fastapi import APIRouter
from app.crud.product import create_product
from app.schemas.product import ProductCreate

router = APIRouter()


@router.post('/products/')
async def create_new_meeting_room(
        product: ProductCreate,
):
    new_product = await create_product(product)
    return new_product
