# Author: CAM (AMDG) 12/11/2020

# Imports
from random import randint


# Functions
def rock_paper_scissors():
    """Play rock paper scissors"""
    player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
    computer = randint(0, 2)

    # Check if the user or the computer won.
    if player == computer:
        print("It's a tie!")
        return "tie"
    elif player == 0:
        if computer == 1:
            print("You lose, paper covers rock.\n")
            return "loss"
        else:
            print("You win, rock crushes scissors!\n")
            return "win"
    elif player == 1:
        if computer == 2:
            print("You lose, scissors cuts paper.\n")
            return "loss"
        else:
            print("You win, paper covers rock!\n")
            return "win"
    elif player == 2:
        if computer == 0:
            print("You lose, rock crushes scissors.\n")
            return "loss"
        else:
            print("You win, scissors cuts paper!\n")
            return "win"


# Counters
games = 0
won = 0
lost = 0
tied = 0

# Keep playing until user chooses to stop playing.
while True:
    play = input("Would you like to play rock, paper, scissors? (Y/N): ")
    if play.upper() == "Y":
        result = rock_paper_scissors()
        if result == "win":
            won += 1
            games += 1
        elif result == "loss":
            lost += 1
            games += 1
        elif result == "tie":
            tied += 1
            games += 1
    elif play.upper() == "N":
        break
    else:
        print("You did not enter Y or N.")
        continue

print("You played {0} game(s) and won {1} time(s), lost {2} time(s), and tied {3} time(s).".format(games, won, lost, tied))

