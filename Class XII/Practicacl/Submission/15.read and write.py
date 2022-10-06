# write a fucntion that reads a file and copies all lines that start with a lower case letter onto another file

def copy(file):
    f1 = open(file, 'r')
    f2 = open("H:\\School\\Online classes Python\\07 July\\July Week 5\\files\\read and write.txt", 'w')
    x = ' '
    while x:
        x = f1.readline()
        if x == '':
            break
        if x[0].islower():
            f2.write(x)
    f1.close()
    f2.close()
            
file = "H:\\School\\Online classes Python\\07 July\\July Week 4\\test.txt"

copy(file)
f = open("H:\\School\\Online classes Python\\07 July\\July Week 5\\files\\read and write.txt", 'r')
str = f.read()
print(str)