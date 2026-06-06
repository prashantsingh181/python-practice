from collections import Counter, defaultdict, namedtuple

# ============================================================
# Q1: The collections module
# ============================================================
# Python's `collections` module has data structures that solve
# problems you'd normally reach for a custom class or verbose
# dict manipulation to handle.
#
# You'll use: Counter, defaultdict, namedtuple
# Import what you need as you go.
#
# ---------------------------------------------------------------
# QUESTION 1a — Counter:
# Given this list of words:
words = [
    "apple",
    "banana",
    "apple",
    "cherry",
    "banana",
    "apple",
    "date",
    "cherry",
    "banana",
    "apple",
]

#
# Using Counter:
# 1. Find the 2 most common words and their counts.
# 2. Print them in the format: "apple: 4, banana: 3"
#
# Expected output: apple: 4, banana: 3
#
# Your solution:
words_counter = Counter(words)
two_most_common = words_counter.most_common(2)
formatted_two_most_common = [f"{word}: {count}" for word, count in two_most_common]
print(", ".join(formatted_two_most_common))

# ---------------------------------------------------------------
# QUESTION 1b — defaultdict:
# Given this list of (student, subject) tuples:
enrollments = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "English"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "Science"),
]
#
# Using defaultdict, group subjects by student so you get:
# {'Alice': ['Math', 'English', 'Science'], 'Bob': ['Science', 'Math'], 'Charlie': ['Math']}
#
# Do NOT use setdefault() or check if the key exists manually.
#
# Your solution:
student_subjects = defaultdict(list)

for student, subject in enrollments:
    student_subjects[student].append(subject)

print(student_subjects)

# ---------------------------------------------------------------
# QUESTION 1c — namedtuple:
# Create a namedtuple called `Point3D` with fields x, y, z.
# Then:
# 1. Create a point at (1, 2, 3)
# 2. Access its fields by name (not by index)
# 3. Try to sasign p.x = 10. What happens? Add a comment explaining why.
#
# Your solution:
Point3D = namedtuple("Point3D", ["x", "y", "z"])
point = Point3D(1, 2, 3)
print(point.x, point.y, point.z)
# point.x = 10
print(point)

# setting point.x gives Attribute Error because named tuple is a subclass of
# tuple and is supposed to be immutable, hence we cannot set attributes

# ---------------------------------------------------------------
# QUESTION 1d (stretch):
# You have this raw text:
text = "to be or not to be that is the question"
#
# Using Counter on the words, find every word that appears more than once.
# Print them sorted alphabetically.
# Expected output: ['be', 'to']
#
# Your solution:
text_count = Counter(text.split())
sorted_repeated_text = sorted([item for item in text_count if text_count[item] > 1])

print(sorted_repeated_text)
