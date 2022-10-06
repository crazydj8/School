# number pattern

n = int(input("Enter your number:"))

for k in range(n, 0, -1):
    for l in range(1, k+1):
        print (l, end=" ")

    for a in range(n-k, 0, -1):
        print (" ", end=" ")

    for b in range(n-k, 0, -1):
        print (" ", end=" ")

    for m in range(k, 0, -1):
        print (m, end=" ")
    print ("")

for i in range(2, n+1):
    for j in range(1, i+1):
        print (j, end=" ")

    for y in range(n-i, 0, -1):
        print (" ", end=" ")

    for z in range(n-i, 0, -1):
        print (" ", end=" ")

    for x in range(i, 0, -1):
        print (x, end=" ")
    print ("")