# print n terms of fibonacci series
# sum of previous 2 terms will give third term

n = int(input("Enter the number of terms:"))

num1 = 0
num2 = 1

print (num1)
print (num2)

for i in range(3, n+1):
    num3 = num1 + num2
    print (num3)

    num1 = num2
    num2 = num3

