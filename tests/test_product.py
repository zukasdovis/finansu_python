import sys
import pytest
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from product_class import Product

def test_product_creation():
    product = Product(
        "iPhone",
        999,
        "Electronics",
        "Apple phone"
    )

    assert product.name == "iPhone"
    assert product.price == 999
    assert product.category == "Electronics"
    assert product.description == "Apple phone"

def test_negative_price():
    with pytest.raises(ValueError):
        Product("Test", -10, "Test", "Test")

def test_valid_price():
    with pytest.raises(ValueError):
        Product("Test", "Test", "Test", "Test") 

def test_to_dict():
    product = Product(
        "iPhone",
        999,
        "Electronics",
        "Apple phone"
    )

    result = product.to_dict()

    assert result == {'name': product.name,
                    'price': product.price,
                    'category': product.category,
                    'description': product.description
                    }

def test__str__():
    product = Product(
            "iPhone",
            999,
            "Electronics",
            "Apple phone"
        )
    assert str(product) == (
            f"Name: {product.name}, "
            f"Price: {product.price}, "
            f"Category: {product.category}, "
            f"Description: {product.description}"
        )
