'''read a number x, now print a number y with no. of digits
of x in tens and the most significant digit of x as its units place'''

x = int(input("Enter your number:"))

n = 0
b = x

while b > 0:
    b = b // 10
    n = n + 1

q = 10 ** (n-1)
y = (10 * n) + (x / q)

print (y)
