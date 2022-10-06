# prime check for a number using break statement

n = int(input("Enter the number:"))

print (" ") 

for i in range(2, (n // 2) + 1):
    if n % i == 0:
        break

if i == (n // 2):
    print ("It is a prime no.")
else:
    print ("It is a composite no.")
