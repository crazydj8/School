# read two lists A and B, write a function that returns a list that contains only yhe elements that are common to both the lists

def common(l1, l2):
    x = len(l1)
    y = len(l2)
    l3 = []

    for i in range(0, x):
            if l1[i] in l2:
                if l1[i] in l3:
                    continue
                else:
                    l3.append(l1[i])
    return(l3)
    
l1 = []
x = int(input("Enter the number of elements of list 1:"))
for i in range(0, x):
    a = input("Enter element no.:")
    l1.append(a)

l2 = []
y = int(input("Enter the number of elements of list 2:"))
for i in range(0, y):
    a = input("Enter element no.:")
    l2.append(a)
   
print("intersection list =", common(l1,l2))
    