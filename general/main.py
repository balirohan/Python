# This is my first Python program
# print("I like Spaghetti!")
# print("It's really good!")

#########################################################

# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))

# age += 1

# print(f"Hello {name}!")
# print("HAPPY BIRTHDAY!")
# print(f"You are {age} years old!")

#########################################################

# if = Do some code only IF some condition is True
#      else do something else

# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to sign up.")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet.")
# else:
#     print("You must be 18+ to sign up.")

# response  = input("Would you like food (Y/N): ").lower()

# if response == 'y':
#     print("Have some food!")
# else:
#     print("No food for you")

# name = input("Enter your name: ").lower()

# if name == "":
#     print("YOU DID NOT TYPE IN YOUR NAME!")
# else:
#     print(f"Hello {name}!")

# for_sale = True

# if for_sale:
#     print("This item is for sale!")
# else:
#     print("This item is not for sale.")

#########################################################

# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# OR
# temp = 20
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")

# AND + NOT
# temp = 0
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is SUNNY 🌞")

# elif temp <= 0 and is_sunny:
#     print("It is COLD outside 🥶")
#     print("It is SUNNY 🌞")

# elif 28 > temp > 0 and is_sunny:
#     print("It is WARM outside 🙂")
#     print("It is SUNNY 🌞")

# if temp >= 28 and not is_sunny:
#     print("It is HOT outside 🥵")
#     print("It is CLOUDY ☁")

# elif temp <= 0 and not is_sunny:
#     print("It is COLD outside 🥶")
#     print("It is CLOUDY ☁")

# elif 28 > temp > 0 and not is_sunny:
#     print("It is WARM outside 🙂")
#     print("It is CLOUDY ☁")

#########################################################

# Conditional expression =  one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on a condition
#                           X if condition else Y

# num = 5
# a = 6
# b = 7
# age = 13
# temp = 20
# user_role = "guest"

# print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b

# print(min_num)

# status = "Adult" if age >= 18 else "Minor"
# print(status)

# weather = "HOT" if temp > 20 else "COLD"
# print(weather)

# Access_level = "Full Access" if user_role == "admin" else "Limited Access"
# print(Access_level)

#########################################################

# String Methods

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find('a')
# result = name.rfind('a')
# result = name.capitalize()
# result = name.upper()
# result = name.upper()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("8")
# result = phone_number.replace("-", " ")

# print(result)

# print(help(str)) --> to list out all the methods of this data type

#########################################################

# String Indexing

# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# credit_number = "1234-5678-9012-3456"

# reversed_card = credit_number[::-1]
# print(reversed_card)

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# print(credit_number[2])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[-4:])
# print(credit_number[::2])

#########################################################

# format specifiers = {value:flags} format a value based on what flags are inserted

# price1 = 3000.14159
# price2 = -9870.65
# price3 = 1200.34

# print(f"Price 1 is ${price1:+,.2f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}")

#########################################################

# while loop = execute some code WHILE some condition remains True

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")




# age = int(input("Enter your age: "))

# while age <= 0:
#     print("Age can't be negative or zero.")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old!")




# food = input("Enter a food you like (q to quit): ")

# while food.lower() != "q":
#     print(f"You like {food}.")
#     food = input("Enter another food you like (q to quit): ")

# print('bye')




# num = int(input("Enter a number between 1-10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid!")
#     num = int(input("Enter a number between 1-10: "))

# print(f"Your number is {num}")

#########################################################

# for loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence, etc.

# for _ in range(10, 0, -1):
#     print(_)
# print("HAPPY NEW YEAR!!")

# credit_card = "1234-5678-0912-3456"

# for x in credit_card:
#     print(x)

# for x in range(21):
#     if x == 13:
#         print("Skipped it as it is unlucky!")
#         continue
#     else:
#         print(x)