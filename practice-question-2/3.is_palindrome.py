def is_palindrome(string):
    modified = "".join(c for c in string.lower() if c.isalnum)
    return modified[::-1] == modified


print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))
