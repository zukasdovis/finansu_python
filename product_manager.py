from product_class import Product
 
class ProductManager:

    total_products = 0

    def __init__(self, products_data=None):
        self.products = []
        
        if products_data:
            for product_dict in products_data:
                if isinstance(product_dict, dict):
                    product = Product(
                        product_dict.get('name'),
                        product_dict.get('price'),
                        product_dict.get('category'),
                        product_dict.get('description')
                    )
                    self.products.append(product)
                elif isinstance(product_dict, Product):
                    self.products.append(product_dict)
            total_products = len(self.products)

    
    
    def add_product(self, product):
        self.products.append(product)
        self.total_products+=1

    def remove_product(self, name):
        for i in range(len(self.products)):
            if self.products[len(self.products) - 1 - i].name == name:
                del self.products[len(self.products) - 1 - i]
                self.total_products -= 1
                return True
        return False

    def print_products(self):
        print("Products:")
        for product in self.products:
            print(product)

    def search_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return (f"Product with name '{name}' not found.")

    @classmethod
    def get_total_products(cls):
        return cls.total_products