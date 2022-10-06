''' read two lists of integers and print overlapped list if they have
atleast one element in common otherwise print disjoint'''

list = []
print("(Enter 'end' to print the list)")

n = input("Enter the element:")
list.append(n)

while n != "end":
    n = input("Enter element:")
    if n != "end":
        list.append(n)

lst2 = []
print("(Enter 'end' to print the list)")

m = input("Enter the element:")
lst2.append(m)

while m != "end":
    m = input("Enter element:")
    if m != "end":
        lst2.append(m)

y = len(list)
x = len(lst2)
z = 0

for i in range(0, x):
    for j in range(0, y):
        if list[i] == lst2[j]:
            z = 1
            
if z == 1:
    print("Lists are overlapped")
else:
    print("lists are Disjoint")