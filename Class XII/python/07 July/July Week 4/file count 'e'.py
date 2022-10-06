# write a program to read a file and count the number of words that contain letter e


f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 4\\test.txt", 'r')

str = " "
suma = 0

while str:
    str = f1.readline()
    if str == '':
        break
    l1 = list(str.split(" "))
    print(l1)
    for i in range(0, len(l1)):
        if "e" in l1[i].lower():
            suma = suma + 1

print("No. of e:", suma)