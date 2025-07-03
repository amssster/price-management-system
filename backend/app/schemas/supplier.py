from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
from enum import Enum


class SupplierStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class SupplierBase(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    status: SupplierStatus = SupplierStatus.ACTIVE
    prefix: Optional[str] = None
    currency: str = "USD"
    exchange_rate: float = 1.0
    default_markup: float = 0.0
    vat_rate: float = 0.0
    import_url: Optional[str] = None
    import_format: Optional[str] = None
    import_frequency: Optional[str] = None


class SupplierCreate(SupplierBase):
    @validator('code')
    def validate_code(cls, v):
        if not v or len(v) < 2:
            raise ValueError('Код поставщика должен содержать минимум 2 символа')
        return v.upper()


class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    status: Optional[SupplierStatus] = None
    prefix: Optional[str] = None
    currency: Optional[str] = None
    exchange_rate: Optional[float] = None
    default_markup: Optional[float] = None
    vat_rate: Optional[float] = None
    import_url: Optional[str] = None
    import_format: Optional[str] = None
    import_frequency: Optional[str] = None


class SupplierInDB(SupplierBase):
    id: int
    created_at: datetime
    updated_at: datetime
    last_import: Optional[datetime] = None

    class Config:
        from_attributes = True
