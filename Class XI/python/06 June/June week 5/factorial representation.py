# read a number and print its factorial representation

a = int(input("Enter the number:"))
num = 1

for n in range(1, a+1):
    num = num * n
    
    if n!=a:
        print (n, "*", end=" ")
    else:
        print (n, end=" ")
        
print ("=", num)