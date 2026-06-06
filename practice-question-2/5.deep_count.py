def deep_count(array):
    count = 0
    for item in array:
        if isinstance(item, list):
            count += deep_count(item)
        else:
            count += 1
    return count


print(deep_count([1, [2, 3], [4, [5, 6]]]))
