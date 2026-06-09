# ============================================================
# Q3: main.py
# ============================================================
# Import the three functions from converter and use them.
# Running this file should print conversions but NOT the demo
# block from converter.py.
#
# Print:
#   "10 km = X miles"
#   "70 kg = X lbs"
#   "100 USD = X INR"
#
# Your solution:

from converter import km_to_miles, kg_to_lbs, usd_to_inr

km = 10
kg = 70
usd = 100

print(f'{km} km = {km_to_miles(km)} miles')
print(f'{kg} kg = {kg_to_lbs(kg)} lbs')
print(f'{usd} USD = {usd_to_inr(usd)} INR')