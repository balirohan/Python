# PATTERN 1

#                   *  *  *  *
#                   *  *  *  *
#                   *  *  *  *
#                   *  *  *  *
t = int(input(""))

for _ in range(t):
    n = int(input("Enter Number of lines: "))

    for __ in range(n):
        for _ in range(n):
            print("*", end=" ")
        print()