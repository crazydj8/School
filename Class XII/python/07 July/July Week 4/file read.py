'''f1 = open("C:\\Users\\Dell\\Desktop\\Online classes Python\\mysql queries.txt", 'r')
str = f1.read()
print(str)
siz = len(str)
print('size=', siz)

f1.seek(0)#reposition file pointer to the position 0

str = f1.read(50)#read will start at 0 and end at 50
print(str)
str = f1.read(50)#file pointer is already at 50 and reads next 50 characters
print(str) 

f1.close()'''

f1 = open("D:\\Study\\School\\Class XII\\mysql queries.txt", 'r')
str = " "
while str:
    str = f1.readline()
    print(str)

f1.close()