def flatten(array):
    result = []

    def flatten_helper(array):
        nonlocal result
        for item in array:
            if isinstance(item, list):
                flatten_helper(item)
            else:
                result.append(item)

    flatten_helper(array)
    return result


print(flatten([[1, 2], [3, [2, 5, [1, 2]]], [5]]))
