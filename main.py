import json

from product_class import Product
from product_manager import ProductManager

with open("products_file.json", "r") as f:
    product_data = json.load(f)

product_manager = ProductManager(product_data)


while True:
    try:
        x=int(input("Enter a number: 0-exit, 1-add product, 2-remove product, 3-view products, 4-search by name, 5-search by category, " \
        "6-search by price range,\n" \
        "7-update product, 8-sort products: "))
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
        product_manager.search_by_name(name)

    elif x==5:
        category = input("Enter category of product to search: ")
        product_manager.search_by_category(category)

    elif x==6:
        try:
            lower = float(input("Enter lower price limit: "))
            upper = float(input("Enter upper price limit: "))
            product_manager.search_by_price_range(lower, upper)
        except ValueError:
            print("Invalid input for price. Please enter a number.")
            continue
    elif x==7:
        product_manager.update_product()

    elif x==8:
        try:
            choice = int(input("Enter how you want to sort: 1-increasing by name, 2-decreasing by name, 3-increasing by price, 4-decreasing by price,\n " \
            "5-increasing by category, 6-decreasing by category: "))

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            product_manager.sort_by_name_incr()
        elif choice == 2:
            product_manager.sort_by_name_decr()
        elif choice == 3:
            product_manager.sort_by_price_incr()
        elif choice == 4:
            product_manager.sort_by_price_decr()
        elif choice == 5:
            product_manager.sort_by_category_incr()
        elif choice == 6:
            product_manager.sort_by_category_decr()

print(f"Total products: {product_manager.get_total_products()}")

with open("products_file.json", "w") as f:
    json.dump([p.to_dict() for p in product_manager.products], f, indent=4)