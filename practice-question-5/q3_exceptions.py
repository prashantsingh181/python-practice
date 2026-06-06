# ============================================================
# Q3: Exception Handling — the full pattern
# ============================================================
# You know try/except. Python also has `else` and `finally` on
# try blocks — and they do something JS's try/catch/finally doesn't.
#
# try:    → attempt the risky thing
# except: → runs if an exception was raised
# else:   → runs ONLY if NO exception was raised (this is the JS gap)
# finally:→ always runs, exception or not
#
# ---------------------------------------------------------------
# QUESTION 3a — Read and explain:
# Without running this, trace through what gets printed for each call.
# Add a comment next to each print with what you think it outputs.


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result: {result}")
    finally:
        print("Done")


divide(10, 2)
# Your prediction (comment): Result: 5

divide(10, 0)
# Your prediction (comment): ZeroDivisionError "Cannot divide by zero"


# ---------------------------------------------------------------
# QUESTION 3b — Custom exceptions:
# Define a custom exception class called `InsufficientFundsError`
# that accepts a `requested` amount and an `available` amount.
# Its __str__ should return:
#   "Requested 500, but only 200 available"
#
# Then write a function `withdraw(balance, amount)` that:
# - Raises InsufficientFundsError if amount > balance
# - Returns the new balance otherwise
#
# Test both paths.
#
# Your solution:
class InsufficientFundsError(Exception):

    def __init__(self, requested, available):
        self.requested = requested
        self.available = available

    def __str__(self):
        return f"Requested {self.requested}, but only {self.available} available"


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    else:
        return balance - amount


print(withdraw(300, 100))
# print(withdraw(200, 400))


# ---------------------------------------------------------------
# QUESTION 3c — Catching multiple exceptions:
# Write a function `safe_parse(value)` that:
# - Tries to convert `value` to an integer
# - If that fails, tries to convert it to a float
# - If that also fails, returns None
# - Always prints "parse attempted" regardless of outcome
#
# safe_parse("42")    → 42   (int)
# safe_parse("3.14")  → 3.14 (float)
# safe_parse("hello") → None
#
# Your solution:
def safe_parse(value):
    try:
        return_value = int(value)
    except ValueError:
        try:
            return_value = float(value)
        except ValueError:
            return_value = None
    finally:
        print("parse attempted")
    return return_value


print(safe_parse("42"))
print(safe_parse("3.14"))
print(safe_parse("hello"))


# ---------------------------------------------------------------
# QUESTION 3d (stretch) — re-raising:
# Sometimes you want to catch an exception, do something (like log it),
# then re-raise it so the caller still sees it.
#
# Write a function `logged_divide(a, b)` that:
# - Tries to divide a by b
# - If ZeroDivisionError occurs, prints "ERROR: division by zero attempted"
#   and then re-raises the same exception (use `raise` with no argument)
# - The caller should still get the ZeroDivisionError
#
# Your solution:
def logged_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: division by zero attempted")
        raise


logged_divide(10, 0)
