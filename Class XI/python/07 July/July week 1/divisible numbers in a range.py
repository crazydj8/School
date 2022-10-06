# print numbers between 1 and m which is divisible by m
# display whether the printed number is even or odd

n = int(input("Enter your limit:"))
m = int(input("Enter your divisor:"))

for i in range(1, n+1):

    if i % m == 0:

        if i % 2 == 0:
            print (i, ", Even")

        else:
            print (i, ", Odd")