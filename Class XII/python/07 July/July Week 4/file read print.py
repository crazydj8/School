#write a program to read a file and count number of lines starting with w or ending with e

f1 = open("D:\\Study\\School\\Class XII\\mysql queries.txt", 'r')
str = ' '
ctw = 0
cte = 1
while True:
    str = f1.readline()
    if str == '':
        break
    if str[0] == 'w':
        ctw = ctw + 1
        print(str)
    elif str[-1] == 'e':
        cte = cte + 1
        print(str)
      
        
f1.close()

print("Lines starting with 'w':", ctw)
print("Lines ending with 'e':", cte)
