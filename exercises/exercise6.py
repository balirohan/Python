# Python Rectangle pattern 

n = int(input("Enter length: "))
m = int(input("Enter breadth: "))

for i in range(m):
    if i == 0 or i == m-1:
            print("*"*n)
    else:
          print("*", sep="")
          print(" "*(n-2), sep="")
          print("*")