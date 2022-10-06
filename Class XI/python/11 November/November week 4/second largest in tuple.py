'''initialize a tuple of 10 numbers and find the second largest number 
from the tuple'''

t1 = (0, 5, 8, 10, 43, 56, 600, 72, 95, 88, )

x = len(t1)
a = max(t1)
large = -1

for i in range(0, x):
    if t1[i] < a:
        if t1[i] > large:
            large = t1[i]

print ("Second largest number=", large)
    