# Lab 1
# Group 8
# Author: Zhaochun Fu (Rory)
# Date: 09/27/2026

import random


def guessing_game():
    """Take a random number between 1 and 100. Play a five tries guessing game and ask to play again.

    Show the tries left and tell the player if each guess is too low or
    too high. Show the number after a loss, then ask to play again.
    """
    play_again = "y"

    while play_again == "y":
        number = random.randint(1, 100)
        print("Hello! I'm thinking of a number between 1 and 100.")

        for attempt in range(5):
            tries_left = 5 - attempt
            word = "try" if tries_left == 1 else "tries"
            guess = int(input(f"Guess what it is ({tries_left} {word} left): "))

            if guess == number:
                print("You got it! You won!")
                break
            elif attempt == 4:
                print(f"Sorry! You lost. The number was {number}.")
            elif guess < number:
                print("Sorry! Too low. Try again.")
            else:
                print("Sorry! Too high. Try again.")

        play_again = input("Do you want to play again? (Y/N): ").strip().lower()

    print("Thanks for playing!")


if __name__ == "__main__":
    guessing_game()
