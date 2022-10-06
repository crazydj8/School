import mysql.connector as mycon
mydb = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "Quiz")
mycursor = mydb.cursor()

def error(ent):
    x = ent.get()
    if x == "" :
        return(False)
    else:
        return(True)    
        
def check(a, b, c, lbl):
    st = "select * from admin"
    mycursor.execute(st)
    l = mycursor.fetchall()
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
        id = a.get()
        pwd = b.get()
        st = "insert into admin value('{}', '{}')".format(id, pwd)
        mycursor.execute(st)
        mydb.commit()
        frame.tkraise()
        
def back(a, b, c, lbl):
    a.delete(0, "end")
    b.delete(0, "end")
    c.delete(0, "end")
    lbl["text"] = ""

