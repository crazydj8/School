# conversion from decimal to binary

n = int(input("Enter a decimal number:"))

bin = []
bin2 = []
a = n

while a > 0:
    r = a % 2
    a = a // 2
    bin.append(r)

y = len(bin)

for i in range(y-1, -1, -1):
    bin2.append(bin[i])
    
bin =  bin2    

print ("binary equivalent =", end=" ")
for j in range(0, y):
    print (bin[j], end = "")
print ("")

z = 0
r = 0
for k in range(y-1, -1, -1):
    r = r + bin[k] * (2 ** z)
    z = z + 1
    
print ("decimal again = ", r)