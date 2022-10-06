# read a list of n elements and then exchange the consecutive terms 

list = []
print("(Enter 'end' to print the list)")

n = input("Enter the element:")
list.append(n)

while n != "end":
    n = input("Enter element:")
    if n != "end":
        list.append(n)

print (list)

y = len(list)

if y % 2 == 0:
    for i in range(0, y, 2):
        b = list[i]
        list[i] = list[i+1] 
        list[i+1] = b
else:
    for i in range(0, y-1, 2):
        b = list[i]
        list[i] = list[i+1] 
        list[i+1] = b
    
print(list)