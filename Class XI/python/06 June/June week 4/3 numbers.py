# read 3 numbers and display largest and smallest

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if a > b and a > c:
    if b < c:
        (print "largest:", a, "smallest:", b)
    elif c < b:
        (print "largest:", a, "smallest:", c)

elif b > a and b > c:
    if a < c:
        (print "largest:", b, "smallest:", a)
    elif c < a:
        (print "largest:", b, "smallest:", c)

elif c > a and c > b:
    if b < a:
        (print "largest:", c, "smallest:", b)
    elif a < b:
        (print "largest:", c, "smallest:", a)