# Concession Stand Program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print()
print("----------- MENU -----------")
for key, value in menu.items():
    print(f"{key:<9}: ${value:<.2f}")
print("----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)
count = 0
print("----------- YOUR ORDER -----------")
for food in cart:
    if count%2 == 0:
        print(food, end=" ")
    else:
        print(food, end="\n")
    count += 1
print()
print(f"Your total is: ${total:.2f}")