# read a number and print its reverse

a = int(input("Enter your number:"))

num = 0
b = a

while b > 0:
    r = b % 10
    b = b // 10
    num = 10 * num + r

print (num)
