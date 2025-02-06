fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]
groceries = [["apple", "orange", "banana", "coconut"], 
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# fruits[0] = "pineapple"
# print(fruits)

# print(groceries[0][0]) --> apple

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()