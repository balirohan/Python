import random

choices = ("rock", "paper", "scissors")
is_running = True
while is_running:
    computer = random.choice(choices)
    guess = input("Rock, Paper, or Scissors?: ").lower()
    if guess.isalpha() and guess in choices:
        if guess == "rock":
            if computer == "paper":
                print("YOU LOSE.")
            elif computer == "scissors":
                print("YOU WIN!")
            else:
                print("It's a draw.")
        elif guess == "paper":
            if computer == "rock":
                print("YOU WIN!")
            elif computer == "scissors":
                print("YOU LOSE.")
            else:
                print("It's a draw.")
        elif guess == "scissors":
            if computer == "rock":
                print("YOU LOSE.")
            elif computer == "paper":
                print("YOU WIN!")
            else:
                print("It's a draw.")
    else:
        print(f"{guess} is an invalid input.")
        continue
    print(f"Computer chose: {computer}, You chose: {guess}")
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        print("Hope you had fun!")
        is_running = False