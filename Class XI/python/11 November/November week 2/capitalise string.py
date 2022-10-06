'''read a string with multiple words and capitalise first letter of each 
word'''

str1 = input("Enter your string:")
str2 = ""

y = len(str1)
start = 0

for i in range(0, y):
    if i==0:
        str2 = str2 + str1[i].upper()
    else:
        if str1[i].isspace():
            str2 = str2 + " " + str1[i+1].upper()
            
        else:
            str2 = str2 + str1[i]
        print (str2)
print (str2)