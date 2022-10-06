# print a pattern

n = int(input("Enter your number:"))

for i in range(1, n+1):
    for j in range(1, i+1):
        print (j , end=" ")
    print ("")

for k in range(n, 0, -1):
    for l in range(1, k+1):
        if l != 1:
            print (l-1, end=" ")
    print ("")