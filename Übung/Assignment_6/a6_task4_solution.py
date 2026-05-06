"""
Implements a simple guessing game.
"""

import random

lower_bound = int(input("Please enter the lower interval bound: "))
upper_bound = int(input("Please enter the upper interval bound: "))

number_to_guess = random.randint(lower_bound, upper_bound)

number_of_guesses = 5

print(f"You have {number_of_guesses} guesses.")

guessed = False # Used to set the print-statement for the user
for i in range(number_of_guesses):

    guess = int(input("Please enter your guess: "))

    if guess == number_to_guess:
        guessed = True 
        break
    else:
        guessed = False
        if guess > number_to_guess:
            print("Your guess is larger than the hidden number.")
        else:
            print("Your number is smaller than the number to guess")

if guessed:
    print("Nice! You guessed the hidden number!")
else:
    print("Better luck next time...")