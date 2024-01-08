# Challenge 6: Guess the Number
# Generate a random number between 1 and 10. Ask the user to guess the number
# and provide feedback on whether the guess is too high, too low, or correct.

"""
# Chat GPT 3.5 code below:
import random

# generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# initialize variables
attempts = 0
max_attempts = 3  # set the max number of guesses

while True:
    # ask the user to guess the number
    guess = int(input('Guess a number (between 1 and 10): '))

    # increment the attempts counter
    attempts += 1

    # check if the guess is correct
    if guess == secret_number:
        print(f'Congratulations! You guessed the number {secret_number} in {attempts} attempts.')
        break
    else:
        print('Incorrect. Try again.')

    # check if the user has run out of guesses
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number is {secret_number}.")
        break
"""


# Kylie Ying's code below:

import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f"Yayy!! You've guessed the number {random_number}")

guess(10)
