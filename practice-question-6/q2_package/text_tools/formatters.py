import re
# ============================================================
# Q2: text_tools/formatters.py
# ============================================================
# Implement these two functions.
# Both are used in main.py via the package's __init__.py.
# ============================================================

import re


def slugify(text: str) -> str:
    """
    Convert a string to a URL-friendly slug.
    - Lowercase everything
    - Replace spaces (and multiple spaces) with hyphens
    - Remove any character that is not alphanumeric or a hyphen

    slugify("Hello World")        → "hello-world"
    slugify("  Python is Great!") → "python-is-great"
    slugify("100% Organic!")      → "100-organic"
    """
    # Your implementation:
    striped_alphanum = re.sub(r'[^A-Za-z0-9\s]', '', text.strip().lower())
    return re.sub(r'\s+', '-', striped_alphanum)

if __name__ == "__main__":
    print(slugify("Hello World"))
    print(slugify("  Python is Great!"))
    print(slugify("100% Organic!"))

def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to max_length characters.
    If truncated, append suffix.
    If text fits, return it unchanged.

    truncate("Hello World", 8)         → "Hello..."
    truncate("Hi", 10)                 → "Hi"
    truncate("Hello World", 8, " →")   → "Hello →"
    """
    # Your implementation:
    # return text if len(text) < max_length
    return text if len(text) < max_length else text[:max_length - len(suffix)] + suffix

if __name__ == "__main__":
    print(truncate("Hello World", 8))
    print(truncate("Hi", 10))
    print(truncate("Hello World", 8, " →"))
