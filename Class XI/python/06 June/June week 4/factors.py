# read number and display its factors

a = int(input("Enter your number:"))

print ("Factors for", a, "are:")

for x in range(1, a//2):
    if a % x == 0:
        print (x)
print (a)
