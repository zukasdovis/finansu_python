from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    category: str
    description: str

products = []

@app.get("/")
def home():
    return {"message": "Product API is running"}

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id >= len(products):
        return {"error": "Product not found"}
    return products[product_id]