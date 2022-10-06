# generate first 10 terms of a fibonacci series in a tuple

t1 = (0, 1, )

for i in range(0, 8):
    num3 = t1[i] + t1[i+1]
    t1 = t1 + (num3, )
    
print (t1)