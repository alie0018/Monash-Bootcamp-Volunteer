from __future__ import annotations

import random

"""
Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.
"""

def number_guesser() -> None:
    """
    A function that will run a random number guesser game between 1 and 100.
    Hints will be given to the user whether their guess was lower or higher than the target number.
    Prints a sticker if the user manages to guess the correct number for extra fun.

    :return: None
    """
    # use the random module to generate a random number within a certain range
    target = random.randint(1, 100)  # in this case we are generating a random number between 1 and 100
    
    # Initialize the guess variable into None
    guess = None  # doesn't really matter since we are going to overwrite the guess variable
    
    # We are using a while loop since we don't know when the user going to guess correctly
    while guess != target:
        # Since we will get a ValueError when the user tries to input a string instead of an integer,
        # we are using the try exception to catch the exception
        try:
            # we wanted the user to input an integer
            guess = int(input("Please guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100")
            continue  # this will continue the loop

        # check if the user guessed the correct number and end the loop.
        if guess == target:
            print("Congratulation, your guess was correct!")
        # check if the user guessed number is higher than the target
        elif guess > target:
            print("Your guess was higher than the target")
        # check if the user guessed number is lower than the target
        elif guess < target:
            print("Your guess was lower than the target")


if __name__ == "__main__":
    number_guesser()
