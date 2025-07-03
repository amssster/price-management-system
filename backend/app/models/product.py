from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    # Основная информация
    name = Column(String(500), nullable=False, index=True)
    sku = Column(String(100), unique=True, nullable=False, index=True)
    supplier_sku = Column(String(100), index=True)
    barcode = Column(String(50))

    # Описание
    description = Column(Text)
    short_description = Column(Text)
    specifications = Column(Text)

    # Категоризация
    category = Column(String(255))
    brand = Column(String(255))
    model = Column(String(255))

    # Ценообразование
    cost_price = Column(Float)
    retail_price = Column(Float)
    wholesale_price = Column(Float)
    markup_percent = Column(Float)

    # Складские данные
    quantity = Column(Integer, default=0)
    min_quantity = Column(Integer, default=0)
    weight = Column(Float)
    dimensions = Column(String(100))

    # Статус
    is_active = Column(Boolean, default=True)
    in_stock = Column(Boolean, default=True)

    # Изображения
    image_url = Column(String(500))
    gallery_urls = Column(Text)

    # SEO
    seo_title = Column(String(255))
    seo_description = Column(Text)
    seo_keywords = Column(String(500))

    # Связи
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    # Метаданные
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Отношения
    supplier = relationship("Supplier", back_populates="products")

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, sku={self.sku})"
