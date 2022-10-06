import mysql.connector as mycon
mydb = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "qna")
mycursor = mydb.cursor()


def value(x):
    return(int(x.get()))

def error(ent):
    x = ent.get()
    if x == "" :
        return(False)
    else:
        return(True)

def showques(lbl1, lbl2, x, z):
    y = value(x)
    q = z.get()
    st1 = "select Question from {};".format(q)
    mycursor.execute(st1)
    qlist = mycursor.fetchall()
    
    st2 = "select Answer from {};".format(q)
    mycursor.execute(st2)
    alist = mycursor.fetchall()
    
    lbl1["text"] = "Q" + str(y) + ". " + qlist[y-1][0]
    lbl2["text"] = "A" + str(y) + ". " + alist[y-1][0]
    
def changeques(x, ent1, ent2, lbl1, z):
    q = z.get()
    condition = 1
    e = [error(ent1), error(ent2)]
    for i in e:
        if i == False:
            condition = 0
    if condition == 1:        
        y = value(x)
        st1 = "update {} set Question = '{}', Answer = '{}' where SrNo = {};".format(q, ent1.get(), ent2.get(), y)
        mycursor.execute(st1)
        mydb.commit()
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