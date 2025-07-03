from fastapi import APIRouter
from app.api.v1.endpoints import suppliers, products, imports, pricing, exports

api_router = APIRouter()

# Регистрация всех эндпоинтов
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(imports.router, prefix="/imports", tags=["imports"])
api_router.include_router(pricing.router, prefix="/pricing", tags=["pricing"])
api_router.include_router(exports.router, prefix="/exports", tags=["exports"])
