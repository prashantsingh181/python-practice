def find_duplicates(numbers):
    duplicates = []
    freq_counter = {}
    for number in numbers:
        freq_counter[number] = freq_counter.get(number, 0) + 1
        if freq_counter[number] == 2:
            duplicates.append(number)

    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
