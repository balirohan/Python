import random

lowest_num = 1
highest_num = 100
guesses = 0
is_running = True

print()
print("----------------------------")
print("Python Number Guessing Game!")
print("----------------------------")
print(f"Select a number between {lowest_num} & {highest_num}")

while is_running:
    answer = random.randint(lowest_num, highest_num)
    ask = input(f"Enter a number between {lowest_num} & {highest_num} (q to quit): ").lower()
    if ask.isdigit() and highest_num >= int(ask) >= lowest_num:
        if int(ask) == answer:
            print("WOHOO! YOU WIN!")
            break
        else:
            print("Incorrest Guess :(")
            print(f"Your Guess: {ask}, Random Number: {answer}")
            guesses += 1
            continue
    elif ask == "q":
            print("Better luck next time!")
            print(f"You guessed {guesses} times")
            break
    else:
        print(f"{ask} is not a valid number")
        ask = input(f"Please select a number between {lowest_num} & {highest_num}: ")
        continue

if not ask == "q":
    print(f"You got it right in {guesses} guesses!")