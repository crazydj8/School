# write a function swap taht recieves 2 integers and swaps their values. print swapped values in function and in program after fn is called

h = int(input("Enter first number:"))
g = int(input("Enter second number:"))


def swap(a, b):
    global h, g
    g = a
    h = b
    '''a = h
    b = g
    print("Swapped - #1 =", a, "#2 =", b)'''
    
swap(h, g)
print("Original - #1 =", h, "#2 =", g)