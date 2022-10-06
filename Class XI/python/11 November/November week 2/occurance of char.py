# read a pattern and count the no. of occurances of the pattern

str1 = input("Enter your string:")
text = input("Enter the pattern to search for:")

a = len(str1)
y = len(text)
suma = 0
start = 0

for i in range(0, a):
    if i == 0:
        find = str1.find(text, start)
        
    else:
        x = start + y - 1
        find = str1.find(text, x)
        

    if find == -1:
        break
        
    else:
        suma = suma + 1
        start = find
        
print("Occurances=", suma)