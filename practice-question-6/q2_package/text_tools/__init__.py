# ============================================================
# Q2: Building a Package
# ============================================================
# This folder (text_tools/) is a PACKAGE.
# It has two modules inside: formatters.py and validators.py
#
# TASK: Configure this __init__.py so that users of the package
#       can import like this (from main.py):
#
#   from text_tools import slugify, truncate, is_email, is_url
#
#       instead of having to write:
#
#   from text_tools.formatters import slugify, truncate
#   from text_tools.validators import is_email, is_url
#
# This is called "re-exporting" — you surface the public API here.
# Hint: use relative imports (from .formatters import ...)
#
# Also define __all__ listing the four public names.
#
# Your solution:
from .formatters import slugify, truncate
from .validators import is_email, is_url

__all__ = ["slugify", "truncate", "is_email", "is_url"]