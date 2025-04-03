#  PATTERN 6

#        1 2 3 4 5
#        1 2 3 4
#        1 2 3
#        1 2
#        1

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        for _ in range(n-__):
            print(_+1, end=" ")
        print()