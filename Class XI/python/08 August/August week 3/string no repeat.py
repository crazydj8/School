# read a string and print the string again without repeated characters

string = input("Enter your string:")
x = len(string)
y=0
for i in range(0, x):
    for y in range(i-1, -1, -1):
        if string[y] == string [i]:
            break
    if y == 0:
        a = string.count(string[i])
        print (string[i], a)