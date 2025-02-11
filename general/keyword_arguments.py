# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3.KEYWORD 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", "Mr.", "Spongebob", "Squarepants")
# hello("Hello", "Spongebob", "Squarepants", "Mr.")
# hello("Hello", first="Spongebob", last="Squarepants", title="Mr.")
# hello("Hello", "Mr.", last="John", first="James")

# for x in range(1, 11):
#     print(x, end=" ")   # 'end' is a keyword argument found within the print() function just like 'sep'

# for x in range(1, 6):
#     print(x, sep="-")

# def get_phone(country_code, area_code, first, last):
#     print(f"{country_code}-{area_code}-{first}-{last}")

# phone_num = get_phone(country_code=+91, area_code=88, first=6050, last=8975)