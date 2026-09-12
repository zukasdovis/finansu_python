class Product:
    
    def __init__(self, name, price, category, description):
        self.name = name
        self.price = price
        self.category = category
        self.description = description


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
        return (
        f"Product(name={self.name!r}, "
        f"price={self.price!r}, "
        f"category={self.category!r}, "
        f"description={self.description!r})"
        )
    def to_dict(self):
        return{
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'description': self.description
            }

        