# write a function that recieves a lsit and returns the number of elements that are unique in this list

l1 = [2, 3, 56, 78, 90, 2, 34 ,3]

def unique(l1):
    n = len(l1)
    l2 = []
    for i in range(0, len(l1)):
        if l1[i] not in l2:
            l2.append(l1[i])
            if l1[i] in l1[i+1:]:
                n = n - 1
    return(n)
    
print("Unique=", unique(l1))