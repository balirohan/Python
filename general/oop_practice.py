# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# student1 = Student("Rohan Bali", 22)
# student1.display_info()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     def get_salary(self):
#         return f"Name: {self.name}, Salary: {self.__salary}"
    
#     def set_salary(self, new_salary):
#         if new_salary >= 0:
#             self.__salary = new_salary
#             return f"Salary has been updated successfully. Your new salary is: {self.__salary}"
#         else:
#             return f"New salary should be greater than 0"
        

# employee1 = Employee("Rohan Bali", 10000)
# print(employee1.get_salary())
# print(employee1.set_salary(25000))


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price

#     def get_price(self):
#         return f"Price of {self.name} is {self.__price} Rs."
    
#     def set_price(self, new_price):
#         if new_price < 0:
#             raise ValueError("Price cannot be less than 0 Rs.")
#         print(f"Price has been set to {new_price}")
#         self.__price = new_price

# product1 = Product("iPhone 16 SE", 59999)
# print(product1.get_price())
# product1.set_price(49999)
# product1.set_price(-50)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return f"Price of {self.name} = {self.__price}"
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price should be greater than or equal to 0.")
        self.__price = new_price
        return f"The new price of {self.name} has been set to {self.__price}"

product1 = Product("iPhone 16 SE", 59999)
print(product1.price)
product1.price = 49999