# write a function which recieves a value n and generates the first n lines of pascals triangle in a list

def pascal(n):
    n = n
    l1 = []
    for i in range(0, n):
        coff = 1
        l2 = []
        for k in range(0, i+1):
            l2.append(coff)
            coff = int(coff * (i - k) / (k + 1))
        l1.append(l2)

    
    return(l1)
    
a = int(input("Enter number of rows:"))

print(pascal(a))