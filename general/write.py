# Writing in files (.txt, .json, .csv)

import json, csv

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

txt_data = "I like pasta!"

file_path = "general/output.txt"
file_path = "general/output.json"
file_path = "general/output.csv"

# try:
#     with open(file=file_path, mode="w") as file:
#         for employee in employees:
#             file.write(employee+" ")
#         print(f"text file '{file_path}' was created")
# except FileExistsError:
#     print("The file already exists, change mode from 'x' to write in it.")

# try:
#     with open(file=file_path, mode="w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"JSON file '{file_path}' was created")
# except FileExistsError:
#     print("The file already exists, change mode from 'x' to write in it.")

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"text file '{file_path}' was created")
except FileExistsError:
    print("The file already exists, change mode from 'x' to write in it.")