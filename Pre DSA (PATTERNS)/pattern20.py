#       PATTERN 20


#       *        *
#       **      **
#       ***    ***
#       ****  ****
#       **********
#       ****  ****
#       ***    ***
#       **      **
#       *        *

t = int(input())

for i in range(t):
    n = int(input())
    spaces = 2*n-2
    for __ in range((2*n)-1):
        stars = __+1
        if __ >= n:
            stars = 2*n-__-1
        for _ in range(stars):
            print("*", end="")

        for _ in range(spaces):
            print(" ", end="")

        for _ in range(stars):
            print("*", end="")

        if __+1 < n:
            spaces -= 2
        else:
            spaces += 2

        print()