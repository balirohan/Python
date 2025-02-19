# Decorator = A function that extends the behavior of another function w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

#             we need to add a wrapper in the decorator function, otherwise it will get called by itself.

def add_sprinkles(func):
    def wrapper(*args):
        print("*You add sprinkles* 🎊")
        func(*args)
    return wrapper

def add_fudge(func):
    def wrapper(*args):
        print("*You add fudge* 🍫")
        func(*args)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(size, flavor):
    print(f"Here is your {size} {flavor} ice cream 🍨")

get_ice_cream("medium", "vanilla")