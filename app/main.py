from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas import ProductCreate, ProductUpdate, ProductResponse
from app.database import engine, Base, get_db
from app.models import Product

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Product API is running"}


@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price,
        category=product.category,
        description=product.description,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@app.patch("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    db_product = db.get(Product, product_id)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    for attr, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, attr, value)

        db.commit()
        db.refresh(db_product)

    return db_product


@app.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.get(Product, product_id)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()

    return db_product
