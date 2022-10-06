# read a number and check if it is prime or not

a = int(input("Enter your number:"))

prime = 1

if a < 2:
    print ("Number invalid")

else:
    for x in range(1, (a//2) + 1):
        if a % x == 0:
            b = x

    if b == 1:
        prime = 0

    if prime == 1:
        print ("composite")
    elif prime == 0:
        print ("prime")

