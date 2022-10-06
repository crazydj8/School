# write a function that recieves a list of 10 integers and find the largest and smallest ad returns their values, another fn that takes 2 values x, y and replaces all occurances of x with y and returns no. of changes. read a list of 10 values and use both functions

def smlrg(l1):
    sml = l1[0]
    lrg = l1[0]
    l2 = []
    for i in range(0, len(l1)):
        if l1[i] > lrg:
            lrg = l1[i]
        elif l1[i] < sml:
            sml = l1[i]
    l2.append(lrg)
    l2.append(sml)
    return (l2)
    
def swap(l1, x, y):
    for i in range(0, len(l1)):
        if l1[i] == x:
            l1[i] = y
            
    return(l1)
    
    
l1 = []    
for a in range(0, 10):
    a = int(input("Enter your number:"))
    l1.append(a)
    
print(smlrg(l1))

x = int(input("Enter the no. you want to swap:"))
y = int(input("Enter the number you want to swap with:"))

print(swap(l1, x, y))