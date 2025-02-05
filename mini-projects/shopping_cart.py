# Python Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n----- YOUR CART -----")
print(f"{'Food':<20} {'Price':>10}")
print("-" * 30)
# for food in foods:
#     print(food, end=" ")

for price in prices:
    total += price

# print()
# print(f"Your total is: ${total}")


for food, price in zip(foods, prices):
    print(f"{food:<20} ${price:>9.2f}")

print()
print(f"{'Total':<20} ${total:>9.2f}")