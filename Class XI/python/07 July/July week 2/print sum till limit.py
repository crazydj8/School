# read the limit and print numbers 1 - 2/2' + 4/4' -6/6'
# x' represents factorial of x

n = int(input("Enter your limit:"))

if n == 1:
    print (1)
else:
    print ("1 ,", end=" ")
    for i in range(1, n+1):
        b = 2 * i
        print (b, "/", end=" ")

        suma = 1

        for j in range(1, b+1):
            suma = suma * j

        print (suma, ",", end=" ")
