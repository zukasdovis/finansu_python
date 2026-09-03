from product_class import Product
 
class ProductManager:
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
    
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for i in range(len(self.products)):
            if self.products[len(self.products) - 1 - i].name == name:
                del self.products[len(self.products) - 1 - i]
                return True
        return False

    def print_products(self):
        print("Products:")
        for product in self.products:
            print(product)