# PATTERN 16

#           A
#          ABA
#         ABCBA
#        ABCDCBA

t = int(input())

for i in range(t):
    n = int(input())
    for __ in range(n):
        for space1 in range(n-__-1):
            print(" ", end="")

        char = ord("A")
        for letter in range((2*__)+1):
            print(chr(char), end="")
            if letter < ((2*__)+1)//2:
                char += 1
            else:
                char -= 1

        for space2 in range(n-__-1):
            print(" ", end="")

        print()