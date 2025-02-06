# collection = single "variable" used to store multiple values
#   List       = [] ordered and changeable. Duplicates OK
#   Set        = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple      = () ordered and unchangeable. Duplicates OK. FASTER
#   Dictionary = {} ordered and changeable. NO duplicates
#                   A collection of {key:value} pairs         


# LIST  -  UNORDERED & CHANGEABLE
# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(fruits[::-1])

# print("apple" in fruits)
# print("pineapple" in fruits)

# fruits[0] = "kiwi"

# fruits.append("grapes")
# fruits.remove("coconut")
# fruits.insert(0, "grapes")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("kiwi")) --> element not found in list would return an error
# print(fruits.count("kiwi"))
# print(fruits)

# for fruit in fruits:
#     print(fruit)




# SETS  -  UNORDERED & IMMUTABLE

# fruits = {"apple", "banana", "orange", "coconut"}

# for fruit in fruits:
#     print(fruit)

# print(help(fruits))
# print(dir(fruits))
# print(fruits)
# print(len(fruits))
# print("Pineapple" in fruits)

# print(fruits[0]) --> indexing doesn't work with sets

# fruits.add("grape")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# fruits.add("coconut") --> prints only 1
# print(fruits)




# TUPLES  -  ORDERED & UNCHANGEABLE

# fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print(fruits)
# print("pineapple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# for fruit in fruits:
#     print(fruit)




# DICTIONARY  -  ORDERED & CHANGEABLE

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(dict)

# print(capitals.get("USA"))
# print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("That capital exists!")
# else:
#     print("That capital doesn't exist.")

# print(capitals)



# capitals.update({"Germany": "Berlin"})
# print(capitals.update({"USA": "Detroit"}))
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# print(capitals)

# keys = capitals.keys()
# for key in keys:
#     print(key)

# values = capitals.values()
# for value in values:
#     print(value)

# items = capitals.items()
# for key, value in items:
#     print(f"{key:<7}: {value:<}")

# print(items)
# print(values)
# print(keys)