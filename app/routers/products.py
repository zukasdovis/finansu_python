from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate, ProductResponse

from app.services.products import (
    get_product,
    create_product,
    get_products,
    update_product,
    delete_product,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductResponse])
def get_products_endpoint(db: Session = Depends(get_db)):
    return get_products(db)


@router.post("/", response_model=ProductResponse)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.patch("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    updated_product = update_product(db, product_id, product)

    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product


@router.delete("/{product_id}", response_model=ProductResponse)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    deleted_product = delete_product(db, product_id)

    if deleted_product is None:
        raise HTTPException(status=404, detail="Product not found")

    return deleted_product
