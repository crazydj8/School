# count the number of e in a string

str = input("Enter the string:")

suma = 0

for i in str:
    if i == "e" or i == "E":
        suma = suma + 1

print (suma)
