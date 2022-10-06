import time
import mysql.connector as mycon
mydb1 = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "Quiz")
mycursor1 = mydb1.cursor()
mydb2 = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "qna")
mycursor2 = mydb2.cursor()


userans = []
score = 0
loop = True
    
def error(ent, lbl):
    x = ent.get()
    if x == "" :
        ent.insert(0, " ")
    return True

def nextframe(ent, lbl, frame):
    if error(ent, lbl) == True:
        frame.tkraise()
    
def play(ent, frame, lbl, q1, q2, q3, q4, q5, z):
    q = z.get()
    if error(ent, lbl) == True:
        frame.tkraise()
        
        global l1, l2
        st1 = "select Question from {};".format(q)
        mycursor2.execute(st1)
        l1 = mycursor2.fetchall()
        st2 = "select Answer from {};".format(q)
        mycursor2.execute(st2)
        l2 = mycursor2.fetchall()

        q1["text"] = "Q1. " + l1[0][0]
        q2["text"] = "Q2. " + l1[1][0]
        q3["text"] = "Q3. " + l1[2][0]
        q4["text"] = "Q4. " + l1[3][0]
        q5["text"] = "Q5. " + l1[4][0]
        
def savename(ent, lbl):
    global nm
    if ent.get() != "":
        nm = ent.get()

def reset(ent, lbl, tlbl):
    if error(ent, lbl) == True:
        ent.delete(0, "end")
        lbl["text"] = ""
        tlbl.config(fg = "lime")
    
def back(ent, lbl):
    ent.delete(0, "end")
    lbl["text"] = ""

def answer(lbl, entry, lbl1):
    if error(entry, lbl1) == True:
        global l2, score
        x = lbl.cget("text")
        n = int(x[-1])
        if entry.get().lower() == l2[n-1][0].lower():
            score += 1


def scores(entry, lbl1):
    if error(entry, lbl1) == True:
        global nm, score
        st = "insert into scores value('{}', {})".format(nm, score)
        mycursor1.execute(st)
        mydb1.commit()
    
def finish(lbl1, lbl2, entry, lbl3):
    if error(entry, lbl3) == True:
        global nm, score
        lbl1["text"] = "Your name: "+ nm
        lbl2["text"] = "Your score: "+ str(score)

def take(entry, lbl):
    if error(entry, lbl) == True:
        global userans
        userans.append(entry.get())

def analyse(lbl1, lbl2, lbl3, lbl4, lbl5, clbl1, clbl2, clbl3, clbl4, clbl5):
    global userans, l2
    for i in [lbl1, lbl2, lbl3, lbl4, lbl5]:
        i.config(fg = "lime")
    lbl1["text"] = userans[0]
    if userans[0].lower() != l2[0][0].lower():
        lbl1.config(fg = "red")
    lbl2["text"] = userans[1]
    if userans[1].lower() != l2[1][0].lower():
        lbl2.config(fg = "red")
    lbl3["text"] = userans[2]
    if userans[2].lower() != l2[2][0].lower():
        lbl3.config(fg = "red")
    lbl4["text"] = userans[3]
    if userans[3].lower() != l2[3][0].lower():
        lbl4.config(fg = "red")
    lbl5["text"] = userans[4]
    if userans[4].lower() != l2[4][0].lower():
        lbl5.config(fg = "red")
    clbl1["text"] = l2[0][0]
    clbl2["text"] = l2[1][0]
    clbl3["text"] = l2[2][0]
    clbl4["text"] = l2[3][0]
    clbl5["text"] = l2[4][0]
    
def analyseques(lbl1, lbl2, lbl3, lbl4, lbl5):
    global l1
    lbl1["text"] = "Q1. " + l1[0][0]
    lbl2["text"] = "Q2. " + l1[1][0]
    lbl3["text"] = "Q3. " + l1[2][0]
    lbl4["text"] = "Q4. " + l1[3][0]
    lbl5["text"] = "Q5. " + l1[4][0]
    
def scorereset():
    global score, userans
    score = 0
    userans = []

    
def time1(s, tlbl, ent1, errorlbl, window):
    global loop
    loop = True
    temp = int(s.get())
    tlbl["text"] = "Time left: " + s.get()
    while loop:
        s.set("{}".format(temp))
        window.update()
        tlbl["text"] = "Time left: " + s.get()
        time.sleep(1)
        if temp == 5:
            tlbl.config(fg = "red")
        if temp == 0:
            if ent1.get() == "":
                ent1.delete(0, "end")
                ent1.insert(0, " ")
            errorlbl.config(fg = "lime")
            errorlbl["text"] = "Autosaved, Please click Next!"
            ent1.config(state= "disabled")           
            break
        temp -= 1

def destroy(entry, lbl1):
    global loop
    if error(entry, lbl1) == True:
        loop = False

def setvar(l):
    for i in l:
        i.set("30")

    