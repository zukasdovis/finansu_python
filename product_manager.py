from product_class import Product
 
class ProductManager:


    def __init__(self, products_data: list[Product] | None = None):
        self.products: list[Product] = []
        
        if products_data:
            for product_dict in products_data:
                if isinstance(product_dict, dict):
                    product = Product(
                        name=product_dict.get('name'),
                        price=product_dict.get('price'),
                        category=product_dict.get('category'),
                        description=product_dict.get('description')
                    )
                    self.products.append(product)
                elif isinstance(product_dict, Product):
                    self.products.append(product_dict)

    
    
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, name: str) -> bool:
        for i in range(len(self.products)):
            if self.products[len(self.products) - 1 - i].name == name:
                del self.products[len(self.products) - 1 - i]
                return True
        return False

    def print_products(self, product_list=None):
        if product_list is None:
            product_list = self.products

        print("Products:")
        for product in product_list:
            print(product)

    def search_by_name(self, name: str) -> Product | None:
        for product in self.products:
            if product.name == name:
                return product
        return None

    def search_by_category(self, category: str) -> list[Product] | None:
        products_by_category = []
        for product in self.products:
            if product.category == category:
                products_by_category.append(product)
        if products_by_category:
            return products_by_category
        else:
            return None

    def search_by_price_range(self, lower: float, upper: float) -> list[Product] | None:
        products_by_price = []
        for product in self.products:
            if product.price>=lower and product.price<=upper:
                products_by_price.append(product)
        if products_by_price:
            return products_by_price
        else:
            return None


    def update_product(self):
        print("Products:")

        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product.name} - {product.price} - {product.category}")

        try:
            choice = int(input("Enter the number of the product you want to update: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= choice < len(self.products):

            
            try:
                to_change = int(input("What to change: 1-name, 2-price, 3-category:"))
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

            if to_change == 1:
                updated_value = input("Enter name:")
                self.products[choice].name = updated_value
            elif to_change == 2:
                updated_value = float(input("Enter price:"))
                self.products[choice].price = updated_value
            elif to_change == 3:
                updated_value = input("Enter category:")
                self.products[choice].category = updated_value
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

    def sort_by_name_incr(self):
        self.products.sort(key=lambda product: product.name)  
    def sort_by_name_decr(self):
        self.products.sort(key=lambda product: product.name, reverse=True) 
        
    def sort_by_price_incr(self):
        self.products.sort(key=lambda product: product.price)  
    def sort_by_price_decr(self):
        self.products.sort(key=lambda product: product.price, reverse=True)  

    def sort_by_category_incr(self):
        self.products.sort(key=lambda product: product.category)  
    def sort_by_category_decr(self):
        self.products.sort(key=lambda product: product.category, reverse=True)  
    
    def get_total_products(self) -> int:
        return len(self.products)