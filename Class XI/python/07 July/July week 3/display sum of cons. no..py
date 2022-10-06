# read a no and display list of consecutive no that add up to that no.

n = int(input("Enter your limit:"))
suma = 0
r = 1

for i in range(1, n):
    suma = 0

    for j in range(i, n):
        suma = suma + j
        if suma > n:
            break
        elif suma == n:
            for x in range(i, j + 1):
                print (x, end=" ")
    print ("")
