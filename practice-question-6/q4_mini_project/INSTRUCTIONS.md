# Q4: Mini Project — Build a structured Python package

You're building a small e-commerce order processing system
as a properly structured Python package.

## The structure is already created for you:

```
store/
├── __init__.py          ← expose the public API
├── models/
│   ├── __init__.py      ← re-export Product and Order
│   ├── product.py       ← Product dataclass
│   └── order.py         ← Order dataclass
├── services/
│   ├── __init__.py      ← re-export apply_discount, calculate_total
│   └── pricing.py       ← pricing logic
└── utils/
    ├── __init__.py      ← re-export format_currency, format_order_summary
    └── formatters.py    ← display formatting
```

## What to implement:

### store/models/product.py
A `Product` dataclass with fields:
- name: str
- price: float  (must be > 0, validate in __post_init__)
- category: str

### store/models/order.py
An `Order` dataclass with fields:
- order_id: int
- items: list[Product]   (default empty list)
- status: str            (default "pending")

### store/services/pricing.py
Two functions:
- `apply_discount(price, discount_pct)` → price after discount (0-100%)
- `calculate_total(order)` → sum of all item prices in the order

### store/utils/formatters.py
Two functions:
- `format_currency(amount)` → "₹1,234.56"  (use f-string with comma formatting)
- `format_order_summary(order)` → multi-line string:
    Order #42 [pending]
    - Laptop: ₹85,000.00
    - Mouse: ₹1,500.00
    Total: ₹86,500.00

### Each __init__.py
Re-export the right names so main.py can use clean imports.

## main.py should work with ONLY these imports:
```python
from store.models import Product, Order
from store.services import apply_discount, calculate_total
from store.utils import format_currency, format_order_summary
```

## Run with:
```
python3 main.py   (from inside q4_mini_project/)
```
