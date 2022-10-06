# program to print twin primes between 10 and 50
11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47

p1 = -1

for n in range(10, 50):

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            break
    if i == (n // 2):
        if p1 == -1:
            p1 = n
        else:
            p2 = n
            print (p1, p2)
            p1 = p2
   
