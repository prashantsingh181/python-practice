def caesar_cipher(string, shift):
    result = ""
    for char in string:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            ascii_after_shift = (ord(char) - base + shift) % 26 + base
            result += chr(ascii_after_shift)
        else:
            result += char

    return result


print(caesar_cipher("hello", 3))
print(caesar_cipher("xyz", 2))
