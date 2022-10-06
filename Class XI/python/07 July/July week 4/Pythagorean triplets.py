# program to display all pythagorean triplets from 1 to limit

n =  int (input("Enter your limit:"))

print ("Pythagorean triplets from 1 to", n, "are:")
for a in range(1, n+1):
    x = a ** 2
    for b in range(a+1, n+1):
        y = b ** 2
        for c in range(b+1, n+1):
            z = c ** 2

            if x + y == z:
                print (a, ",", b, ",", c)