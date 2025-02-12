# List comprehension = A concise way to create lists in Python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1, 11) ]
# print(doubles)

# triples = [x * 3 for x in range(1, 11)]
# print(triples)

# squares = [x ** 2 for x in range(1, 11)]
# print(squares)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_nums = [x for x in numbers if x >= 0]
# negative_nums = [y for y in numbers if y < 0]
# print(positive_nums, negative_nums, sep="\n")

# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 != 0]
# print(even_nums, odd_nums, sep="\n")

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)