#File directory
import os 
cwd = list(os.path.abspath(__file__))

for i in range(17):
    cwd.pop()

file = ""

for i in cwd:
    file += i

file = file + "Configg.txt"
#Error check for blanks
def error(ent):
    x = ent.get()
    if x == "" :
        return(False)
    else:
        return(True)
#Check for username and password  
def check(a, b, lbl):
    c = open(file, "r")
    l = []
    while True:
        x = c.readline()
        if x == "":
            break
        else:
            list = x.rstrip("\n").split(",")
            l.append(list)
    c.close()
    id = a.get()
    pwd = b.get()
    y = [error(a), error(b)]
    condition = 1
    lerror = -1
    for i in y:
        if i == False:
            condition = 0
    if len(l) != 0:
        if condition == 1:
            for k in l:
                lerror = 0
                if k[0] == id:
                    if k[1] == pwd:
                        return True
                    else:
                        lbl["text"] = "Invalid Password"
                        b.focus_set()
                    break
                else:   
                    lerror = 1
        elif condition == 0:
            lbl["text"] = "Field(s) cannot be blank"
            a.focus_set()
        
        if lerror == 1:
            lbl["text"] = "Username does not exist"
            a.focus_set()
    else:
        lbl["text"] = "No admins found, please register"
        a.focus_Set()
#Function for login
def login(a, b , lbl, frame1, frame2, combo_box, combostyle, cstyle1):
    if x == 1:
        s = check(a, b , lbl)
        if s == True:
            frame1.tkraise()
    elif x == 2:
        s = check(a, b, lbl)
        if s == True:
            combobox(combo_box, combostyle, cstyle1)
            frame2.tkraise()
#Reseting labels 
def reset(a, b, lbl):
    if check(a, b, lbl) == True:
        a.delete(0,"end")
        b.delete(0,"end")
        lbl["text"] = ""

def goback(a, b, lbl, frame1, frame2):
    a.delete(0, "end")
    b.delete(0, "end")
    lbl["text"] = ""
    global x
    if x == 1:
        frame1.tkraise()
    else:
        frame2.tkraise()

def adminbtn(frame, ent1):
    global x
    x = 1
    frame.tkraise()
    ent1.focus_set()
    
def start(frame):
    global x
    x = 2
    frame.tkraise()

def combobox(combo_box, combostyle, cstyle1):
    c = open(file, "r")
    t = ()
    while True:
        x = c.readline()
        if x == "":
            break
        else:
            p = x.find(",")
            str = x[:p]
            t += (str,)
    c.close()
    combostyle.theme_use(cstyle1)
    if len(t) != 0:
        combo_box["values"] = t
        combo_box.current(0)
    else:
        combo_box["values"] = () 
        combo_box.set("")