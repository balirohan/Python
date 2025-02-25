import random

def roll():
    return random.randint(1, 6)

while True:
    num_players = input("How many players?: ")
    if num_players.isdigit():
        num_players = int(num_players)
        if  4 >= num_players >= 2:
            break
        else:
            print("Only 2-4 Players are allowed.")
    else:
        print("Please enter a valid number next time.")
        continue

max_score = 10
scores = [0 for _ in range(num_players)]

while max(scores) < max_score:
    for _ in range(num_players):
        print(f"Player {_+1}'s turn has started")
        print(f"Your total score so far is {scores[_]}")
        current_score = 0

        while True:
            ask = input("Would you like to roll? (y/n): ").lower()
            if ask.isalpha():
                if ask != "y":
                    break
            else:
                print("Please enter (y/n)")
                continue
            value = roll()
            if value == 1:
                print("You rolled a 1. Turn done!")
                current_score = 0
                break
            else:
                print(f"You rolled a {value}")
                current_score += value
            print(f"Your score is {current_score}")

        scores[_] += current_score
        print(f"Your total score is {scores[_]}")

max_score = max(scores)
winner = scores.index(max_score)
print(f"Player number {winner+1} is the winner with a total score of {max_score}")