from itertools import chain, islice, takewhile, dropwhile, zip_longest, groupby
from functools import reduce

# ============================================================
# Q5: itertools — the generator toolkit
# ============================================================
# itertools gives you composable, memory-efficient tools for
# working with iterables. Since you now understand generators,
# these will make sense immediately.
#
# You'll explore: chain, islice, takewhile, dropwhile, groupby, zip_longest
# Import what you need from itertools.
#
# ---------------------------------------------------------------
# QUESTION 5a — chain:
# Combine these three lists into a single iterable WITHOUT
# creating a new combined list in memory. Print each item.
#
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = [7, 8, 9]
#
# Expected output: 1 2 3 4 5 6 7 8 9 (each on own line)
#
# Your solution:

combined_list = chain(list_a, list_b, list_c)
print(list(combined_list))


# ---------------------------------------------------------------
# QUESTION 5b — islice:
# islice(iterable, stop) works like slicing but on any iterator.
# Use your `integers_from` generator from Q4 of the previous set
# (or rewrite it here) combined with islice to print the first
# 5 even numbers starting from 0.
#
# Expected: 0 2 4 6 8
#
# Your solution:


def integers_from(start):
    current = start
    while True:
        yield current
        current += 1


integers_from_zero = integers_from(0)

evens = islice(integers_from_zero, 0, 10, 2)
print(list(evens))

# ---------------------------------------------------------------
# QUESTION 5c — takewhile / dropwhile:
# Given:
numbers = [2, 4, 6, 7, 8, 10, 11, 12]
#
# 1. Use takewhile to get numbers while they're even. (stops at 7)
#    Expected: [2, 4, 6]
#
# 2. Use dropwhile to skip numbers while they're even, then take the rest.
#    Expected: [7, 8, 10, 11, 12]
#
# Your solution:

starting_evens = takewhile(lambda num: num % 2 == 0, numbers)
print(list(starting_evens))

exclude_starting_evens = dropwhile(lambda num: num % 2 == 0, numbers)
print(list(exclude_starting_evens))

# ---------------------------------------------------------------
# QUESTION 5d — zip_longest:
# Regular zip() stops at the shortest iterable.
# zip_longest fills missing values with a fillvalue.
#
# Given:
names = ["Alice", "Bob", "Carol"]
scores = [88, 92]
#
# Pair them up, filling missing scores with 0.
# Expected: [('Alice', 88), ('Bob', 92), ('Carol', 0)]
#
# Your solution:

students_score = zip_longest(names, scores, fillvalue=0)
print(list(students_score))


# ---------------------------------------------------------------
# QUESTION 5e (stretch) — groupby:
# groupby(iterable, key) groups CONSECUTIVE elements by a key.
# IMPORTANT: the input must be sorted by the key first, or groups won't work right.
#
# Given:
transactions = [
    {"type": "credit", "amount": 100},
    {"type": "credit", "amount": 250},
    {"type": "debit", "amount": 50},
    {"type": "debit", "amount": 75},
    {"type": "credit", "amount": 300},
]
#
# Group by "type" and print the total amount per type:
# Expected:
# credit: 650
# debit: 125
#
# Your solution:
sorted_transactions = sorted(transactions, key=lambda tr: tr["type"])
grouped_transactions = groupby(sorted_transactions, key=lambda tr: tr["type"])

for group in grouped_transactions:
    group_sum = reduce(lambda acc, item: acc + item["amount"], list(group[1]), 0)
    print(f"{group[0]}: {group_sum}")
