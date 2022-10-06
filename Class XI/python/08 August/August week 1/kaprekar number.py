# check if a number is a kaprekar number

lim = int(input("Enter  your limit:"))

for n in range(0, lim+1):

    string = str(n)
    x = len(string)
    sqr = n ** 2
    i = 0
    suma = 0

    while i < x:
        a = sqr % 10
        sqr = sqr // 10
        suma = suma  + (a * (10 ** i))
        i = i + 1

    new = suma + sqr

    if new == n:
        print (n)