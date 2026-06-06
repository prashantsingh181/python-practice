from dataclasses import dataclass, field
from typing import Any, Callable, TypedDict

# ============================================================
# Q6: Type Hints
# ============================================================
# As a TypeScript developer, this will feel familiar — Python's
# type hints are annotations that don't enforce anything at runtime
# but power IDEs, linters (mypy), and documentation.
#
# Key difference from TS: hints are OPTIONAL and IGNORED at runtime.
# Python won't raise an error if you pass the wrong type — but mypy will.
#
# from typing import Optional, Union, Any
# In Python 3.10+: use `int | str` instead of Union[int, str]
# In Python 3.9+: use `list[int]` instead of List[int]
#
# ---------------------------------------------------------------
# QUESTION 6a — Annotate these functions:
# Add type hints to the parameters and return types.
# Do NOT change the function bodies.


def repeat_string(s: str, n: int) -> str:
    return s * n


def first_or_default(items: list[Any], default: Any) -> Any:
    return items[0] if items else default


def merge_dicts(d1: dict, d2: dict) -> dict:
    return {**d1, **d2}


# ---------------------------------------------------------------
# QUESTION 6b — Optional and Union:
# `Optional[X]` means the value can be X or None.
# `Union[X, Y]` means X or Y.
#
# Add type hints to these:


def find_user(user_id: int) -> dict | None:
    # Returns a dict if found, None if not found
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)


def stringify(value: int | float) -> str:
    # Accepts int or float, returns str
    return str(value)


# ---------------------------------------------------------------
# QUESTION 6c — Typed dataclass:
# Rewrite this plain class as a typed dataclass.
# Every field should have a type annotation.


class Config:
    def __init__(self):
        self.host = "localhost"
        self.port = 8080
        self.debug = False
        self.allowed_origins = ["http://localhost:3000"]


# Your solution:


@dataclass
class NewConfig:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False
    allower_origins: list[str] = field(
        default_factory=lambda: ["http://localhost:3000"]
    )


# ---------------------------------------------------------------
# QUESTION 6d — Callable type hint:
# Python can type-hint functions that accept other functions as arguments.
# from typing import Callable
#
# Write a function `apply_twice(fn, value)` that:
# - Takes a function fn and a value
# - Applies fn to value twice: fn(fn(value))
# - Has complete type hints (fn takes an int and returns an int, value is int, return is int)
#
# Example: apply_twice(lambda x: x * 2, 3) → 12
#
# Your solution:
def apply_twice(fn: Callable[[int], int], value: int) -> int:
    return fn(fn(value))


# ---------------------------------------------------------------
# QUESTION 6e (stretch) — TypedDict:
# TypedDict lets you type-hint dictionary shapes — like TS interfaces for dicts.
# from typing import TypedDict
#
# Define a TypedDict called `Movie` with fields:
#   title: str, year: int, rating: float
#
# Then write a function `format_movie(movie: Movie) -> str` that returns:
#   "The Matrix (1999) ★ 8.7"
#
# Your solution:
class Movie(TypedDict):
    title: str
    year: int
    rating: float


movie: Movie = {"title": "The Matrix", "year": 1999, "rating": 8.7}


def format_movie(movie: Movie) -> str:
    return f'{movie["title"]} ({movie["year"]}) * {movie["rating"]}'


print(format_movie(movie))
