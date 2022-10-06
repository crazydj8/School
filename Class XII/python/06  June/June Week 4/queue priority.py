#a program to implement 3 queues highestpr, normalpr, lowestpr: the program accepts element alongwith its priority

'''eg. element: KP213
       priority(H/N/L):H
       then menu offers following:
       1.insert element
       2. search for element
       3. change priority
option 1: element is inserted in either list depending on priority
option 2: ask for an elemet to be searched, display the q in which it is, display its priority
option 3: ask for element, if it exists in any q, ask for new priority, and change the q and remove it from previous q'''

def isempty(q):
    if q == []:
        return True
    else:
        return False

def enq(q, x):
    q.append(x)
    if len(q) == 1:
        front = 0 
        rear = 0
    else :
        rear = len(q) - 1
    
def deq(q):
    if isempty(q):
        return("Underflow")
    else :
        item = q.pop(0)
    return (item)
   
def peek(q):
    if isempty(q):
        return "Underflow"
    else :
        return (q[0])

def disp(q):
    if isempty(q):
        print("Q is empty")
    else:
        rear = len(q) - 1
        for i in range(0, rear+1):
            print (q[i])
            
def search(q, a):
    for i in range(0, len(q)):
        if q[i] == a:
            return True
        else:
            return False
            
hq = []
nq = []
lq = []

while True:
    print("Your choices are: \n1. Insert element \n2. Search for element \n3. Change Priority \n4. Exit")
    ch = int(input("Enter your choice(1/2/3/4):"))
    
    if ch == 1:
        condition = 1
        a = input("Enter your element:")
        while condition == 1:
            pr = input("Enter your priority(H/N/L):")
            if pr == "H" or pr == "N" or pr == "L":
                condition = 0
            else:
                print("Please enter H or N or L")
        if pr == "H":
            enq(hq, a)
            print("Element added to Hqueue successfully")
        elif pr == "N":
            enq(nq, a)
            print("Element added to Nqueue successfully")
        elif pr == "L":
            enq(lq, a)
            print("Element added to Lqueue successfully")
            
    elif ch == 2:
        a = input("Enter the element to be searched:")
        if search(hq, a):
            print("Your element is in Hq:")
            disp(hq)
            print("Its priority is High")
        elif search(nq, a):
            print("Your element is in Nq:")
            disp(nq)
            print("Its priority is Normal")
        elif search (lq, a):
            print("Your element is in Lq:")
            disp(lq)
            print("Its priority is Low")
        else:
            print("Element not found")
            
    elif ch == 3:
        a = input("Enter the element you want to change priority of:")
        pr = input("Enter new priority:")
        condition = 0
        if search(hq, a):
            hq.remove(a)
            condidtion = 1
        elif search(nq, a):
            nq.remove(a)
            condidtion = 1
        elif search (lq, a):
            lq.remove(a)
            condidtion = 1
        else:
            print("Element not found")
        if condition == 1:
            if pr == "H":
                enq(hq, a)
            elif pr == "N":
                enq(nq, a)
            elif pr == "L":
                enq(lq, a)        
    
    
    
    
    
    