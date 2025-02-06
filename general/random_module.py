import random

# print(help(random))

low = 1
high = 100

# print(random.randint(low, high))
# print(random.random())

options = ("rock", "paper", "scissors")
# print(random.choice(options))

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards)
# print(cards)