# PATTERN 2

#        * * * * *
#        * * * *
#        * * *
#        * *
#        *


t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        for _ in range(n-__):
            print("*", end=" ")
        print()