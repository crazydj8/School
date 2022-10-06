# enter a number and write its table from 1-10

a = int(input("Enter your number:"))

for x in range(1, 11):
    b = a * x
    print (a, "*", x, "=", b)
