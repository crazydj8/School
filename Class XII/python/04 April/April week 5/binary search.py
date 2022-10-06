# write a function that performs binary search of a number on a list

def searcha(l1, x):
    beg = 0
    last = len(l1) - 1
    while beg <= last:
        mid = (beg + last) // 2
        if x == l1[mid]:
            return (mid)
            
        elif x < l1[mid]:
            last = mid - 1
            
        elif x > l1[mid]:
            beg = mid + 1
    return ("Not Found")
    
def searchd(l1, x):
    beg = 0
    last = len(l1) - 1
    while beg <= last:
        mid = (beg + last) // 2
        if x == l1[mid]:
            return (mid)
            
        elif x > l1[mid]:
            last = mid - 1
            
        elif x < l1[mid]:
            beg = mid + 1
    return ("Not Found")

l1 = [1, 2, 3, 4, 5]
l2 = [5, 4, 3 ,2 ,1]
a = int(input("Enter the number you want to search:"))

print("The postion of", a, "in list 1 is:", searcha(l1, a))
print("The postion of", a, "in list 2 is:", searchd(l2, a))
    