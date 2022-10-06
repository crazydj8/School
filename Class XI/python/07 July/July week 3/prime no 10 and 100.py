# print all prime numbers between 10 and 100
n = int(input("Enter your limit:"))
print ("All prime numbers between 0 and " + str(n) + " are:")
for i in range(2, n):
    prime = 1
    for x in range(1, (i // 2) + 1):
        if i % x == 0:
            b = x

    if b == 1:
        prime = 0

    if prime == 0:
        print (i, end=" ")
