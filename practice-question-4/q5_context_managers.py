# ============================================================
# Q5: Context Managers (the `with` statement)
# ============================================================
# JS equivalent: try/finally blocks, or the "using" proposal (Stage 3)
# Python's `with` statement is how you manage resources that need cleanup:
# files, database connections, locks, timers, etc.
#
# You've probably seen: with open("file.txt") as f: ...
# This question explores what's happening under the hood and how to build your own.
#
# QUESTION 5a — Why `with` exists:
# The code below opens a file WITHOUT a context manager.
# Rewrite it using `with open(...) as f:` syntax.
# Then add a comment: what happens to the file if an exception is raised
# in the non-`with` version vs the `with` version?

# Non-context-manager version (rewrite this):
# f = open("notes.txt", "w")
# f.write("Hello from Python")
# f.close()
#
# Your version:
with open("notes.txt", "w") as f:
    f.write("Hello from Python")


# ---------------------------------------------------------------
# QUESTION 5b — Build a context manager using a class (search this!):
# A context manager is any object that implements __enter__ and __exit__.
#
# Write a class called `Timer` that:
# - On __enter__: records the start time (use time.time()) and returns self
# - On __exit__: records the end time, prints "Elapsed: X.XXXXs"
# - __exit__ receives 3 args after self: exc_type, exc_val, exc_tb
#   (these are for exception handling — return False or None to not suppress errors)
#
# Usage:
#   with Timer() as t:
#       sum(range(1_000_000))
#   # prints: Elapsed: 0.0312s (or similar)
#
# Your solution:
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        time_elapsed = end_time - self.start_time
        print(f"Elapsed: {time_elapsed:.4f}s")


with Timer() as t:
    sum(range(1_000_000))


# ---------------------------------------------------------------
# QUESTION 5c — Build a context manager using contextlib (search this!):
# Python has a shortcut: the @contextmanager decorator from contextlib.
# Instead of a class with __enter__/__exit__, you write a generator function.
# Everything before `yield` is the setup (__enter__), everything after is teardown (__exit__).
#
# Rewrite your Timer from 5b as a context manager function using @contextmanager.
# Search: "contextlib contextmanager python"
#
# Your solution:
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        time_elapsed = end - start
        print(f"Elapsed: {time_elapsed:.4f}")


with timer() as t:
    sum(range(1_000_000))


# ---------------------------------------------------------------
# QUESTION 5d (stretch) — Suppressing exceptions:
# Context managers can swallow exceptions by returning True from __exit__.
# Write a context manager called `suppress_errors(*exception_types)` that:
# - Silently ignores any exceptions of the given types
# - Lets other exceptions through normally
#
# Usage:
#   with suppress_errors(ValueError, TypeError):
#       int("not a number")  # should NOT crash
#
#   with suppress_errors(ValueError):
#       raise KeyError("this should still crash")
#
# HINT: Check the exc_type argument in __exit__. If it's in exception_types, return True.
# BONUS: Python's standard library already has this — find it! (search: "contextlib suppress")
#
# Your solution:
class suppress_errors:
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exception_types:
            return True


with suppress_errors(ValueError, TypeError):
    int("not a number")

with suppress_errors(ValueError):
    raise KeyError("this should still crash")
