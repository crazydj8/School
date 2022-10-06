''' read a string and set a start position p. look for the nth occurance of the
character at p'''

string = input("Enter your string:")
x = int(input("Enter number of the character you want to search for:"))
n = int(input("Enter no. of occurances to search for:"))

y = len(string)

suma = 0

for i in range(x+1, y):
    if string[i] == string[x]:
        suma = suma + 1
    if i > n:
        break
    print ("i=", string[i], "x=", string[x])
    print ("sum=", suma)

if suma == n:
    print ("yes")
    
else:
    print ("no")