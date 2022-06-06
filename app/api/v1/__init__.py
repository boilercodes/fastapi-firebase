from app.api.v1 import products
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])
