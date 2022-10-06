# read a file that contains name and phone number and splits it into two separate files

f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\namandphon.txt", 'r')
f2 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\name.txt", 'a')
f3 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 5\\files\\phone.txt", 'a')

x = ' '
while x:
    x = f1.readline()
    if x == '':
        break
    l = x.split(" ")
    for i in l:
        #print("x",i)
        if i.isalnum():
            f3.write(i)
            f3.write("\n")
        elif i.isalpha():
            f2.write(i)
            f2.write("\n")

f1.close()
f2.close()
f3.close()