''' menu driven program to read two complex numbers and perform 
arithmatic operations on them'''

a = int(input("Enter the Real part of first no.:"))
b = int(input("Enter the Imaginary part of first no.:"))
c = int(input("Enter the real part of Second no.:"))
d = int(input("Enter the Imaginary part of Second no.:"))

x = complex(a, b)
y= complex(c, d)


print ("")
print("Your choices are: \n1. add -> + \n2. subtract -> - \n3. multiply -> * \n4. divide -> / \n5. exit")
n = input("Enter your choice:")

while n != "exit" or n != "5":
    if n == "+" or n == "1":
        sum = x + y
        print(x, "+", y, "=", sum)
    elif n == "-" or n == "2":
        diff = x - y
        print(x, "-", y, "=", diff)
    elif n == "*" or n == "3":
        prod = x * y
        print(x, "*", y, "=", prod)
    elif n == "/" or n == "4":
        quo = x / y
        print(x, "/", y, "=", quo)
        
    print ("")
    print("Your choices are: \n1. add -> + \n2. subtract -> - \n3. multiply -> * \n4. divide -> / \n5. exit")
    n = input("Enter your choice:")
