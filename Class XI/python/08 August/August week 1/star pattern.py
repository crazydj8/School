# star pattern

n = int(input("Enter your limit:"))
n = n + 1

for i in range(1, n+1):

    for j in range(1, n-i+1):
        print (" ", end="")

    print ("*", end="")
    
    for x in range(i, 1, -1):
        if i != n:
            print (" ", end="")
        elif i == n:
            print ("*", end="")
        
    for y in range(i, 2, -1):
        if i != n:
            print (" ", end="")
        elif i == n:
            print ("*", end="")

    if i != 1:
        print ("*", end="")

    print ("")
    
for p in range(n-1, 0, -1):

    for j in range(1, n-p+1):
        print (" ", end="")

    print ("*", end="")

    for l in range(p, 1, -1):
        print (" ", end="")
        
    for h in range(p, 2, -1):
        print (" ", end="")
    
    if p != 1:
        print ("*", end="")

    print ("")


