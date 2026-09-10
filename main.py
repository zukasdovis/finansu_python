import json

from product_class import Product
from product_manager import ProductManager

with open("products_file.json", "r") as f:
    product_data = json.load(f)

product_manager = ProductManager(product_data)


while True:
    try:
        x=int(input("Enter a number: 0-exit, 1-add product, 2-remove product, 3-view products, 4-search by name, 5-search by category: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if x==0:
        break
    elif x==1:
        name = input("Enter product name: ")
        try:
            price = float(input("Enter product price: "))
        except ValueError:
            print("Invalid input for price. Please enter a number.")
            continue
        category = input("Enter product category: ")
        description = input("Enter product description: ")

        product = Product(name, price, category, description)

        product_manager.add_product(product)

    elif x==2:
        name = input("Enter product name to remove: ")
        if product_manager.remove_product(name):
            print(f"Product '{name}' removed successfully.")
        else:
            print(f"Product '{name}' not found.")
    elif x==3:
        product_manager.print_products()

    elif x==4:
        name = input("Enter name of product to search: ")
        print(product_manager.search_by_name(name))

    elif x==5:
        category = input("Enter category of product to search: ")
        print(product_manager.search_by_category(category))

    elif x==6:
        try:
            lower = float(input("Enter lower price limit: "))
            upper = float(input("Enter upper price limit: "))
            print(product_manager.search_by_price_range(lower, upper))
        except ValueError:
            print("Invalid input for price. Please enter a number.")
            continue

print(f"Total products: {product_manager.get_total_products()}")

with open("products_file.json", "w") as f:
    json.dump([p.to_dict() for p in product_manager.products], f, indent=4)