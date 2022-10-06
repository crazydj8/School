#File directory
import os 
cwd = list(os.path.abspath(__file__))

for i in range(18):
    cwd.pop()

file = ""

for i in cwd:
    file += i

file = file + "Configg.txt"
def error(ent):
    x = ent.get()
    if x == "" :
        return(False)
    else:
        return(True)    
        
def check(a, b, c, lbl):
    f = open(file, "r")
    l = []
    while True:
        x = f.readline()
        if x == "":
            break
        else:
            list = x.rstrip("\n").split(",")
            l.append(list)
    f.close()
    id = a.get()
    pwd = b.get()
    cpwd = c.get()
    y = [error(a), error(b), error(c)]
    condition = 1
    serror = -1
    for i in y:
        if i == False:
            condition = 0
    if len(l) != 0:
        if condition == 1:
            for i in l:
                serror = 0
                if i[0] == id:
                    lbl["text"] = "Username already exists"
                    break
                else:
                    serror = 1
        elif condition == 0:
            lbl["text"] = "Field(s) cannot be blank"
    else:
        if pwd == cpwd:
            return True
        else:
            lbl["text"] = "Passwords do not match"
    if serror == 1:
        if pwd == cpwd:
            return True
        else:
            lbl["text"] = "Passwords do not match"

def register(a, b, c, lbl, frame):
    if check(a, b, c, lbl) == True:
        c = open(file, "a")
        id = a.get()
        pwd = b.get()
        s = id + "," + pwd + "\n"
        c.write(s)
        c.close()
        frame.tkraise()
        
def back(a, b, c, lbl):
    a.delete(0, "end")
    b.delete(0, "end")
    c.delete(0, "end")
    lbl["text"] = ""

