import mysql.connector as mycon
mydb = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "Quiz")
mycursor = mydb.cursor()

def error1(ent):
    x = ent.get()
    if x == "" :
        return(False)
    else:
        return(True)
def error2(ent):
    x = ent.get('1.0', "end")
    if x == "" :
        return(False)
    else:
        return(True)

def check(a, b, lbl):
    y = [error1(a), error2(b)]
    condition = 1
    for i in y:
        if i == False:
            condition = 0
    if condition == 0:
            lbl["text"] = "Field(s) cannot be blank"
            a.focus_set()
    else:
        return (True)

def submit(a, b, lbl, btn):
    if check(a, b, lbl) == True:
        st = "insert into feedback value('{}', '{}');".format(a.get(), b.get('1.0', "end").rstrip("\n"))
        mycursor.execute(st)
        mydb.commit()
        lbl.config(fg = "lime")
        lbl["text"] = "Feedback Submitted! Please click Home"
        a.config(state = "disabled")
        b.config(bg = "white", fg = "gray", state = "disabled")
        btn.config(state = "disabled")

def home(a, b, lbl, btn):
    a.config(state = "normal")
    a.delete(0, "end")
    b.config(bg = "black", fg = "lime", state = "normal")
    b.delete("1.0", "end")
    lbl["text"] = ""
    btn.config(state = "normal")