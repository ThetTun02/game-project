# Lab 1
# Group 8
# Author: Thet Tun
#Date: 09/25/2026

import random

def play_rock_paper_scissors():
    """play rock paper scissor against computer.
Compare player's choice with computer's random choice.
And print whether player wins, loses, or ties."""

    player = input("Enter your choice: 1. paper, 2. scissors, 3. rock  ")
    while player != "1" and player != "2" and player != "3":
        print("Please enter 1, 2, or 3")
        player = input("Enter your choice: 1. paper, 2. scissors, 3. rock: ")

    computer = random.randint(1, 3)
    if (player == "1" and computer == 1) or (player == "2" and computer == 2) or (player == "3" and computer == 3):
        print ("It's a tie!")
    elif (player == "1" and computer == 3) or (player == "2" and computer == 1) or (player == "3" and computer == 2):
        print ("You Win!")
    else:
        print ("You Lose!")

if __name__== "__main__":
    answer = input("Do you want to play? (Y/N): ")
    while answer == "Y" or answer == "y":
        play_rock_paper_scissors()
        answer = input ("Do you want to play again? (Y/N)")