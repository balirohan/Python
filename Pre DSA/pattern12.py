# PATTERN 12

#        1      1                        6
#        12    21                        4
#        123  321                        2
#        12344321                        0

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        for left_num in range(__+1):
            print(left_num+1, end="")
        for space in range(2*(n-__) - 2):
            print(" ", end="")
        for right_num in range(__+1, 0, -1):
            print(right_num, end="")
        print()