# check if number is a perfect number or not
# perfect number is a number which is equal to sum of its digits

a = int(input("Enter the number:"))
s = 0
b = (a/2)+1

for x in range(1, b):
    if a % x == 0:
        s = s + x

if s == a:
    print (a, "Is a perfect number")
else:
    print (a, "Is not a perfect number")

