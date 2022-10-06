# write a function that recieves a number and checks if it is a perfect number. write a function test that recieves starting value(11) and ending value(20) which calls the first function.

def perfect(x):
    suma = 0
    for i in range(1, x-1):
        if x % i == 0:
            suma = suma + i
    
    if suma == x:
        print(x, "is perfect number")

def test(a=11, b=20):
    for i in range(a, b+1):
        perfect(i)
   
test()
test(1)
test(b=100)
test(b = 200, a =100)