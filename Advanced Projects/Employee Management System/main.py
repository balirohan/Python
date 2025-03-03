# EMPLOYEE MANAGEMENT SYSTEM

import csv
import os

PATH = "Advanced Projects/Employee Management System/data.csv"
COLUMNS = ["Name", "Age", "Gender", "Phone Number", "Email", "Salary", "EmployeeID", "Department"]

class Person:
    def __init__(self, name, age, gender, phone_num, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_num = phone_num
        self.email = email

    @classmethod
    def search_employee(cls, employee_id):
        try:
            with open(PATH, "r") as file:
                reader = csv.reader(file)
                header = next(reader, None)  # Skip header row
                
                for row in reader:
                    if row and row[-2] == employee_id:  # Check EmployeeID column
                        print("\n✅ Employee Found:")
                        print(f"Name: {row[0]}, Age: {row[1]}, Gender: {row[2]}, Phone: {row[3]}, Email: {row[4]}, Salary: {row[5]}, EmployeeID: {row[6]}, Department: {row[7]}")
                        return  # Stop searching after finding the employee
                        
        except FileNotFoundError:
            print("\n❌ The file doesn't exist.")
        
        print(f"\n❌ Employee with ID {employee_id} not found.")
        

class Employee(Person):
    def __init__(self, name, age, gender, phone_num, email, salary, employee_id, department):
        super().__init__(name, age, gender, phone_num, email)
        self.__salary = salary
        self.employee_id = employee_id
        self.department = department

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError(f"You cannot set the salary as {new_salary}. Try setting it to a value above 0.")
        self.__salary = new_salary
        print(f"Salary updated successfully. Your current salary is {self.__salary}")

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")
        print(f"Employee Gender: {self.gender}")
        print(f"Employee Mobile Number: {self.phone_num}")
        print(f"Employee Email: {self.email}")
        print(f"Employee Salary: {self.salary}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Department: {self.department}")

    def save_to_file(self, PATH):
        file_exists = os.path.exists(PATH)
        is_empty = os.stat(PATH).st_size == 0 if file_exists else True
        with open(PATH, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists or is_empty:
                writer.writerow(COLUMNS)
            
            writer.writerow([self.name, self.age, self.gender, self.phone_num, self.email, self.salary, self.employee_id, self.department])
        print(f"Employee data saved successfully to {PATH}")

    def load_from_file(self):
        try:
            with open(PATH, "r") as file:
                reader = csv.reader(file)
                print("Employee Data from file: ")
                for row in reader:
                    print(", ".join(row))
        except FileNotFoundError:
            print("File doesn't exist.")


employee1 = Employee("Rohan Bali", 22, "Male", "8860508975", "balirohan301@gmail.com", 10000, "BT21GCS059", "AI")
# employee1.display_info()
# employee1.save_to_file(PATH)
# employee1.load_from_file()
Employee.search_employee("BT21GCS059")