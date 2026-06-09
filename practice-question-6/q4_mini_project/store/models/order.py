# store/models/order.py
# Your solution:

from dataclasses import dataclass, field
from .product import Product


@dataclass
class Order:
    order_id: int
    items: list[Product] = field(default_factory=list)
    status: str = "pending"
