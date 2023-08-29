"""Rock, Paper, Scissors"""
"""The classic hand game of luck."""

import random, time, sys

print(
    """Rock, Paper, Scissors game
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
 """
)

# These variables keep track of wins, losses and ties
wins = 0
loses = 0
ties = 0

while True:  # Main game loop
    while True:  # Keep asking until player enters R, P, S, or Q
        print("{} wins, {} loses, {} ties}".format(wins, loses, ties))
        print("Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit")
        player_move = input("> ").upper()
        if player_move == "Q":
            print("Thanks for playing")
            sys.exit()
        if player_move == "R" or player_move == "P" or player_move == "S":
            break
        else:
            print("Type one of R, P, S or Q")
