# Lab 1
# Group 8
# Author: Gislaine Pires
# Date: 09/27/2026

# Imported both games
from guessing import guessing_game
from rps import play_rock_paper_scissors


# Created the main() function
def main():
    # Display the game menu and allow the user to choose and play either game.

    # Make sure the user can play multiple games, multiple times
    play_again = "y"

    # Added the menu
    while play_again == "y":
        print("\nWhich game do you want to play?")
        print("1. Guessing Game")
        print("2. Rock-Paper-Scissors")

        # Checked for invalid input
        choice = input("Enter your choice (1 or 2): ").strip()

        while choice != "1" and choice != "2":
            print("Please enter 1 or 2.")
            choice = input("Enter your choice (1 or 2): ").strip()

        # Called the appropriate game
        if choice == "1":
            guessing_game()
        else:
            play_rock_paper_scissors()

        play_again = input(
            "\nDo you want to play again or switch games? (Y/N): "
        ).strip().lower()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
