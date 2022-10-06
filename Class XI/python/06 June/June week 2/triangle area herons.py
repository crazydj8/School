# calculating area of a triangle by Heron's formula
import math

a = float(input("Enter the first side:"))
b = float(input("Enter the second side:"))
c = float(input("Enter the third side:"))

s = (a + b + c) / 2
a = math.sqrt(s * (s - a) * (s - b) * (s - c))

print ("area of triangle:", a)