import os
cwd = list(os.path.abspath(__file__))
for i in range(18):
    cwd.pop()
file = ""
for i in cwd:
    file += i
file = file + "Configg.txt"
def value(x):
    return(str(x.get()))

def delete(x, lbl):
    y = value(x)
    c = open(file, "r")
    l1 = []
    while True:
        c1 = c.readline()
        if c1 == "":
            break 
        else:
            l = c1.rstrip("\n").split(",")
            l1.append(l)
    c.close()
    d = len(l1)
    for i in range(d):
        nm = l1[i][0]
        if nm == y:
            l1.pop(i)
            break
    C = open(file, "w")
    for j in l1:
        a = j[0]
        b = j[1]
        str = a + "," + b + "\n"
        C.write(str)
    C.close()    
    lbl["text"] = "Deleted succesfully"

def home(lbl):
    lbl["text"] = ""