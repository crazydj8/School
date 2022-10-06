'''take a string, start limit and number display string from start limit
till no. of characters'''

string = input("Enter your string:")
x = int(input("Enter starting limit:"))
n = int(input("Enter no. of characters:"))
y = len(string)
l = x + n
print ("")

for i in range(x, l):
    print (string[i-1], end="")
    if i >= y:
        break
print ("")