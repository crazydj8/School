#File directory
import os
cwd = list(os.path.abspath(__file__))

for i in range(16):
    cwd.pop()

file1 = ""
file2 = ""
for i in cwd:
    file1 += i
    file2 += i

file1 = file1 + "Questions.txt"
file2 = file2 + "Answers.txt"
def value(x):
    return(int(x.get()))

def error(ent):
    x = ent.get()
    if x == "" :
        return(False)
    else:
        return(True)

def showques(lbl1, lbl2, x):
    y = value(x)
    q = open(file1, "r")
    qlist = []
    while True:
        r = q.readline()
        if r == "":
            break
        else:
            l = r.rstrip("\n")
            qlist.append(l)
    q.close()
    
    a = open(file2, "r")
    alist = []
    while True:
        z = a.readline()
        if z == "":
            break
        else:
            l = z.rstrip("\n")
            alist.append(l)
    a.close()
    lbl1["text"] = "Q" + str(y) + ". " + qlist[y-1]
    lbl2["text"] = "A" + str(y) + ". " + alist[y-1]
    
def changeques(x, ent1, ent2, lbl1):
    condition = 1
    e = [error(ent1), error(ent2)]
    for i in e:
        if i == False:
            condition = 0
    if condition == 1:        
        y = value(x)
        q = open(file1, "r")
        qlist = []
        while True:
            r = q.readline()
            if r == "":
                break
            else:
                l = r.rstrip("\n")
                qlist.append(l)
        q.close()
        a = open(file2, "r")
        alist = []
        while True:
            z = a.readline()
            if z == "":
                break
            else:
                l = z.rstrip("\n")
                alist.append(l)
        a.close()
        qlist[y-1] = ent1.get() 
        alist[y-1] = ent2.get()
        
        q = open(file1, "w")
        for i in qlist:
            q1 = i + "\n"
            q.write(q1)
        q.close()
        a = open(file2, "w")
        for k in alist:
            a1 = k + "\n"
            a.write(a1)
        a.close()
        lbl1.configure(fg = "lime")
        lbl1["text"] = "Edited successfully"
    else:
        lbl1.configure(fg = "red")
        lbl1["text"] = "Field(s) cannot be blank"
        
def reset(ent1, ent2):
    condition = 1
    e = [error(ent1), error(ent2)]
    for i in e:
        if i == False:
            condition = 0
    if condition == 1:
        ent1.delete(0, "end")
        ent2.delete(0, "end")
        
def back(ent1, ent2, lbl1):
    ent1.delete(0, "end")
    ent2.delete(0, "end")
    lbl1["text"] = ""

def errorreset(lbl1):
    lbl1["text"] = ""