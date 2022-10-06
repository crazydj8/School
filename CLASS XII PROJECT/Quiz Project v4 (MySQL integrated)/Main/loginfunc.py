import mysql.connector as mycon
mydb = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "Quiz")
mycursor = mydb.cursor()

#Error check for blanks
def error(ent):
    x = ent.get()
    if x == "" :
        return(False)
    else:
        return(True)
        
#Check for username and password  
def check(a, b, lbl):
    mydb.commit()
    st = "select * from admin"
    mycursor.execute(st)
    l = mycursor.fetchall()
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
def login(a, b , lbl, frame1, frame2):
    if x == 1:
        s = check(a, b , lbl)
        if s == True:
            frame1.tkraise()
    elif x == 2:
        s = check(a, b, lbl)
        if s == True:
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
    mydb.commit()
    st = "select username from admin"
    mycursor.execute(st)
    l = mycursor.fetchall()
    combostyle.theme_use(cstyle1)
    if len(l) != 0:
        combo_box["values"] = l
        combo_box.current(0)
    else:
        combo_box["values"] = () 
        combo_box.set("")
  