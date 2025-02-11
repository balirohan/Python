# *args   = allows you to pass multiple non-key arguments
# *kwargs = allows you to pass multiple keyword arguments
#           * unpacking operator
#           1. positional 2. default 3. keyword 4. ARBITRARY

# def add(a, b):
#     return a + b

# print(add(1, 2))  --> works
# print(add(1, 2, 3)) --> doesn't work

# def add(*args):         --> can change *args to any variable like *nums, *vals, etc.
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4, 5))

# def display_name(*args):
#     for _ in args:
#         print(_, end=" ")

# display_name("Mr.", "Rohan", "Kumar", "Bali", "III")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(street="123 Fake St.", apt="100", city="Detroit", state="Michigan", zip="54321")

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     if 'apt' in kwargs:
#         print('\n'+kwargs.get('street'), kwargs.get('apt'))
#     else:
#         print('\n'+kwargs.get('street'))
#     print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

# shipping_label("Dr.", "Spongebob", "Squarepants", "III",
#                street = "123 Fake St.",
#                apt = "#100",
#                city = "Detroit",
#                state = "MI",
#                zip = "54321")