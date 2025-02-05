# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


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