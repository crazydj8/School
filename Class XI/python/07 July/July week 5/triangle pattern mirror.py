# for a limit n print numbers in a triangle

n = int(input("Enter your limit:"))
n = n + 1

for p in range(n-1, 1, -1):

    for j in range(1, n-p+1):
        print (" ", end="")

    for k in range(1, p+1):
        print ("*", end="")

    for l in range(p, 1, -1):
        print ("*", end="")

    print ("")

for i in range(1, n+1):

    for j in range(1, n-i+1):
        print (" ", end="")

    for k in range(1, i+1):
            print ("*", end="")

    for l in range(i, 1, -1):
        print ("*", end="")

    print ("")
    

