#       PATTERN 21


#         *****
#         *   *
#         *   *
#         *   *
#         *****


t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        for _ in range(n):
            if __ == 0 or _ == 0 or __ == n - 1 or _ == n - 1:
                print("*", end="")
            else:
                print(" ", end="")

        print()