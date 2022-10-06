# write a program to count the no of occurences of "to" and "the" in a data file

f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 4\\test.txt", 'r')
suma = 0 
sumb = 0

x = ' '
while x:
    x = f1.readlines()
    print(x)
    if x == "":
        break
    '''l = x.split(" ")
    print(l)
    for i in l:
        if i == "to":
            suma = suma + 1
        if i == "the":
            sumb = sumb + 1

print("No. of 'to':", suma)
print("No. of 'the':", sumb)'''