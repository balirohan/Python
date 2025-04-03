# PATTERN 13

#        A
#        A B
#        A B C
#        A B C D
#        A B C D E

t = int(input())

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(t):
    n = int(input())
    for __ in range(n):
        for ch in range(ord('A'), ord('A') + __ + 1):
            print(chr(ch), end=" ")
        print()