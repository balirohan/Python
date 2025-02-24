import random

upper_limit = input("Enter a number: ")

if upper_limit.isdigit():
    upper_limit = int(upper_limit)
    if upper_limit <= 0:
        print(f"Please enter a number larger than {upper_limit} next time.")
        quit()
else:
    print(f"Please enter a positive number next time. {upper_limit} is not a valid number")
    quit()

random_number = random.randint(0, upper_limit)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got it")
        break

    elif user_guess > random_number:
        print("You were above the number.")

    elif user_guess < random_number:
        print("You were below the number.")

print("You got it in", guesses, "guesses")