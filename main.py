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

    # Display what the player chose:
    if player_move == "R":
        print("Rock versus...")
        player_move = "Rock"
    elif player_move == "P":
        print("Paper versus...")
        player_move = "Paper"
    elif player_move == "S":
        print("Scissors versus...")
        player_move = "Scissors"

    # Count to three with dramatic pauses
    time.sleep(0.5)
    print("1...")
    time.sleep(0.25)
    print("2...")
    time.sleep(0.25)
    print("3...")
