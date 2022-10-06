# write a program to read a list of 10 elements in descending order. read an element to be inserted. perform using bisect module
import bisect
def sorta(l1):
    for i in range(0, len(l1)):
        small = l1[i]
        pos = i
        for j in range(i+1, len(l1)):
            if l1[j] < small:
                small = l1[j]
                pos = j
        
        x = l1[i]
        l1[i] = l1[pos]
        l1[pos] = x
        
    return (l1)
    
def sortd(l1):
    for k in range(0, len(l1)):
        large = l1[k]
        pos = k
        for j in range(k+1, len(l1)):
            if l1[j] > large:
                large = l1[j]
                pos = j
        
        x = l1[k]
        l1[k] = l1[pos]
        l1[pos] = x
        
    return (l1)
    
def insert(l1, x):
    bisect.insort(l1, x)
    
l1 = [99, 87, 54, 32, 11, 3]
print("Your list is:", l1)

x = int(input("Enter the element you want to add:"))
insert(l1, x)

sortd(l1)
print("Your new list is:", l1)