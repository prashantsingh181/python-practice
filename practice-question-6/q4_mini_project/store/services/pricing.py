# store/services/pricing.py
# Your solution:

from store.models import Order
from functools import reduce


def apply_discount(price: float, discount_pct: float) -> float:
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("discount_pct must be between 0 and 100")

    if price < 0:
        raise ValueError("price must be greater than 0")

    return price * (1 - (discount_pct / 100))


def calculate_total(order: Order) -> float:
    return reduce(lambda acc, item: acc + item.price, order.items, 0)
