# write a program to read a file and count the number of line and count the number of vowels

f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 4\\test.txt", 'r')

vow = 0
str = " "

while True:
    str = f1.readline()
    if str == '':
        break
    for x in str:
        if x.lower() in ("a", "e", "i", "o", "u"):
            vow = vow + 1
f1.seek(0)            
str = f1.read()  
#str1 = str.rstrip()
lin = str.count("\n")

print("number of lines=", lin+1)
print("number of vowels=", vow)