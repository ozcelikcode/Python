# Rock, Paper, Scissors Game

import random

options = ("rock", "paper", "scissors", "bismillah")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper or scissors): ")

    print(f"Player chose {player}")
    print(f"Computer chose {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "bismillah":
        print("Computer: God you bless bro, You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        running = False


print("Thanks for playing!")