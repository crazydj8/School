# Write a function that receives a start value and end value and lists all prime numbers between them , if start value is not specified take it as 10 if end value is not specified take it as 50.

def prime(start=10, end=50):
    i = -1
    l = []
    for x in range(start, end):
        for i in range(2, x):
            if x % i == 0:
                break
        if i == (x - 1):
            l.append(x)
    print("Prime numbers between", start, "and", end, "are:")
    print(l)
        
a = int(input("Enter you start limit"))
b = int(input("Enter you end limit"))

prime(a, b)
prime(start=a)
prime(end=b)
prime()
prime(end = 60, start = 50)