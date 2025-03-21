#  PATTERN 7

#        *
#       ***
#      *****
#     *******
#    *********

# t = int(input())

# for i in range (t):
#     n = int(input())
#     c = n-1
#     for __ in range(n):
#         print(" "*c, end="")
#         for _ in range((2*__) + 1):
#             print("*", end="")
#         c-=1
#         print()

t = int(input())

for i in range (t):
    n = int(input())
    for __ in range(n):
        for s1 in range(n-__-1):
            print(" ",end="")
        for star in range((2*__)+1):
            print("*", end="")
        for s2 in range(n-__-1):
            print(" ",end="")
        print()