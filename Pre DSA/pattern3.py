t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(1, n+1):
        for _ in range(__):
            print(_+1, end=" ")
        print()