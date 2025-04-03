# PATTERN 4

#        1
#        2 2
#        3 3 3
#        4 4 4 4
#        5 5 5 5 5

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        for _ in range(__+1):
            print(__+1, end=" ")
        print()