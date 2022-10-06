# program to write in a file

f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\student.dat", "a")

for i in range(0, 3):
    a = input("Enter name:")
    f1.write(a)
    f1.write("\n")
    
f1.close()
print("File closed")

f1 = open("H:/student.dat", "r")
x = f1.read()
print(x)