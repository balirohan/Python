# Exercise 3.1 Circumference of a circle

import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is {circumference:.2f}cm")


# Exercise 3.2 Area of a circle

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {area:.2f}cm².")