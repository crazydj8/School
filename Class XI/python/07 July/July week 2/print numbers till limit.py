# for numbers in range n, print 1 and 0 in pattern
# loop nesting example

n = int(input("Enter your number:"))

for i in range(1, n+1):
    for j in range(1, i+1):
        print (j % 2, end=" ")
    print ("")
