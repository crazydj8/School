# print a given string in reverse

str = input("Enter the string:")

x = len(str)

for i in range(-1, (-x-1), -1):
    print (str[i], end="")
