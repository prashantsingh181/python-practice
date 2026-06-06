def chunk_list(array, size):
    chunk = []
    result = []
    for item in array:
        chunk.append(item)
        if len(chunk) == size:
            result.append(chunk)
            chunk = []

    if len(chunk):
        result.append(chunk)

    return result


print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
