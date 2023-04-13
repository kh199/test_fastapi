from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    nm_id: int


class ProductCreate(ProductBase):
    nm_id: int
    # name: str
    # brand: str
    # brand_id: int
    # site_brand_id: int
    # supplier_id: int
    # sale: int
    # price: int
    # sale_price: int
    # rating: int
    # feedbacks: int
    # colors: Optional[str]


class ProductDB(ProductCreate):
    id: int

    class Config:
        orm_mode = True
