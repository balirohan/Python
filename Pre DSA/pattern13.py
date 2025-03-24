# PATTERN 13

#        1
#        2 3
#        4 5 6
#        7 8 9 10
#        11 12 13 14 15

t = int(input())

for i in range(t):
    n = int(input())
    num = 1
    for __ in range(n):
        for _ in range(__+1):
            print(num, end=" ")
            num += 1
        print()
