''' read a string and a pattern and delete all occurances of pattern in
the string'''

str1 = input("Enter your string:")
str2 = ""
text = input("Enter the pattern to search for:")

a = len(str1)
y = len(text)
start = 0

for i in range(0, a):
    find = str1.find(text,start)
    if find != -1:
        for j in range(start, find):
            str2 = str2 + str1[j]
        start = find + y
    else:
        for k in range(start, a):
            str2 = str2 + str1[k]
        break
print(str2)