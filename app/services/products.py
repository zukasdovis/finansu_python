from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate, ProductUpdate


def get_product(db: Session, product_id: int):
    return db.get(Product, product_id)


def create_product(db: Session, product_data: ProductCreate):
    new_product = Product(
        name=product_data.name,
        price=product_data.price,
        category=product_data.category,
        description=product_data.description,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def get_products(db: Session):
    return db.query(Product).all()


def update_product(db: Session, product_id: int, product_data: ProductUpdate):
    product = db.get(Product, product_id)

    if product is None:
        return None

    update_data = product_data.model_dump(exclude_unset=True)

    for attr, value in update_data.items():
        setattr(product, attr, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int):
    product = db.get(Product, product_id)

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return product
