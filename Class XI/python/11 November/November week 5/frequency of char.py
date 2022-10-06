# Read a text and store the characters and their frequency in a tuple

t = tuple()

str1 = input("Enter your string:")
x = len(str1)

for i in range(0, x):
    if str1.find(str1[i], 0, i)!=-1:
        pass
    else:
        count = str1.count(str1[i])
        t = t + (str1[i], count,)

print(t)