# write a function to read the length breadth and height of a cuboid and return its volume

def vol(x, y=7, z=9):
    vol = x*y*z
    return (vol)

l = int(input("Enter the length in cm:"))
b = int(input("Enter the breadth in cm:"))
h = int(input("Enter the height in cm:"))

print("Volume =", vol(l, b, h), "sq. cm")
print("Volume with specified height(9cm) =", vol(l, b), "sq. cm")
print("Volume with specified breadth(7cm) and height(9cm) =", vol(l), "sq. cm")

# specifying parameter in a statement

print("Volume with specified length(9cm) breadth(7cm) and height(9cm) =", vol(x=9, y=7, z=9), "sq. cm")