from functools import reduce


def process(numbers):
    if not isinstance(numbers, list):
        raise Exception("")

    odds = list(filter(lambda num: num % 2 != 0, numbers))
    odd_squares = list(map(lambda num: num**2, odds))
    odd_squares_total = reduce(lambda acc, num: acc + num, odd_squares)

    return odd_squares_total


print(process([1, 2, 3, 4, 5, 6, 7]))
