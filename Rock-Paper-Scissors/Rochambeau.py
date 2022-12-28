import random

options = ("Rock", "Paper", "Scissors")

player = None

running = True

while running:

    computer = random.choice(options)

    print("\n_______________________________________________________")

    player = input("\nEnter an Option (Rock, Paper, Scissors) : ").capitalize()

    while player not in options:
        print("!!ERROR!! : Invalid Input")
        player = input("\nEnter an Option again (Rock, Paper, Scissors) : ").capitalize()

    print("\n==================")
    print(f"Player : {player}")
    print(f"Computer : {computer}")
    print("==================")

    if player == "Rock" and computer == "Scissors" or player == "Scissors" and computer == "Paper" or player == "Paper"\
            and computer == "Rock":
        print("\nYou WIN!")

    elif computer == "Rock" and player == "Scissors" or computer == "Scissors" and player == "Paper" or computer == \
            "Paper" and player == "Rock":
        print("\nYou LOSE!")

    elif player == computer:
        print("\nIt's TIE!")

    else:
        print("!!ERROR!! : Unknown Error")

    if not input("\nPlay again?(y/N) : ").lower() == "y":
        running = False
