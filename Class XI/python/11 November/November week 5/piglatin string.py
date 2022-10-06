# generate a piglatin string

str1 =  input("Enter your string:")
str1 = str1 + " " 
str2 = ""

y = len(str1)
first = 0
x = 1

for i in range(0, y):
    if x == 1:
        x = 0
        first = str1[i]
        continue
    if str1[i] == " ":
        x = 1
        str2 = str2 + first
        str2 = str2 + "a"
    str2 = str2 + str1[i]
    

print (str2)