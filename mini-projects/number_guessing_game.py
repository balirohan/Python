import random

lowest_num = 1
highest_num = 100
guesses = 0
is_running = True

print("Python Number Guessing Game!")
print(f"Select a number between {lowest_num} & {highest_num}")

while is_running:
    answer = random.randint(lowest_num, highest_num)
    ask = input(f"Enter a number between {lowest_num} & {highest_num}: ")
    if ask.isdigit() and 100 >= int(ask) >= 1:
        if int(ask) == answer:
            print("WOHOO! YOU WIN!")
            break
        else:
            print("Incorrest Guess :(")
            print(f"Your Guess: {ask}, Random Number: {answer}")
            guesses += 1
            continue
    else:
        print(f"{ask} is not a valid number")
        ask = input(f"Please select a number between {lowest_num} & {highest_num}: ")
        continue

print(f"You got it right in {guesses} guesses!")