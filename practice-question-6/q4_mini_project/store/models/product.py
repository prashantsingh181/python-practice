# store/models/product.py
# Your solution:

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    category: str

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("price must be greater than 0")
