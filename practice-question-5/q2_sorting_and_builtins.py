from collections import defaultdict

# ============================================================
# Q2: Sorting, min/max, and key functions
# ============================================================
# Python's sorted(), min(), max() all accept a `key` argument —
# a function applied to each element before comparison.
# This is more powerful than it sounds.
#
# ---------------------------------------------------------------
# QUESTION 2a:
# Sort this list of strings by LENGTH (shortest first),
# with alphabetical order as a tiebreaker.
#
words = ["banana", "fig", "apple", "kiwi", "date", "plum"]
#
# Expected output: ['fig', 'date', 'kiwi', 'plum', 'apple', 'banana']
#
# Your solution:
sorted_words_by_length = sorted(words, key=lambda word: (len(word), word))
print(sorted_words_by_length)


# ---------------------------------------------------------------
# QUESTION 2b:
# Given this list of dicts:
employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 95000},
    {"name": "Bob", "dept": "Marketing", "salary": 72000},
    {"name": "Carol", "dept": "Engineering", "salary": 110000},
    {"name": "Dave", "dept": "Marketing", "salary": 85000},
    {"name": "Eve", "dept": "Engineering", "salary": 72000},
]
#
# Sort by department (alphabetical), then by salary (highest first) within each dept.
# Print each employee's name and salary.
#
# Expected output:
# Carol - 110000
# Alice - 95000
# Eve - 72000
# Dave - 85000
# Bob - 72000
#
# Your solution:

sorted_employees = sorted(employees, key=lambda emp: (emp["dept"], -emp["salary"]))
for emp in sorted_employees:
    print(f'{emp["name"]} - {emp["salary"]}')
print(sorted_employees)

# ---------------------------------------------------------------
# QUESTION 2c:
# Find the employee with the highest salary using max().
# Do it in one line. No loops, no sorting.
#
# Your solution:

print(max(employees, key=lambda emp: emp["salary"])["name"])


# ---------------------------------------------------------------
# QUESTION 2d (stretch):
# Given this dict of city populations:
populations = {
    "Mumbai": 20_667_656,
    "Delhi": 32_941_000,
    "Chennai": 10_971_108,
    "Kolkata": 14_850_000,
    "Bangalore": 13_193_000,
}
#
# Return a NEW dict sorted by population descending.
# Expected: Delhi first, Mumbai second, ...
#
# Your solution:
