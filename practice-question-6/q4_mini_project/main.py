# ============================================================
# Q4: main.py — Wire it all together
# ============================================================
# Use ONLY these imports (do not change them):
from store.models import Product, Order
from store.services import apply_discount, calculate_total
from store.utils import format_currency, format_order_summary

# TASK: Write code that does the following:
#
# 1. Create these products:
#    - Laptop, price=85000, category="Electronics"
#    - Mouse, price=1500, category="Electronics"
#    - Python Book, price=800, category="Books"
#
# 2. Apply a 10% discount to the Laptop's price.
#    Print: "Laptop after 10% discount: ₹76,500.00"
#
# 3. Create an Order with order_id=42 containing Laptop and Mouse.
#    (Use the discounted Laptop price — create a new Product with the discounted price)
#
# 4. Print the full order summary using format_order_summary.
#    Expected:
#      Order #42 [pending]
#      - Laptop: ₹76,500.00
#      - Mouse: ₹1,500.00
#      Total: ₹78,000.00
#
# 5. Verify that creating a Product with price=-100 raises a ValueError.
#
# Your solution:

laptop = Product("Laptop", 85000, "Electronics")
mouse = Product("Mouse", 1500, "Electronics")
python_book = Product("Python Book", 800, "Books")

laptop_discount = 10
laptop_discounted_price = apply_discount(laptop.price, laptop_discount)

print(
    f"{laptop.name} after {laptop_discount}% discount: {format_currency(laptop_discounted_price)}"
)

discounted_laptop = Product("Laptop", laptop_discounted_price, "Electronics")
order = Order(42, [discounted_laptop, mouse])

print(format_order_summary(order))

bad_product = Product("Bad Product", -100, "Grocery")