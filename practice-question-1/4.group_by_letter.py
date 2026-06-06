def group_by_letter(words):
    grouping = {}
    for word in words:
        first_char = word[0]
        if grouping.get(first_char) is not None:
            grouping[first_char].append(word)
        else:
            grouping[first_char] = [word]

    return grouping


print(group_by_letter(["apple", "avocado", "banana"]))
