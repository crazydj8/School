# decimal to hexadecimal

n = int(input("Enter a decimal number:"))

hex = []
hex2 = []
a = n

while a > 0:
    n = a % 16
    if n > 9:
        hex.append(chr(55 + n))
    else:
        hex.append(chr(48+n))
    a = a // 16

y = len(hex)

for i in range(y-1, -1, -1):
    hex2.append(hex[i])
hex =  hex2    

print ("Hexadecimal equivalent =", end = " ")
for j in range(0, y):
    print (hex[j], end = "")
print ("")

z = 0
r = 0
for k in range(y-1, -1, -1):
    q = ord(hex[k])
    if hex[k].isalpha():
        q = q - 55
    elif hex[k].isdigit():
        q = q - 48
    r = r + q * (16 ** z)
    z = z + 1
    
print ("decimal again = ", r)