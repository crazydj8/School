''' read the char and a string and check how many times char appears 
in string'''

str = input("Enter the string:")
let = input("Enter the character:") 

suma = 0

for i in str:
    if i == let:
        suma = suma + 1

print (suma)
