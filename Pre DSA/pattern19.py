#       PATTERN 19

#       **********
#       ****  ****
#       ***    ***
#       **      **
#       *        *
#       *        *
#       **      **
#       ***    ***
#       ****  ****
#       **********


t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n//2):
        for _ in range((n//2)-__):
            print("*", end="")
        for space in range(2*__):
            print(" ", end="")
        for _ in range((n//2)-__):
            print("*", end="")
        print()
    for __ in range(n//2):
        for _ in range(__+1):
            print("*", end="")
        for space in range(n-(2*__)-2):
            print(" ", end="")
        for _ in range(__+1):
            print("*", end="")
        print()