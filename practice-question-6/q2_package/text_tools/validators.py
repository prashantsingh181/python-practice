# ============================================================
# Q2: text_tools/validators.py
# ============================================================
# Implement these two functions.
# Use the `re` module for pattern matching.
# ============================================================

import re


def is_email(value: str) -> bool:
    """
    Return True if value looks like a valid email address.
    A valid email has: local@domain.tld
    - local: one or more alphanumeric/underscore/dot/hyphen chars
    - domain: one or more alphanumeric/hyphen chars
    - tld: 2-6 alphabetic characters

    is_email("user@example.com")   → True
    is_email("bad@")               → False
    is_email("nodomain")           → False
    is_email("a@b.io")             → True
    """
    # Your implementation:
    return bool(re.fullmatch(r"[\w\.\-]+@[a-zA-Z\-]+\.[a-zA-Z]{2,6}", value))


def is_url(value: str) -> bool:
    """
    Return True if value is a URL starting with http:// or https://
    followed by at least one more character.

    is_url("https://google.com")  → True
    is_url("http://x.io")         → True
    is_url("ftp://nope.com")      → False
    is_url("not a url")           → False
    """
    # Your implementation:
    return bool(re.search(r"^https?://.+", value))


if __name__ == "__main__":
    print(is_email("user@example.com"))
    print(is_email("bad@"))
    print(is_email("nodomain"))
    print(is_email("a@b.io"))
    print(is_url("https://google.com"))
    print(is_url("http://x.io"))
    print(is_url("ftp://nope.com"))
    print(is_url("not a url"))
