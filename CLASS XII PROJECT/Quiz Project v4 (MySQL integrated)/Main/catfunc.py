import mysql.connector as mycon

mydb = mycon.connect(host = "localhost", user = "root", password = "mysql", database = "qna")
mycursor = mydb.cursor()

def combobox(combo_box, combostyle, cstyle1):
    mycursor.execute("show tables;")
    l = mycursor.fetchall()
    combostyle.theme_use(cstyle1)
    if len(l) != 0:
        combo_box["values"] = l
        combo_box.current(0)
    else:
        combo_box["values"] = () 
        combo_box.set("")    