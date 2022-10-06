'''store name and price of five products in a tuple and display products
with highest and lowest price'''
    
t1 = (("Laptop", 70000), ("Camera", 30000), ("Video game", 1200), ("Bicycle", 11000,), ("Heater", 15000), )

x = len(t1)
small = t1[i][1]
large = t1[i][1]

for i in range(1, x):
    if t1[i][1]<small:
        small = t1[i][1]
        names = t1[i][0]
    elif t1[i][1]>large:
        large = t1[i][1]
        namel = t1[i][0]

print("Most Expensive product:", namel, ", Price:", large)
print("Cheapest product:", names, ", Price:", small)
