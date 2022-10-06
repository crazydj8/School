# write a program to read a list of 10 numbers and perform binary search

def binsearch(l1, x):
    beg = 0
    last = len(l1) - 1
    while beg <= last:
        mid = (beg + last) // 2
        if x == l1[mid]:
            return mid
        elif x > l1[mid]:
            beg = mid + 1
        else:
            last = mid - 1
    else: 
        return False

n = int(input("Enter the size of array: "))
l1 = [int(input("Enter your number:")) for i in range(n)]
l1.sort()
print("Your list is:", l1)
x = int(input("Enter the number you want to search:"))
print("Number not found") if binsearch(l1, x) == False else print(x, "is at index position:", binsearch(l1, x))