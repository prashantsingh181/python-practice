from math_utils import celsius_to_fahrenheit, is_prime
import math_utils
from math_utils import GOLDEN_RATIO as phi

# ============================================================
# Q1: main.py — Import and use math_utils
# ============================================================
#
# TASK A: Import celsius_to_fahrenheit and is_prime from math_utils
#         using a NAMED import (from ... import ...).
#         Then call them and print:
#           "100°C = 212.0°F"
#           "17 is prime: True"
#           "4 is prime: False"
#
# TASK B: Import the entire math_utils module (import math_utils)
#         and call clamp via the module namespace:
#           clamp(15, 0, 10) → should print 10
#           clamp(-5, 0, 10) → should print 0
#           clamp(7, 0, 10)  → should print 7
#
# TASK C: Import GOLDEN_RATIO with an alias `phi` and print it.
#
# Your solution:

temp_in_celcius = 100
print(f"{temp_in_celcius}°C = {celsius_to_fahrenheit(temp_in_celcius)}°F")

number1 = 17
number2 = 4
print(f"{number1} is prime: {is_prime(number1)}")
print(f"{number2} is prime: {is_prime(number2)}")


print(math_utils.clamp(15, 0, 10))
print(math_utils.clamp(-5, 0, 10))
print(math_utils.clamp(7, 0, 10))

print(phi)