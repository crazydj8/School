# program with start of ap and step value. write 4 terms of ap

a = int(input("Enter the initial value of the AP:"))
d = int(input("Enter the step value"))

def ap(a, d):
    x = a
    y = a + d
    z = a + (2 * d)
    q = a + (3 * d)
    return(x, y, z, q)
    
print("Your AP is:", ap(a, d))