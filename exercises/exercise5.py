# Exercise 5 Validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a new username: ")
duplicate = input("Re-enter the username: ")

if not 12 >= len(username) > 0:
    print("Username must be longer than 0 characters and not more than 12 characters long.")
    print(f"{username} does not match the length criteria.")
elif username.find(" ") != -1:
    print("Username cannot contain spaces.")
    print(f"'{username}' contains space(s).")
elif username.isdigit():
    print("Username cannot contain digits.")
    print(f"{username} contains digit(s).")
elif username != duplicate:
    print("Usernames don't match, make sure you're entering the correct username each time.")
else:
    print(f"User '{username}' created.")