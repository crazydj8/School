# read a number and check if it is a cyclic prime
# 113 is cyclic prime and so is 131 and 311

n = int(input("Enter your number:"))

c = 0
s = str(n)
num = len(s)
no = n

while(c <= num-1):

    for i in range(2, n):
        if n % i == 0:
            break
    if i == (n-1):
        r = n % 10
        q = n // 10
        no = r * (10 ** (num-1)) + q
        n = no
    else:
        break

    c = c + 1    

if c == num :
    print ("Cyclic prime")
else:
    print ("Not cyclic prime")