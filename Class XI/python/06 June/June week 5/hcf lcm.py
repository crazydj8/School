# read two numbers and find their hcf and lcm

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if a > b:
    s = b
elif a < b:
    s = a

for i in range(1, s+1):
    if a % i == 0 and b % i == 0:
        hcf = i

print ("HCF=", hcf)

lcm = (a * b) / hcf

print ("LCM=", lcm)
