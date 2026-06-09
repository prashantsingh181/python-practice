# store/utils/formatters.py
# Your solution:

import locale
from store.models import Order
from store.services import calculate_total

locale.setlocale(locale.LC_MONETARY, "en_IN")


def format_currency(amount: float) -> str:
    return locale.currency(amount, grouping=True)


def format_order_summary(order: Order) -> str:

    output = f"Order#{order.order_id} [{order.status}]\n"
    for item in order.items:
        output += f"- {item.name}: {format_currency(item.price)}\n"

    output += f"Total: {format_currency(calculate_total(order))}"

    return output
