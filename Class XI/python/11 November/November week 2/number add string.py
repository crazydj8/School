#read a string, extract digits from string and add them up

str1 = input("Enter your string:")
str2 = ""

y = len(str1)
suma = 0
dig = 0

for i in range(0, y):
    if str1[i].isdigit():
        num = int(str1[i])
        suma = suma+num
        str2 = str2 + str1[i]
        dig = 1

if dig == 1:
    print (str1, "has digits", str2, "which sum up to", suma)
else:
    print ("No digit found in", str1)