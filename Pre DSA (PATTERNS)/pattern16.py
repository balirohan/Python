# PATTERN 16

#        A
#        B B
#        C C C
#        D D D D
#        E E E E E

t = int(input())

for i in range(t):
    n = int(input())
    char = ord("A")
    for __ in range(n):
        for _ in range(__+1):
            print(chr(char), end=" ")
        print()
        char += 1