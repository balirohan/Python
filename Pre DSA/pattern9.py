#    PATTERN 9

#        *
#       ***
#      *****
#     *******
#    *********
#    *********
#     *******
#      *****
#       ***
#        *

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        for space in range(n-__-1):
            print(" ", end="")
        for star in range((2*__)+1):
            print("*", end="")
        print()
    for __ in range(n):
        for space in range(__):
            print(" ", end="")
        for star in range(2*(n-__)-1):
            print("*", end="")
        print()