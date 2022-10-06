# write a function to sort the list of numbers in ascending order

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
    
l1 = [5,2,12,16,1,14]

print(sorta(l1))
print(sortd(l1))