''' inititalize a list of numbers and shift all zeroes to the right and 
non zeroes to left of the list'''

list = [43, 0, 56, 8, 5, 7, 0, 2, 1, 0]

y = len(list)

for i in range(0, y):
    if list[i] == 0:
        list.append(list[i])
        list.remove(list[i])
print (list)