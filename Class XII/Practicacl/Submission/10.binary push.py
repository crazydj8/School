#read a number, convert to binary, push to stack and display

def isempty(stk):
    if stk == []:
        return True
    else:
        return False
        
def push(stk, x):
    stk.append(x)
    top = len(stk) 
    
def disp(stk):
    if isempty(stk):
        print("Empty")
    else:
        top = len(stk) - 1
        for i in range(top, -1, -1):
            print(stk[i])
            
def binary(n):
    a = n
    x = 0
    sum = 0

    while a > 0:
        r = a % 2
        a = a // 2
        sum = sum + r * (10 ** x)
        x = x + 1
        
    return (sum)
    
    
s1 = []    
a = int(input("Enter the number of inputs:"))
for i in range(0, a):
    x = int(input("Enter your number:"))
    y = binary(x)
    push(s1, y)
    
print("Your stack is:")
disp(s1)