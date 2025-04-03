#    PATTERN 10

#        *
#        **
#        ***
#        ****
#        *****
#        ****
#        ***
#        **
#        *

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(2*n-1):
        stars = __ + 1
        if __ + 1 > n: stars = 2*n - __ - 1
        for _ in range(stars):
            print("*", end="")
        print()