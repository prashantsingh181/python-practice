def rle_encode(string):
    count = 0
    result = ""
    for i in range(len(string)):
        count += 1
        if i == len(string) - 1 or string[i + 1] != string[i]:
            result += f"{count}{string[i]}"
            count = 0
    return result


def rle_decode(string):
    result = ""
    for i in range(0, len(string), 2):
        digit = int(string[i])
        char = string[i + 1]
        result += digit * char
    return result


print(rle_encode("aaabbbccddddee"))
print(rle_decode("3a3b2c4d2e"))
