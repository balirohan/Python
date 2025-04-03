# PATTERN 3

#        1
#        1 2
#        1 2 3
#        1 2 3 4
#        1 2 3 4 5

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(1, n+1):
        for _ in range(__):
            print(_+1, end=" ")
        print()