# ============================================================
# Q2: main.py — Use the text_tools package
# ============================================================
# Import slugify, truncate, is_email, is_url from text_tools
# using a SINGLE import line (from text_tools import ...).
#
# Then run these and verify the outputs match the docstrings:

# slugify tests:
# print(slugify("Hello World"))         → hello-world
# print(slugify("  Python is Great!"))  → python-is-great
# print(slugify("100% Organic!"))       → 100-organic

# truncate tests:
# print(truncate("Hello World", 8))     → Hello...
# print(truncate("Hi", 10))             → Hi

# is_email tests:
# print(is_email("user@example.com"))   → True
# print(is_email("bad@"))               → False

# is_url tests:
# print(is_url("https://google.com"))   → True
# print(is_url("ftp://nope.com"))       → False

# Your solution:
from text_tools import slugify, truncate, is_email, is_url
print(slugify("Hello World"))
print(slugify("  Python is Great!"))
print(slugify("100% Organic!"))

print(truncate("Hello World", 8))
print(truncate("Hi", 10))

print(is_email("user@example.com"))
print(is_email("bad@"))

print(is_url("https://google.com"))
print(is_url("ftp://nope.com"))