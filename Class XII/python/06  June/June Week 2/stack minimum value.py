#create a stack to perform push and pop operations and a third operation find min which returns smallest element on the stack

'''steps:
1) create 2 stacks s1 and s2
2) when the first element is added, push it on s1 and s2
3) when inserting other elements, push element on stack s1, compare element with top of stack s2, if element<top(s2)
4) when popping an element pop topmost element from s1, if this element is equal to top of s2, pop from s2 also'''

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
            
def findmin(x, s2):
    y = peek(s2)
    if x == y:
        itm2 = spop(s2)

s1 = []
s2 = []
while True:
    print("Your choices are: \n1. Push \n2. Pop \n3. Peek \n4. Display \n5. Exit")
    ch = int(input("Enter your choice(1/2/3/4/5):"))

    if ch == 1:
        a = int(input("Enter element to push:"))
        if isempty(s1) == True:
            push(s1, a)
            push(s2, a)
        else:
            push(s1, a)
            x = peek(s2)
            if a < x:
                push(s2, a)
 
    elif ch == 2:
        itm1 = spop(s1)
        findmin(itm1, s2)

    elif ch == 3:
        itm = peek(s1)
        print ("Top =", itm)

    elif ch == 4:
        disp(s1)
        print("Minimum value =", peek(s2))

    elif ch == 5:
        break