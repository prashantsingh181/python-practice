from dataclasses import dataclass, field

# ============================================================
# Q4: dataclasses
# ============================================================
# Writing __init__, __repr__, __eq__ by hand every time is tedious.
# Python's @dataclass decorator generates them for you from
# simple field declarations — similar to TypeScript interfaces
# but with runtime behavior baked in.
#
# from dataclasses import dataclass, field
#
# ---------------------------------------------------------------
# QUESTION 4a — Basic dataclass:
# Rewrite this class as a dataclass.
# You should be able to delete __init__ and __repr__ entirely
# and get the same behavior.


class ProductOld:
    def __init__(self, name: str, price: float, in_stock: bool = True):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, price={self.price}, in_stock={self.in_stock})"
        )


# Your dataclass version:
# (Check: repr(Product("Laptop", 999.99)) should print the same as above)


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True


print(repr(Product("Laptop", 999.99)))

# ---------------------------------------------------------------
# QUESTION 4b — Default values and field():
# Create a dataclass called `Order` with:
# - order_id: int
# - items: list  (default should be an empty list — but there's a gotcha here.
#                 Try using [] as a default first. What error do you get? Why?
#                 Then fix it using field(default_factory=...))
# - status: str = "pending"
#
# Your solution:


@dataclass
class Order:
    order_id: int
    items: list = field(default_factory=list)
    status: str = "pending"


# ---------------------------------------------------------------
# QUESTION 4c — Frozen dataclass:
# A frozen dataclass is immutable — like a namedtuple but with type hints.
# Create a frozen dataclass called `Coordinate` with fields lat and lon (both float).
# Verify it's immutable by trying to assign to a field and catching the error.
#
# Your solution:


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float


coordinate = Coordinate(22.12, 22.11)

try:
    coordinate.lat = 10.12
except Exception as err:
    print(err)

# ---------------------------------------------------------------
# QUESTION 4d (stretch) — post_init:
# dataclasses have a __post_init__ method that runs after __init__.
# It's useful for validation.
#
# Create a dataclass `PositiveNumber` with a single field `value: float`.
# In __post_init__, raise a ValueError if value <= 0.
#
# Your solution:


@dataclass
class PositiveNumber:
    value: float

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError


positive_number = PositiveNumber(-12)
