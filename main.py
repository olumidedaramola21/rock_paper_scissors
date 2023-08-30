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
        print("{} wins, {} loses, {} ties".format(wins, loses, ties))
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

    # Display what the computer chose:
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = "Rock"
    elif random_number == 2:
        computer_move = "Paper"
    elif random_number == 3:
        computer_move = "Scissors"
    print(computer_move)
    time.sleep(0.25)

    # Display and record win/loss/tie
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == "Rock" and computer_move == "Scissors":
        print("You win!")
        wins += 1
    elif player_move == "Paper" and computer_move == "Rock":
        print("You win!")
        wins += 1
    elif player_move == "Scissors" and computer_move == "Paper":
        print("You win!")
        wins += 1
    elif player_move == "Scissors" and computer_move == "Rock":
        print("You lose!")
        loses += 1
    elif player_move == "Rock" and computer_move == "Paper":
        print("You lose!")
        loses += 1
    elif player_move == "Paper" and computer_move == "Scissors":
        print("You lose!")
        loses += 1
