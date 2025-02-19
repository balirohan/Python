# Python reading files (.txt, .json, .csv)

import json, csv

file_path = "general/output.txt"
file_path = "general/output.csv"
file_path = "general/output.json"

# try:
#     with open(file=file_path, mode="r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("That file was not found")

# except PermissionError:
#     print("You're not allowed to read this file")

try:
    with open(file=file_path, mode="r") as file:
        content = json.load(file)
        print(content[0])
        print(content[0]["name"])
        print(content[0]["age"])
        print(content[0]["job"])

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You're not allowed to read this file")

# try:
#     with open(file=file_path, mode="r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
#             print(line[0])

# except FileNotFoundError:
#     print("That file was not found")

# except PermissionError:
#     print("You're not allowed to read this file")