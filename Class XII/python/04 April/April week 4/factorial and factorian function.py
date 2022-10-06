# write a function check that recieves a number and returns its factorial. write a function check2 that recieves a number and checks if the number is a factorian. In main print a list of all factorians between 100 and 999.(number for which sum of factorial of digits is the number itself)

def check(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
        
    return(fact)
    
def check2(x):
    dig = len(str(x))
    a = x
    suma = 0
    while a > 0:
        rem = a % 10
        a = a // 10
        suma = suma + check(rem)
    if suma == x:
        print(x, "Is a factorian")

for i in range(100, 1000):
    check2(i)

