# ============================================================
# Q4: Generators & Iterators
# ============================================================
# JS equivalent: Generator functions (function*), iterators, Symbol.iterator
# Python's generators are similar syntax but used far more commonly
# in everyday Python code (including in standard library).
#
# Key idea: a generator function uses `yield` instead of `return`.
# It produces values one at a time — lazily — instead of building a full list.
#
# QUESTION 4a — Basic generator:
# Write a generator function called `countdown(n)` that:
# - Yields numbers from n down to 1
#
# Then use it in a for loop to print: 5 4 3 2 1 (each on own line)
#
# Your solution:
def countdown(n):
    for i in range(n, 0, -1):
        yield i


for count in countdown(5):
    print(count)


# ---------------------------------------------------------------
# QUESTION 4b — Infinite generator:
# Write a generator called `integers_from(start)` that:
# - Yields integers starting from `start`, incrementing forever
#
# Then use `next()` to manually get the first 3 values from integers_from(10)
# Expected: 10, 11, 12
#
# HINT: An infinite while True loop inside a generator is safe — it only
#       advances when next() is called. There's no blocking.
#
# Your solution:
def integers_from(start):
    current = start
    while True:
        yield current
        current += 1


integers = integers_from(10)
print(next(integers))
print(next(integers))
print(next(integers))

# ---------------------------------------------------------------
# QUESTION 4c — Generator expression (search this!):
# Just like list comprehensions, Python has GENERATOR EXPRESSIONS.
# They look almost identical but use () instead of [].
#
# Given:
import sys

big_list = list(range(1_000_000))
#
# 1. Create a list comprehension that squares all numbers: squares_list = [...]
# 2. Create a generator expression that does the same: squares_gen = (...)
# 3. Print sys.getsizeof() for both. What do you notice about the sizes?
# 4. Add a comment explaining WHY there's a difference.
#
# Your solution:
squares_list = [item**2 for item in big_list]
squares_gen = (item**2 for item in big_list)
print(f"Size of squares_list: {sys.getsizeof(squares_list)}")
print(f"Size of squares_gen: {sys.getsizeof(squares_gen)}")
# There is a massive difference in the sizes of squares_list and squares_gen
# that is because the list comprehension that created the squares_list
# generates the entire list and store it in the memory, while the generator
# expression only creates the memory for generator object that when called
# with next gives the next value


# ---------------------------------------------------------------
# QUESTION 4d — Practical generator:
# Write a generator called `read_in_chunks(text, chunk_size)` that:
# - Takes a long string and a chunk_size integer
# - Yields successive chunks of that string
#
# Example:
#   for chunk in read_in_chunks("Hello World", 3):
#       print(chunk)
# Output:
#   Hel
#   lo
#    Wo
#   rld
#
# HINT: Think about string slicing in a loop. When should the loop stop?
#
# Your solution:
def read_in_chunks(text, size):
    length = len(text)
    starting_index = 0

    while starting_index < length:
        ending_index = starting_index + size
        actual_ending_index = ending_index if ending_index <= length else length
        yield text[starting_index:actual_ending_index]
        starting_index = ending_index


for chunk in read_in_chunks("Hello World", 3):
    print(chunk)

# ---------------------------------------------------------------
# QUESTION 4e (stretch) — yield from (search this!):
# Python has a `yield from` syntax for delegating to another iterable.
# Rewrite this function using `yield from` instead of the for loop:


def flatten_bad(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item


# Your version using yield from:
def flatten(nested_list):
    for sublist in nested_list:
        yield from sublist


#
# Test: list(flatten([[1,2], [3,4], [5]])) should give [1, 2, 3, 4, 5]
print(list(flatten([[1, 2], [3, 4], [5]])))
