from fastapi import APIRouter, HTTPException
from models import Product, ProductScore
from services import evaluate_product_service

router = APIRouter()

@router.post("/evaluate-product", response_model=ProductScore)
async def evaluate_product(product: Product):
    try:
        return await evaluate_product_service(product)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))