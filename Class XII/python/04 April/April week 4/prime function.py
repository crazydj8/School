# write a function that recieves a number and checks whether its a prime number or not. read a number x and check all primes between 2 and x.

def prime(x):
    i = -1
    for i in range(2, x):
        if x % i == 0:
            break
    if i == (x - 1):
        print(x, "is prime")
        
x = int(input("Enter your limit:"))

for j in range(2, x):
    prime(j)