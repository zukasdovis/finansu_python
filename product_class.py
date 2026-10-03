from dataclasses import dataclass


@dataclass
class Product:

    name: str
    price: float
    category: str
    description: str

    def __post_init__(self):
        if not isinstance(self.price, (int, float)):
            raise ValueError("Price must be a number")

        if self.price < 0:
            raise ValueError("Price cannot be negative")

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Price: {self.price}, "
            f"Category: {self.category}, "
            f"Description: {self.description}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["category"], data["description"])
