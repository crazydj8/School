#write a menu driven program to add, subtract, multiply, transpose, find sum of both diagonal's elements, print the upper and lower triangle. read the no of rows and columns for the two matrices and perform above mentioned  


print("For the Matrices->")
deg = int(input("Enter the degree of square matrix:"))

print("For first Matrix->")
m1 = []
for i in range(0, deg):
    r = []
    for j in range(0, deg):
        x = int(input("Enter your element at ("+str(i)+","+str(j)+"):"))
        r.append(x)
    m1.append(r)
    
print("For second Matrix->")    
m2 = []
for i in range(0, deg):
    r = []
    for j in range(0, deg):
        x = int(input("Enter your element at ("+str(i)+","+str(j)+"):"))
        r.append(x)
    m2.append(r)
    
print("Your matrices are->")
print("Matrix 1=")
for i in range(0, deg):
    for j in range(0, deg):
        print(m1[i][j], end = " ")
    print("")
    
print("Matrix 2=")
for i in range(0, deg):
    for j in range(0, deg):
        print(m2[i][j], end = " ")
    print("")

def sum(m1, m2):
    deg = len(m1)
    m3 = [] #m3 = m1 + m2
    for i in range(0, deg):
        row = []
        for j in range(0, deg):
            x = m1[i][j] + m2[i][j]
            row.append(x)
        m3.append(row)
    return (m3)
    
def diff(m1, m2):
    deg = len(m1)
    m3 = [] #m3 = m1 + m2
    for i in range(0, deg):
        row = []
        for j in range(0, deg):
            x = m1[i][j] - m2[i][j]
            row.append(x)
        m3.append(row)
    return (m3)

def trans(m1):
    m3 = []
    for i in range(0, len(m1)):
        row = []
        for j in range(0, len(m1)):
            x = m1[j][i]
            row.append(x)
        m3.append(row)
    print("The transpose is:")
    for i in range(0, len(m3)):
        for j in range(0, len(m3)):
            print(m3[i][j], end = " ")
        print("")

def sumdiag(m1):
    x = 0
    for i in range(0, len(m1)):
        x = x + m1[i][i]
    j = len(m1)
    y = 0
    for i in range(0, len(m1)):
        y = y + m1[i][j-1]
        j = j - 1
    return(x, y)

def tri(m1):
    print("Lower triangle:")
    for i in range(0, len(m1)):
        for j in range(0, i+1):
            print(m1[i][j], end = " ")
        print ("")
    print("Upper triangle:")
    for i in range(0, len(m1)):
        if i == 0:
            for j in range(0, len(m1)):
                print(m1[i][j], end = " ") 
            print ("")
        else:
            for j in range(0, len(m1)):
                if i > j:
                    print(" ", end = " ")
                else:
                    print(m1[i][j], end = " ") 
            print ("")    

def prod(m1, m2):
    m3 = []
    for i in range(0, len(m1)):
        row = []
        for j in range(0, len(m1)):
            x = 0
            for k in range(0, len(m2)):
                x = x + m1[i][k] * m2[k][j]
            row.append(x)
        m3.append(row)
    return(m3)

print("Your choices are: \n1. add(+) \n2. subtract(-) \n3. multiply(*) \n4. transpose(trans) \n5. Print upper and lower triangle(tri) \n6. Sum of Diagonals(sumd) \n7. Exit(exit)")
n = input("Enter your choice:")

while n != "exit" and n != "7":
    if n == "+" or n == "1":
        x = sum(m1, m2)
        print("Sum =")
        for i in range(0, len(x)):
            for j in range(0, len(x)):
                print(x[i][j], end = " ")
            print("")
                
    elif n == "-" or n == "2":
        x = diff(m1, m2)
        print("Difference =")
        for i in range(0, len(x)):
            for j in range(0, len(x)):
                print(x[i][j], end = " ")
            print("")
        
    elif n == "*" or n == "3":
        x = prod(m1, m2)
        print("Product =")
        for i in range(0, len(x)):
            for j in range(0, len(x)):
                print(x[i][j], end = " ")
            print("")
        
    elif n == "trans" or n == "4":
        condition = 0
        while condition == 0:
            x = int(input("Which matrix do you want to transpose (1 or 2):"))
            if x == 1:
                trans(m1)               
                condition = 1
            elif x == 2:
                trans(m2)
                condition = 1 
            else:
                print("Please input 1 or 2")
    elif n == "tri" or n == "5":    
        condition = 0
        while condition == 0:
            x = int(input("Which matrix do you want to print triangles of (1 or 2):"))
            if x == 1:
                tri(m1)
                condition = 1
            elif x == 2:
                tri(m2)
                condition = 1
            else:
                print("Please input 1 or 2")
    elif n == "sumd" or n == "6":
        condition = 0
        while condition == 0:
            x = int(input("Which matrix do you want the sum of diagonals of(1 or 2):"))
            if x == 1:
                y = sumdiag(m1)
                (a, b) = y
                print("Sum of Left Diagonal =", a)
                print("Sum of Right Diagonal =", b)
                condition = 1
            elif x == 2:
                y = sumdiag(m2)
                (a, b) = y
                print("Sum of Left Diagonal =", a)
                print("Sum of Right Diagonal =", b)
                condition = 1
            else:
                print("Please input 1 or 2")
        
    print ("")
    print("Your choices are: \n1. add(+) \n2. subtract(-) \n3. multiply(*) \n4. transpose(trans) \n5. Print upper and lower triangle(tri) \n6. Sum of Diagonals(sumd) \n7. Exit(exit)")
    n = input("Enter your choice:")

    
    
    
    
    
    
    
    
    
    
    
    
    