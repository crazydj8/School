# for numbers in range n, print numbers in pattern

n = int(input("Enter your number:"))
b = (2 * n) + 1

for i in range(1, b, 2):
    for j in range(1, i+1):
            print (j, end=" ")
    print ("")
