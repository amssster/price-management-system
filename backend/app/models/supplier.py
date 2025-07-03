from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum


class SupplierStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    code = Column(String(50), unique=True, nullable=False, index=True)
    description = Column(Text)

    # Контактная информация
    contact_person = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    website = Column(String(255))

    # Настройки
    status = Column(Enum(SupplierStatus), default=SupplierStatus.ACTIVE)
    prefix = Column(String(10))
    currency = Column(String(3), default="USD")
    exchange_rate = Column(Float, default=1.0)
    default_markup = Column(Float, default=0.0)
    vat_rate = Column(Float, default=0.0)

    # Настройки импорта
    import_url = Column(String(500))
    import_format = Column(String(20))
    import_frequency = Column(String(20))
    last_import = Column(DateTime)

    # Метаданные
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Связи
    products = relationship("Product", back_populates="supplier")
    import_logs = relationship("ImportLog", back_populates="supplier")
    pricing_rules = relationship("PricingRule", back_populates="supplier")

    def __str__(self):
        return f"Supplier(id={self.id}, name={self.name}, code={self.code})"
