# write a function calc that recieves 2 numbers and returns the sum, difference and product as elements of a tuple and it returns values as independent variables

def calc(x,y):
    sum = x + y
    diff = x - y
    prod = x * y
    return (sum, diff, prod)
    
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print(calc(a,b))

sum, diff, prod = calc(a,b)

print("sum=", sum)
print("difference=", diff)
print("product=", prod)
