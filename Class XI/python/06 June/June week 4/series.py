# program will print the given series

n = int(input("Enter the limit:"))


for a in range(1, n, 3):
    if a % 2 == 1:
        print (a)
    elif a % 2 == 0:
        print (-a)