def most_frequent(numbers):
    freq_count = {}
    most_frequent = []
    for number in numbers:
        if freq_count.get(number):
            freq_count[number] += 1
            if freq_count[number] > freq_count[most_frequent[0]]:
                most_frequent.insert(0, number)
        else:
            freq_count[number] = 1
            most_frequent.append(number)

    return most_frequent[0]


print(most_frequent([1, 3, 2, 1, 4, 3, 1]))
