#write a program to read a number and check if it is an armstrong number create a function cntdig that recieves the number and counts the number of digits. arm function recieves a number and checks if its armstrong number.


def cntdig(x):
    i = 0
    while x > 0:
        x = x // 10
        i = i + 1
    return (i)

def check(x):
    dig = cntdig(x)
    suma = 0
    a = x
    while a > 0:
        r = a % 10
        a = a // 10
        suma = suma + r ** dig 
    if suma == x:
        print("Armstrong")
    else:
        print("Not Armstrong")
        
a = int(input("Enter your number:"))

check(a)

    
    