# write a program to create a file and write marks of students

f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\student.dat", "w")

for i in range(0, 3):
    rno = input("Enter Roll. no.:")
    nm = input("Enter name:")
    m1 = input("Enter marks in physics:")
    m2 = input("Enter marks in chemistry:")
    m3 = input("Enter marks in maths:")
    str = rno + " " + nm + " " + m1 + " " + m2 + " " + m3 + "\n"
    f1.write(str)
    
f1.close()
f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\student.dat", "r")

x = ' '
while x:
    x = f1.readline()
    if x == '':
        break
    l = x.split(" ")
    for i in range(2, 5):
        p = 1
        print(l[i], "< 40")
        if int(l[i]) < 40:
            p = 0
            break
    if p == 1:
        print(l[1], "has passed")
    
    
    
    