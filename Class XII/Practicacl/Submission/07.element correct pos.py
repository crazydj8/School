# write a function that recieves a sorted list and inserts the element in right place in ascending/descending order

def findpos(l1, x):
    siz = len(l1)
    if x < l1[0]:
        return (0)
    else:
        pos = -1
        for i in range(0, siz-1):
            if l1[i] <= x and x <= l1[i+1]:
                pos = i + 1
                break
        if pos == -1:
            pos = siz
        return (pos)
        
def shift(l1, pos):
    l1.append(0)
    siz = len(l1)
    i = siz - 1
    while i >=pos:
        l1[i] = l1[i-1]
        i = i - 1 

lst1 = [1, 16, 23, 54, 69, 80]
a = int(input("Enter the number which you want to add to your list:"))

pos = findpos(lst1, a)
shift(lst1, pos)

lst1[pos] = a

print(lst1)
print("Position of insertion:", pos)