# ============================================================
# Q3: Decorators
# ============================================================
# JS equivalent: Higher-order functions, middleware, method wrappers
# Decorators are Python's built-in syntax for wrapping functions.
#
# A decorator is just a function that takes a function and returns a function.
# The @syntax is syntactic sugar — @my_decorator above a function is the same as:
#   my_func = my_decorator(my_func)
#
# QUESTION 3a — Read and understand:
# What does this decorator do? Add a comment explaining it in plain English.
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result

    return wrapper


# Your explanation as a comment:
# This is a decorator function that can be added with @timer above a function
# and whenever that function is called that function will run and decorator
# will calculate and print the time taken by that function

# ---------------------------------------------------------------
# QUESTION 3b — Write your own decorator:
# Write a decorator called `shout` that:
# - Wraps any function that returns a string
# - Converts the return value to UPPERCASE
#
# Then apply it to this function using the @ syntax:

#
# So that greet("prashant") returns "HELLO, PRASHANT"
#
# Your decorator:
import functools


def shout(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        value = fn(*args, **kwargs)
        return value.upper()

    return wrapper


@shout
def greet(name):
    return f"hello, {name}"


print(greet("prashant"))


# ---------------------------------------------------------------
# QUESTION 3c — Decorator with arguments (search this!):
# This is a level up — decorators that take their own parameters.
# Write a decorator called `repeat(n)` that runs the decorated function n times.
#
# Usage should look like:
#
#   @repeat(3)
#   def say_hi():
#       print("hi")
#
#   say_hi()  # prints "hi" three times
#
# HINT: You need THREE levels of nesting: the outer function takes n,
#       returns a decorator, which takes func, returns wrapper.
#       Search: "decorator with arguments python"
#
# Your solution:
def repeat(n):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for i in range(n):
                if i == n - 1:
                    return fn(*args, **kwargs)
                fn(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hi():
    print("hi")


say_hi()


# ---------------------------------------------------------------
# QUESTION 3d (stretch) — functools.wraps (search this!):
# There's a problem with naive decorators. Try this:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def important_function():
    """This function does something important."""
    pass


print(important_function.__name__)  # What does this print? Why is it a problem?
print(important_function.__doc__)  # And this?


# Fix the decorator using functools.wraps so the original metadata is preserved.
# Search: "functools wraps python"
#
# Your fixed version:
def my_version_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


@my_version_decorator
def some_func():
    "Doc string of some_func"
    pass


print(some_func.__name__)
print(some_func.__doc__)
