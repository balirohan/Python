# PATTERN 15

#        A B C D E
#        A B C D
#        A B C
#        A B
#        A

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        char = ord("A")
        for _ in range(n-__, 0, -1):
            print(chr(char), end=" ")
            char = char + 1
        print()