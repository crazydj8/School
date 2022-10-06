# evaluate postfix to infix

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
        return top[stk]
        
        
exp = input("Enter Expression: ")
l1 = list(exp)
print(l1)
#l1 = ["2", "3", "+", "4", "5", "+", "*", "5", "/"]
s1 = []
top1 = None

for i in range(0, len(l1)):
    if l1[i].isdigit():
        push(s1, int(l1[i]))   
    else:
        op1 = spop(s1)
        op2 = spop(s1)
        if l1[i] == "+":
            x = op2 + op1
        elif l1[i] == "-":
            x = op2 - op1
        elif l1[i] == "*":
            x = op2 * op1
        elif l1[i] == "/":
            x = op2 / op1    
        elif l1[i] == "^":
            x = op2 ** op1
        push(s1, x)   
    print (s1)
print("Answer =", spop(s1))

