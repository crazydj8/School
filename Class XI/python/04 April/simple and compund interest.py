# calculate simple and compound interest

p = int(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = int(input("Enter the time(in years): "))

si = (p * r * t) / 100
ci = p * (1 + (r / 100)) ** t

print ("Simple Interest= ", si)
print ("Compound Interest= ", ci)

