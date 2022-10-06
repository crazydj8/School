#menu driven program for queue operations

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

queue = []
while True:
    print("Your choices are: \n1. Enqueue \n2. Dequeue \n3. Peek \n4. Display \n5. Exit")
    ch = int(input("Enter your choice(1/2/3/4/5):"))
    if ch == 1:
        a = int(input("Enter element to enqueue:"))
        enq(queue, a)
    elif ch == 2:
        itm = deq(queue)
        if itm == "Underflow":
            print(itm)
    elif ch == 3:
        itm = peek(queue)
        print ("Front =", itm)
    elif ch == 4:
        disp(queue)
    elif ch == 5:
        break