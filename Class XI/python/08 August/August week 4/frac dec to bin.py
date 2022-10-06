# convert fractional decimal to bin 

n = float(input("Enter your fractional decimal:"))

bin = []
fbin = []
binfinal = []

dec = int(n)
frac = n - dec

while dec > 0:
    r = dec % 2
    dec = dec // 2
    bin.append(r)

y = len(bin)

for i in range(y-1, -1, -1):
    binfinal.append(bin[i])
 
binfinal.append(".")

fracbin = 0
z =10
for k in range(0, 10):
    num = frac * 2
    quo = int(num)
    frac = num - quo
    if num == 1:
        break
    else:
        binfinal.append(quo)

f = len(binfinal)
print ("binary equivalent =", end=" ")
for j in range(0, f):
    print(binfinal[j], end = "")
print ("")