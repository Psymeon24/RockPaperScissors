# Python program to create Rock, Paper, and scissors game

import random


class Play_again:
    @classmethod
    def lower(cls):
        pass


Yes = "y"


class End:
    pass


No = "n"

Restart = Yes != "y"

while True:

    # initiating user action
    player = input("Enter a choice ( R=rock, P=paper, S=scissors):")
    possible_actions = ["rock", "paper", "scissors"]

    # initiating the choice function
    CPU = random.choice(possible_actions)
    print(f"\nplayer {player}, CPU {CPU}.\n")

    if player == CPU:
        print(f"Both players selected {player}. it's a tie!")
    elif player == "rock":
        if CPU == "paper":
            print("rock smashes paper! Game won!")
    else:
        print("paper covers rock! Game lost!")

    Restart = "Play_again? (y/n): "
    if Play_again.lower() != "y":
        break
