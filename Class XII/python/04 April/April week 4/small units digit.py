# write a function that takes 2 numbers and returns a number that has a smaller ones digit. default values for numbers are 158 and 233. call function in all possible ways

def small(x=158, y=233):
    if x%10 > y%10:
        return y
    elif x%10 < y%10:
        return x

print("Number with smaller units place =", small())
print("Number with smaller units place =", small(25))
print("Number with smaller units place =", small(y = 66))
print("Number with smaller units place =", small(x = 50, y = 221))

