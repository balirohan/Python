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
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
            elif computer == "scissors":
                print("YOU WIN!")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
            else:
                print("It's a draw.")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
        elif guess == "paper":
            if computer == "rock":
                print("YOU WIN!")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
            elif computer == "scissors":
                print("YOU LOSE.")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
            else:
                print("It's a draw.")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
        elif guess == "scissor":
            if computer == "rock":
                print("YOU LOSE.")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
            elif computer == "paper":
                print("YOU WIN!")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
            else:
                print("It's a draw.")
                print(f"Computer chose: {computer}, You chose: {guess}")
                break
    else:
        print(f"{guess} is an invalid input.")
        continue
