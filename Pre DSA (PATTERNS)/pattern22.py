#       PATTERN 22


#      4 4 4 4 4 4 4
#      4 3 3 3 3 3 4
#      4 3 2 2 2 3 4
#      4 3 2 1 2 3 4
#      4 3 2 2 2 3 4
#      4 3 3 3 3 3 4
#      4 4 4 4 4 4 4


t = int(input())

for i in range(t):
    n = int(input())
    for __ in range((2*n)-1):
        for _ in range((2*n-1)):
            top = __
            left = _
            right = (2*n - 2) - _
            down = (2*n - 2) - __
            print(n - min(min(top, down), min(left, right)), end="")
        print()