# write a program to read a list of 10 elements. sort the list. read an item to be deleted. find position of item using binary search. delete the item. print the deleted list.
import bisect

def sort(l1):
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

def pos(l1, x):
    pos = bisect.bisect(l1, x)
    return (pos)

l1 = [10, 54, 36, 78, 99]
x = int(input("Enter the number you want to delete:"))

sort(l1)
print ("List before:", l1)
y = pos(l1, x)

l1.pop(y-1)
print ("List after":, l1)


