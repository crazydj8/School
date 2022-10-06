# read a number and display the sum of its digits

a = int(input("Enter your number:"))

num = 0
b = a

while b > 0:
    r = b % 10
    b = b // 10
    num = num + r

print ("sum =", num)
