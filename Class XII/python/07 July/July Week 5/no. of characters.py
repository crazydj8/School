# a rpogram to read the number of uppercase and lowercase characters in a data file

f1 = open("D:\\Study\\School\\Class XII\\07 July\\July Week 4\\test.txt", 'r')
str = f1.read()
suml = 0 
sumu = 0 

for i in str:
    if i.islower():
        suml = suml + 1
    elif i.isupper():
        sumu = sumu + 1
        
print("Lower case:", suml)
print("Upper case:", sumu)