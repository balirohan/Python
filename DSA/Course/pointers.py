# INTEGERS
# num1 = 11

# num2 = num1

# print("Before num2 value is updated:")
# print(f"num1 = {num1}")
# print(f"num2 = {num2}")

# print(f"\nnum1 points to: {id(num1)}")
# print(f"num2 points to: {id(num2)}")

# # num2 points to the same memory location as num1

# num2 = 22

# print("\nAfter num2 value is updated:")
# print(f"num1 = {num1}")
# print(f"num2 = {num2}")

# print(f"\nnum1 points to: {id(num1)}")
# print(f"num2 points to: {id(num2)}")


#DICTIONARY
dict1 = {'value': 11} 
dict2 = dict1  # dict2 points to the same location as dict1

print("Before value is updated:")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"\ndict1 points to {id(dict1)}")
print(f"dict2 points to {id(dict2)}")

dict2['value'] = 22

print("\nAfter value is updated:")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"\ndict1 points to {id(dict1)}")
print(f"dict2 points to {id(dict2)}")