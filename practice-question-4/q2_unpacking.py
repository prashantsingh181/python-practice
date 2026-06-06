from functools import reduce

# ============================================================
# Q2: Unpacking, *args, **kwargs
# ============================================================
# JS equivalent: destructuring, rest/spread (...args)
# Python's version is similar but has some key differences.
#
# QUESTION 2a:
# Given this tuple:
point = (10, 20, 30)
#
# Unpack it into three variables: x, y, z.
# Then print: "x=10, y=20, z=30"
# (Use an f-string)
#
# Your solution:
x, y, z = point
print(f"x={x}, y={y}, z={z}")

# ---------------------------------------------------------------
# QUESTION 2b — Extended unpacking (search this!):
# Given this list:
data = [1, 2, 3, 4, 5, 6]
#
# Using the * operator in unpacking:
# - Assign the first element to `first`
# - Assign the last element to `last`
# - Assign everything in between to `middle`
# In ONE line (no slicing, no indexing).
#
# HINT: Python has "starred assignment" — similar to JS rest destructuring
#       but the * can go anywhere: first, *rest = ... or *rest, last = ...
#
# Your solution:
first, *middle, last = data
print(first, middle, last)


# ---------------------------------------------------------------
# QUESTION 2c — *args:
# Write a function called `sum_all` that:
# - Accepts ANY number of positional arguments
# - Returns their sum
# - Works for: sum_all(1, 2), sum_all(1, 2, 3, 4, 5), sum_all(10)
#
# Your solution:
def sum_all(*args):
    return reduce(lambda acc, item: acc + item, args)


print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(10))


# ---------------------------------------------------------------
# QUESTION 2d — **kwargs:
# Write a function called `build_profile` that:
# - Accepts a required `username` argument
# - Accepts any number of keyword arguments
# - Returns a dict with 'username' plus all the extra kwargs
#
# Example:
#   build_profile("prashant", role="dev", city="Mumbai")
#   → {'username': 'prashant', 'role': 'dev', 'city': 'Mumbai'}
#
# Your solution:
def build_profile(username, **kwargs):
    user = kwargs.copy()
    user["username"] = username
    return user


print(build_profile("prashant", role="dev", city="mumbai"))


# ---------------------------------------------------------------
# QUESTION 2e (stretch) — Unpacking into function calls:
# You have this function:
def greet(first_name, last_name, greeting="Hello"):
    return f"{greeting}, {first_name} {last_name}!"


# And this dict:
person = {"first_name": "Prashant", "last_name": "Singh", "greeting": "Hey"}
#
# Call `greet` by UNPACKING the dict as keyword arguments (one line, no manual extraction).
# HINT: In JS you'd do greet({...person}) but Python has a different operator for this.
#
# Your solution:
print(greet(**person))
