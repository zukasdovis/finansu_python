class Product():

    total_products = 0
    
    def __init__(self, name, price, category, description):
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        Product.total_products += 1


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Category: {self.category}, Description: {self.description}"

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category}, description={self.description})"

    @classmethod
    def get_total_products(cls):
        return cls.total_products

        