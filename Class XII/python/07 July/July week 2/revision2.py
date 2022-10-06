# define a swap function

h = int(input("Enter first number:"))
g = int(input("Enter second number:"))


def swap(a, b):
    x = a
    a = b
    b = x
    return(a,b)
    
print(swap(h, g))
print(h, g)
    
    