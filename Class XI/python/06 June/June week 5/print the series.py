# print series 0, 6, 8, 18, 24, 38, 48, 66, 80, 102
# series logic: (odd square)-1, (even square)+2

n = int(input("Enter the number of terms:"))

for a in range(1, n+1):
    b = a**2

    if a % 2 == 0:
        b = b + 2

    else:
        b = b - 1

    print (b)

    