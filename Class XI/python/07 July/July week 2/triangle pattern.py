# for a limit n print numbers in a triangle

n = int(input("Enter your limit:"))

for i in range(1, n+1):

    for j in range(1, n-i+1):
        print (" ", end="")

    for k in range(1, i+1):
        print (k, end="")

    for l in range(i, 1, -1):
        print (l-1, end="")

    print ("")
