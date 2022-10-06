# read sides of triangle and tell which type of triangle it is it is

a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))

if a == b and b == c and a == c:
    (print "It is an equilateral triangle")

elif a + b > c and b + c > a and a + c > a:
    if a != b and b != c and a != c:
        (print "Its a scalene triangle")
    if a != b and b == c:
        (print "Its an isosceles triangle")
    elif a != c and b == a:
        (print "Its an isosceles triangle")
    elif c != b and a == c:
        (print "Its an isosceles triangle")

else:
    print ("it cannot form a triangle")
    



