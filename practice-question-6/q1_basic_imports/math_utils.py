import math

# ============================================================
# Q1: Basic Module Creation & Importing
# ============================================================
# This file is a MODULE. main.py will import from it.
#
# TASK: Implement the three functions below.
# Do not change the function signatures.
# ============================================================


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (9 / 5 * c) + 32


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    # Your implementation:
    sqrt_int = math.trunc(math.sqrt(n))

    for i in range(2, sqrt_int + 1):
        if n % i == 0:
            return False

    return True


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Return value clipped to [min_val, max_val]."""
    # Your implementation:
    return max(min_val, min(max_val, value))


# ---------------------------------------------------------------
# BONUS: Add a module-level constant called GOLDEN_RATIO = 1.618033988749895
# Then import and use it in main.py
GOLDEN_RATIO = 1.618033988749895