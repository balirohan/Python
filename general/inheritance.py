# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Max")
cat = Cat("Tinkle")
mouse = Mouse("Stuart")

print(dog.name)
print(f"is {dog.name} alive?: {dog.is_alive}")
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print(f"is {cat.name} alive?: {cat.is_alive}")
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name)
print(f"is {mouse.name} alive?: {mouse.is_alive}")
mouse.eat()
mouse.sleep()
mouse.speak()