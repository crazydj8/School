''' read the pattern and a string and check how many times pattern 
appears in string'''

str = input("Enter the string:")
let = input("Enter the pattern:") 
x = len(let)
y = len(str)
suma = 0

for i in range(0, y):
    if (str[i]) == (let[0]):
        for j in range(0, x):
            if (let[j]) != (str[i]):
                break
            
            i = i + 1
        
        if j == x-1:
            suma = suma+ 1           
            
print (suma)