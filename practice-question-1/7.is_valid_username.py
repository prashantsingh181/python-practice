def is_valid_username(username):
    passed = True
    if len(username) < 5 or len(username) > 20:
        passed = False
    if not username[0].isalpha():
        passed = False
    if username[-1] == "_":
        passed = False
    for char in username:
        if not char.isalpha() and not char.isdigit() and char != "_":
            passed = False
            break

    return passed


print(is_valid_username("john_doe"))
print(is_valid_username("_bad"))
