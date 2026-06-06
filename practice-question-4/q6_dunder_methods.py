# ============================================================
# Q6: Dunder (Magic) Methods — Python's Data Model
# ============================================================
# JS equivalent: Overriding toString(), Symbol.iterator, Symbol.toPrimitive,
#                Proxy traps
# Python lets you define how your objects behave with operators, built-ins,
# and iteration by implementing special __dunder__ methods.
#
# This is one of the most "Pythonic" things that has no clean JS parallel.
#
# QUESTION 6a — __repr__ and __str__:
# JS equivalent: toString()
# __str__ is the human-readable version (used by print())
# __repr__ is the developer/debug version (used in REPL, logs)
#
# Given this class, add __repr__ and __str__ methods:
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Add __str__: should return "'{title}' by {author}"
    # Add __repr__: should return "Book(title='{title}', author='{author}', pages={pages})"
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"


# Test:
b = Book("Clean Code", "Robert Martin", 431)
print(str(b))  # 'Clean Code' by Robert Martin
print(repr(b))  # Book(title='Clean Code', author='Robert Martin', pages=431)


# ---------------------------------------------------------------
# QUESTION 6b — __len__ and __getitem__:
# These let your object work with len() and [] indexing.
#
# Create a class called `Playlist` that:
# - Takes a list of song names in __init__
# - Implements __len__ so len(playlist) works
# - Implements __getitem__ so playlist[0] works
# - BONUS: If __getitem__ works correctly, Python's for loop will also work on it
#          (try iterating over it — you shouldn't need __iter__!)
#
# Your solution:
class Playlist:
    def __init__(self, song_list):
        self.song_list = song_list

    def __len__(self):
        return len(self.song_list)

    def __getitem__(self, index):
        return self.song_list[index]


playlist = Playlist(["Roar", "Fireworks", "Mummy"])
print(len(playlist))
print(playlist[0])
for song in playlist:
    print(song)

# ---------------------------------------------------------------
# QUESTION 6c — __add__ and __eq__ (operator overloading):
# JS equivalent: You can't do this cleanly in JS (no operator overloading).
#
# Create a class called `Vector` that represents a 2D vector (x, y).
# - __add__: v1 + v2 should add components: Vector(1,2) + Vector(3,4) = Vector(4,6)
# - __eq__: v1 == v2 should compare components: Vector(1,2) == Vector(1,2) → True
# - __repr__: should return "Vector(x, y)"
#
# Your solution:


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("both operands should be vector type")
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("both operands shoule be Vector")
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


vector1 = Vector(2, 3)
vector2 = Vector(3, 4)
print(vector1 + vector2)
print(vector1 == vector2)


# ---------------------------------------------------------------
# QUESTION 6d — __call__ (callable objects):
# JS equivalent: Classes with a default invoke behavior don't exist,
#               but think of it like making an object behave as a function.
#
# Create a class called `Multiplier` that:
# - Takes a factor in __init__
# - Implements __call__ so the object can be called like a function
#
# Usage:
#   double = Multiplier(2)
#   triple = Multiplier(3)
#   double(5)   # returns 10
#   triple(5)   # returns 15
#   double(triple(4))  # returns 24
#
# Your solution:
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return num * self.factor


double = Multiplier(2)
triple = Multiplier(3)
print(double(5))
print(triple(5))


# ---------------------------------------------------------------
# QUESTION 6e (stretch) — __contains__ and __iter__:
# Add to your Playlist class from 6b:
# - __contains__: so `"Blinding Lights" in playlist` works
# - __iter__: explicit iterator using iter() on your internal list
#             (this is cleaner than relying on __getitem__ for iteration)
#
# Test:
#   p = Playlist(["Song A", "Song B", "Song C"])
#   print("Song A" in p)   # True
#   print("Song D" in p)   # False
#   for song in p: print(song)
#
# Your solution (modify/extend your Playlist class above):
class PlaylistExtended(Playlist):
    def __contains__(self, item):
        return item in self.song_list

    def __iter__(self):
        return iter(self.song_list)


p = Playlist(["Song A", "Song B", "Song C"])
print("Song A" in p)
print("Song D" in p)
for song in p:
    print(song)
