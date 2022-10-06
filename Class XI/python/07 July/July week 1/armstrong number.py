# read and tell armstrong number
# it is a number which is equal to the sum of its (digits)^(number of terms)

a = int(input("Enter your number:"))

num = 0
b = a

while b > 0:
    b = b // 10
    num = num + 1

print ("Number of digits is", num)

suma = 0
c = a

while c > 0:
    rem = c % 10
    suma = suma + (rem**num)
    c = c // 10

if suma == a:
    print (a, "is an armstrong number")
else:
    print (a, "is not an armstrong number")
