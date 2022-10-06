# read the numbers and find out largest even and largest odd

a = int(input("Enter the number of inputs:"))

le = 0
lo = 0
flge = 0
flgo = 0

for i in range(0, a):
    a = int(input("Enter number:"))
    if i == 0:
        if a % 2 == 0:
            le = a
            flge = 1
        else:
            lo = a
            flgo = 1

    else:
        if a % 2 == 0:
            if flge == 0:
                le = a
                flge = 1
            else:
                if a > le:
                    le = a

        else:
            if flgo == 0:
                lo = a
                flgo = 1
            else:
                if a > lo:
                    lo = a

if le == 0:
    flge = 0
if lo == 0:
    flgo = 0

if flge == 1 and flgo == 1:

        print ("Largest even=", le)
        print ("Largest odd=", lo)

elif flge == 0 and flgo == 1:

        print ("No even number found")
        print ("Largest odd=", lo)

elif flge == 1 and flgo == 0:

        print ("Largest even=", le)
        print ("No odd number found")

