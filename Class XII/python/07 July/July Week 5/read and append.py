# program to read 2 filenames and append the contents of first file to second file

f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 4\\test.txt", 'r')
f2 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\read and append.txt", 'a')
x = ' '
while x:
    x = f1.readline()
    if x == '':
        break
    f2.write(x)
f1.close()
f2.close()

f = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\read and append.txt", 'r')
str = f.read()
print(str)