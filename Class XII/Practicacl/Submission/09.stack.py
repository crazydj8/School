#menu driven program for stack operations

def isempty(stk):
    if stk == []:
        return True
    else:
        return False
        
def push(stk, x):
    stk.append(x)
    top = len(stk) - 1
    
def spop(stk):
    if isempty(stk):
        print ("Underflow")
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return (item)
    
def peek(stk):
    if isempty(stk):
        return ("Underflow")
    else:
        top = len(stk) - 1
        return stk[top]
        
def disp(stk):
    if isempty(stk):
        print("Empty")
    else:
        top = len(stk) - 1
        for i in range(top, -1, -1):
            print(stk[i])

stack = []
while True:
    print("Your choices are: \n1. Push \n2. Pop \n3. Peek \n4. Display \n5. Exit")
    ch = int(input("Enter your choice(1/2/3/4/5):"))
    if ch == 1:
        a = int(input("Enter element to push:"))
        push(stack, a)
    elif ch == 2:
        itm = spop(stack)
    elif ch == 3:
        itm = peek(stack)
        print ("Top =", itm)
    elif ch == 4:
        disp(stack)
    elif ch == 5:
        break