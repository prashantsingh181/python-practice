# ============================================================
# Q1: List & Dict Comprehensions
# ============================================================
# JS equivalent mindset: .map(), .filter(), .reduce()
# Python has a more readable built-in syntax for these.
#
# QUESTION 1a:
# Given this list of numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Using a LIST COMPREHENSION (not a loop, not map/filter):
# - Create a new list of squares of only the EVEN numbers.
# Expected output: [4, 16, 36, 64, 100]
#
# Your solution:
squares = [num**2 for num in numbers if num % 2 == 0]
print(squares)

# ---------------------------------------------------------------
# QUESTION 1b:
# Given this list of words:
words = ["hello", "world", "python", "is", "cool", "a", "great"]
#
# Using a LIST COMPREHENSION:
# - Create a new list of words that are longer than 3 characters,
#   but with each word TITLE-CASED.
# Expected output: ['Hello', 'World', 'Python', 'Cool', 'Great']
#
# Your solution:
title_long_words = [word.upper() for word in words if len(word) > 3]
print(title_long_words)

# ---------------------------------------------------------------
# QUESTION 1c:
# Given these two lists:
keys = ["name", "age", "city"]
values = ["Alice", 30, "Mumbai"]
#
# Using a DICT COMPREHENSION:
# - Combine them into a single dictionary.
# Expected output: {'name': 'Alice', 'age': 30, 'city': 'Mumbai'}
#
# HINT: Look up the zip() built-in function — it pairs two iterables together.
# In JS you'd probably use keys.map((k, i) => ...) with index. Python has a better way.
#
# Your solution:
zipped_key_values = list(zip(keys, values))
dictionary = {pair[0]: pair[1] for pair in zipped_key_values}
print(dictionary)

# ---------------------------------------------------------------
# QUESTION 1d (stretch):
# Given this sentence:
sentence = "the quick brown fox jumps over the lazy dog"
#
# Using a DICT COMPREHENSION:
# - Build a dict where each key is a unique word and the value
#   is the length of that word. Skip words shorter than 4 characters.
# Expected output: {'quick': 5, 'brown': 5, 'jumps': 5, 'over': 4, 'lazy': 4}
#
# Your solution:
words_length_dict = {word: len(word) for word in sentence.split() if len(word) > 3}
print(words_length_dict)
