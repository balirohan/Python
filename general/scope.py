# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# func1()
# func2()




# def func1():
#     x = 1   # x -> enclosed scope
#     def func2():
#         x = 2    # x -> local scope
#         print(x)
#     func2()

# func1()




# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 3   # x -> global

# func1()
# func2()


# from math import e    # e -> built-in

# def func1():
#     print(e)

# e = 3    # e -> global

# func1()