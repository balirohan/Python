# Python Rectangle pattern 


le = input("Enter length: ")
while not le.isdigit():
        print("Enter a digit!")
        le = input("Enter length: ")
le = int(le)

br = input("Enter breadth: ")
while not br.isdigit():
        print("Enter a digit!")
        br = input("Enter breadth: ")
br = int(br)

for i in range(br):
    if i == 0 or i == br-1:
            print("*"*le)
    else:
          print("*", " "*(le-2), "*", sep="")