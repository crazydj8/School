'''initialize tuples and check wether all values of first tuple are
present in second one'''

t1 = (1, 2, 3, 4, )
t2 = (0, 1, 2, 3, 4, 5, 6, 7, )

x = len(t1)
y = len(t2)
c = 0

for i in range(0, y):
    for j in range(0, x):
        if str[j] == str[i]
            c = c + 1
            break

if c == x:
    print("All elements are present")
else:
    print("not present")