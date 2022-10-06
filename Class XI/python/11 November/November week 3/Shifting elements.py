'''shift elements of a list such that element at nth position moves to
n+1 position and last element moves to first'''

list = eval(input("Enter your list(Elements separated by a ','):"))
lst2 = []

y = len(list)

for i in range(0, y):
    if i == y-1:
        lst2.insert(0, list[i])
        break
    lst2.append(list[i])

print (lst2)