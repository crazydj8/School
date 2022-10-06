'''define a tuple to hold three coordinates of a triangle determine if
the 3 points form a triange at all, if they do, find the kind of 
triangle'''

import math

t = ((0,0,), (3,0,), (0,4,), )

a = math.sqrt((t[0][0] - t[1][0]) ** 2 + (t[0][1] - t[1][1]) ** 2)
b = math.sqrt((t[1][0] - t[2][0]) ** 2 + (t[1][1] - t[2][1]) ** 2)
c = math.sqrt((t[2][0] - t[0][0]) ** 2 + (t[2][1] - t[0][1]) ** 2)

if a == b and b == c and a == c:
    print ("It is an equilateral triangle")

elif a + b > c and b + c > a and a + c > a:

    if a != b and b != c and a != c:
        print ("Its a scalene triangle")

    if a != b and b == c:
        print ("Its an isosceles triangle")

    elif a != c and b == a:
        print ("Its an isosceles triangle")

    elif c != b and a == c:
        print ("Its an isosceles triangle")

else:
    print ("it cannot form a triangle")
