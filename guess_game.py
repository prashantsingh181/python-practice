from random import randint
from sys import argv

try:
    start = int(argv[1]) or 1
except ValueError:
    start = 1

try:
    stop = int(argv[2]) or 10
except ValueError:
    stop = 10

answer = randint(start, stop + 1)
times_tried = 1

while True:
    try:
        if times_tried == 1:
            guess = int(input(f"Guess a number between {start} and {stop}.\n"))
        else:
            guess = int(input("Guess again.\n"))

        if guess == answer:
            print(f"Correct! The number was {answer}.")
            break
        elif guess < start or guess > stop:
            print(f"Please guess a number between {start} and {stop}")
        elif guess < answer:
            print("The number is higher that this.")
        else:
            print("The number is lower than this.")
        times_tried += 1

    except ValueError:
        print("Please enter integer only!")
        continue
