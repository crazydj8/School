''' a number is a factorian if it is equal to sum of factorials of its
digits'''

a = int(input("Enter your number:"))

num = 0
b = a
suma = 0

while b > 0:
    r = b % 10
    b = b // 10

    facta = 1
    for j in range(1, r + 1):
        facta = facta * j
    suma = suma + facta

if suma == a:
    print ("Yes,", a, "is a factorian")
else:
    print ("No,", a, "is not a factorian")

