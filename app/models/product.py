from sqlalchemy import Column, String, Integer

from app.core.db import Base


class Product(Base):
    nm_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    brand_id = Column(Integer, nullable=False)
    site_brand_id = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    sale = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    sale_price = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    feedbacks = Column(Integer)
    colors = Column(String)
