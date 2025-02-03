# Python Calculator

operator = input("Enter an operator (+ - * /): ")
while True:
    if operator in "+-*/":
        break
    else:
        print("invalid input")
        operator = input("Enter an operator (+ - * /): ")

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
else:
    print(int(num1 / num2))