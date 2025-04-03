# PATTERN 11

#        1
#        0 1
#        1 0 1
#        0 1 0 1
#        1 0 1 0 1


t = int(input())

for i in range(t):
    num = 1
    n = int(input())
    for __ in range(n):
        num = 1 if __%2 == 0 else 0
        for _ in range(__+1):
            print(num, end="")
            num = 0 if num == 1 else 1
        print()