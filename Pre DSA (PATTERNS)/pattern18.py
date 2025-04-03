# PATTERN 18

#        E
#        D E
#        C D E
#        B C D E
#        A B C D E

t = int(input())

for i in range(t):
    n = int(input())
    char = 64 + n
    for __ in range(n):
        col_char = char
        for _ in range(__+1):
            print(chr(col_char), end=" ")
            col_char += 1
        char -= 1
        print()
