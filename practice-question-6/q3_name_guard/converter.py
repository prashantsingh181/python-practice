# ============================================================
# Q3: The __name__ == "__main__" guard
# ============================================================
# This file should work BOTH as:
#   - A reusable module (imported by main.py)
#   - A standalone runnable script (python3 converter.py)
#
# TASK A: Implement the three conversion functions below.
#
# TASK B: Add a __name__ guard at the bottom that runs a small
#         demo ONLY when this file is executed directly:
#           python3 converter.py
#         The demo should print conversions for a few sample values.
#         It should NOT run when main.py imports this file.
#
# Verify this works: running `python3 main.py` should NOT print the demo.
# Running `python3 converter.py` directly SHOULD print the demo.
# ============================================================


def km_to_miles(km: float) -> float:
    """1 km = 0.621371 miles"""
    return km * 0.621371    


def kg_to_lbs(kg: float) -> float:
    """1 kg = 2.20462 lbs"""
    return kg * 2.20462


def usd_to_inr(usd: float, rate: float = 83.5) -> float:
    """Convert USD to INR at given exchange rate."""
    return usd * rate


# TASK B: Your __name__ guard demo here:
if __name__ == "__main__":
    print(km_to_miles(2))
    print(kg_to_lbs(75))
    print(usd_to_inr(22))