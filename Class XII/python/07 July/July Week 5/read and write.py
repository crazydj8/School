# write a fucntion that reads a file and copies all lines that start with a lower case letter onto another file

def copy(str):
    f1 = open(str, 'r')
    f2 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\read and write.txt", 'w')
    x = ' '
    while x:
        x = f1.readline()
        if x == '':
            break
        if x[0].islower():
            f2.write(x)
    f1.close()
    f2.close()
            
file = "D:\\Study\\School\\Class XII\\07 July\\July Week 4\\test.txt"

copy(file)
f = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\read and write.txt", 'r')
str = f.read()
print(str)