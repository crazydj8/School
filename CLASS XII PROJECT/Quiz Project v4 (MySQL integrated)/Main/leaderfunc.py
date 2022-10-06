import mysql.connector as mycon
mydb = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "Quiz")
mycursor = mydb.cursor()

condition = 0

def takescore():
    global lscore
    mydb.commit()
    st = "select * from scores order by score desc;"
    mycursor.execute(st)
    lscore = mycursor.fetchall()
        
def main(lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10, slbl1, slbl2, slbl3, slbl4, slbl5, slbl6, slbl7, slbl8, 
    slbl9, slbl10):
    global condition, lscore, x
    name = [lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10]
    score = [slbl1, slbl2, slbl3, slbl4, slbl5, slbl6, slbl7, slbl8, slbl9, slbl10]
    takescore()
    x = len(lscore)
    if x < 10:
        for i in range(x):
            name[i]["text"] = lscore[i][0] 
            score[i]["text"] = lscore[i][1]
    elif x >= 10:
        for i in range(10):
            name[i]["text"] = lscore[i][0] 
            score[i]["text"] = lscore[i][1]
            
def lbreset(lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10, slbl1, slbl2, slbl3, slbl4, slbl5, slbl6, slbl7, 
    slbl8, slbl9, slbl10):
    lbl1["text"] = "-"
    lbl2["text"] = "-"
    lbl3["text"] = "-"
    lbl4["text"] = "-"
    lbl5["text"] = "-"
    lbl6["text"] = "-"
    lbl7["text"] = "-"
    lbl8["text"] = "-"
    lbl9["text"] = "-"
    lbl10["text"] = "-"
    slbl1["text"] = "-"
    slbl2["text"] = "-"
    slbl3["text"] = "-"
    slbl4["text"] = "-"
    slbl5["text"] = "-"
    slbl6["text"] = "-"
    slbl7["text"] = "-"
    slbl8["text"] = "-"
    slbl9["text"] = "-"
    slbl10["text"] = "-"
    
def lbdel():
    st = "delete from scores;"
    mycursor.execute(st)
    mydb.commit()