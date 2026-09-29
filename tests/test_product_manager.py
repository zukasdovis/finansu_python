from product_class import Product
from product_manager import ProductManager

def test_add_products():
    manager = ProductManager()
    product = Product(
        "iPhone",
        999,
        "Electronics",
        "Apple phone"
    )
    manager.add_product(product)

    assert len(manager.products) == 1
    assert manager.products[0] == product

def test_remove_product():
    manager = ProductManager()
    product = Product(
        "iPhone",
        999,
        "Electronics",
        "Apple phone"
    )

    manager.add_product(product)

    result = manager.remove_product("iPhone")

    assert result is True
    assert len(manager.products) == 0

def test_remove_missing_product():
    manager = ProductManager()

    result = manager.remove_product("iPhone")

    assert result is False

def test_search_by_name():
    manager = ProductManager()

    product = Product(
        "iPhone",
        999,
        "Electronics",
        "Apple phone"
    )

    manager.add_product(product)

    result = manager.search_by_name("iPhone")

    assert result == product

def test_search_by_name_not_found():
    manager = ProductManager()

    result = manager.search_by_name("iPhone")

    assert result is None

def test_search_by_category():
    manager = ProductManager()

    product1 = Product("iPhone", 999, "Electronics", "Phone")
    product2 = Product("Bread", 2, "Food", "Bread")

    manager.add_product(product1)
    manager.add_product(product2)

    result = manager.search_by_category("Electronics")

    assert result == [product1]

def test_search_by_category_not_found():
    manager = ProductManager()

    result = manager.search_by_category("Electronics")

    assert len(result) == 0

def test_sort_by_price_incr():
    manager = ProductManager()

    expensive = Product("Laptop", 1500, "Electronics", "Laptop")
    cheap = Product("Mouse", 20, "Electronics", "Mouse")

    manager.add_product(expensive)
    manager.add_product(cheap)

    manager.sort_by_price_incr()

    assert manager.products == [cheap, expensive]

def test_sort_by_price_decr():
    manager = ProductManager()

    expensive = Product("Laptop", 1500, "Electronics", "Laptop")
    cheap = Product("Mouse", 20, "Electronics", "Mouse")

    manager.add_product(expensive)
    manager.add_product(cheap)

    manager.sort_by_price_decr()

    assert manager.products == [expensive, cheap]

def test_sort_by_name_incr():
    manager = ProductManager()

    expensive = Product("Laptop", 1500, "Electronics", "Laptop")
    cheap = Product("Mouse", 20, "Electronics", "Mouse")

    manager.add_product(expensive)
    manager.add_product(cheap)

    manager.sort_by_name_incr()

    assert manager.products == [expensive, cheap]

def test_sort_by_name_decr():
    manager = ProductManager()

    expensive = Product("Laptop", 1500, "Electronics", "Laptop")
    cheap = Product("Mouse", 20, "Electronics", "Mouse")

    manager.add_product(expensive)
    manager.add_product(cheap)

    manager.sort_by_name_decr()

    assert manager.products == [cheap, expensive]

def test_sort_by_category_incr():
    manager = ProductManager()

    expensive = Product("Laptop", 1500, "Electronics", "Laptop")
    cheap = Product("Mouse", 20, "Device", "Mouse")

    manager.add_product(expensive)
    manager.add_product(cheap)

    manager.sort_by_category_incr()

    assert manager.products == [cheap, expensive]

def test_sort_by_category_decr():
    manager = ProductManager()

    expensive = Product("Laptop", 1500, "Electronics", "Laptop")
    cheap = Product("Mouse", 20, "Device", "Mouse")

    manager.add_product(expensive)
    manager.add_product(cheap)

    manager.sort_by_category_decr()

    assert manager.products == [expensive, cheap]

def test_search_by_price_range():
    manager = ProductManager()
    
    product1 = Product("iPhone", 999, "Electronics", "Phone")
    product2 = Product("Bread", 2, "Food", "Bread")
    
    manager.add_product(product1)
    manager.add_product(product2)
    
    result = manager.search_by_price_range(1, 5)
    
    assert result == [product2]

def test_search_by_price_range_not_found():
    manager = ProductManager()

    result = manager.search_by_price_range(1,5)

    assert result == None
  