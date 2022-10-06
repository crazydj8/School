import tkinter as tk
import mysql.connector as sqlpj

#mysql connection
mypj = sqlpj.connect(host = "localhost", user = "root", passwd = "mysql", database = "project")
if mypj.is_connected():
    print("Connected Successfully to MySQL Database: 'Project'")
cpj = mypj.cursor()

# function
#checks validity of entered values
def valid():
    global va, vb, vc, vd, vl, vm, vn, vk, vp, vq, vr, vs
    va = v1.get()
    vb = v2.get()
    vc = v3.get()
    vd = v10.get()
    vl = v4.get()
    vm = v5.get()
    vn = v6.get()
    vk = v11.get()
    vp = v7.get()
    vq = v8.get()
    vr = v9.get()
    vs = v12.get()
    l1 = ("-", ".", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    l2 = (va, vb, vc, vd, vl, vm, vn, vk, vp, vq, vr, vs)
    for i in l2:
        if i == "":
            return (False)
            break
        elif any(x not in l1 for x in i):
            return (False)
            break
        else:
            return(True)
#brain of program: calculates and adds data to mysql table
def calc():
    if valid() == True:
        global va, vb, vc, vd, vl, vm, vn, vk, vp, vq, vr, vs
        va = float(va)
        vb = float(vb)
        vc = float(vc)
        vd = float(vd)
        vl = float(vl)
        vm = float(vm)
        vn = float(vn)
        vk = float(vk)
        vp = float(vp)
        vq = float(vq)
        vr = float(vr)
        vs = float(vs)        
        det = va*((vm*vr)-(vn*vq))+vb*((vp*vn)-(vl*vr))+vc*((vl*vq)-(vm*vp))
        dx = vd*((vm*vr)-(vn*vq))+vb*((vs*vn)-(vk*vr))+vc*((vk*vq)-(vm*vs))
        dy = va*((vk*vr)-(vn*vs))+vd*((vp*vn)-(vl*vr))+vc*((vl*vs)-(vk*vp))
        dz = va*((vm*vs)-(vk*vq))+vb*((vp*vk)-(vl*vs))+vd*((vl*vq)-(vm*vp))
        mat_det = str([[va, vb, vc, vd], [vl, vm, vn, vk], [vp, vq, vr, vs]])
        syscon = -1
        if det != 0:
            x = dx / det
            y = dy / det
            z = dz / det
            ans_1["text"] = "System is consistent"
            ans_2["text"] = "Solution : x = "+str(x)+", y = "+str(y)+", z ="+str(z)   
            mat_sol = "x="+str(x)+"\ny="+str(y)+"\nz="+str(z)
            syscon = 1
        else:
            if dx == 0 and dy == 0 and dz == 0:
                ans_1["text"] = "System is consistent"
                ans_2["text"] = "There are infinite solutions"
                mat_sol = "Infinite Solutions"
                syscon = 1
            else:
                ans_1["text"] = "System is inconsistent"
                ans_2["text"] = "There is no solution"
                mat_sol = "No Solution"
                syscon = 0
        if syscon == 1:
            con = "Consistent"
        elif syscon == 0:
            con = "inconsistent"
        st = "select max(srno) from cramer"
        no = cpj.execute(st)
        if no == None:            
            st = "INSERT INTO CRAMER(srno, matrix, consistency, solutions) VALUES('{}', '{}', '{}', '{}')".format(1, mat_det, con, mat_sol)
            cpj.execute(st)
        else:
            st = "INSERT INTO CRAMER(srno, matrix, consistency, solutions) VALUES('{}', '{}', '{}', '{}')".format(int(no + 1), mat_det, con, mat_sol)    
            cpj.execute(st)
        mypj.commit()
    else:
        error["text"] = "Error, Please enter numeric values only"
#prints the mysql table and data
def history():
    st = "select * from cramer"
    cpj.execute(st)
    data = cpj.fetchall()
    print("History(sr.no./matrix/consistency/solutions):")
    for row in data:
        print(row)
#clears everything for new entry       
def clear():
    v1.delete(0, 'end')
    v2.delete(0, 'end')
    v3.delete(0, 'end')
    v4.delete(0, 'end')
    v5.delete(0, 'end')
    v6.delete(0, 'end')
    v7.delete(0, 'end')
    v8.delete(0, 'end')
    v9.delete(0, 'end')
    v10.delete(0, 'end')
    v11.delete(0, 'end')
    v12.delete(0, 'end')    
    ans_1["text"] = ""
    ans_2["text"] = ""
    error["text"] = ""

#gui
window = tk.Tk()
window.configure(bg = "black")
window.title("Cramer's Rule Calculator")

#Widgets
#Frames
frame_0 = tk.Frame(
    master = window,
    bg="black")
frame_1 = tk.Frame(
    master = window,
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    bg="black")
frame_2 = tk.Frame(
    master = window,
    bg="black")
frame_3 = tk.Frame(
    master = window,
    bg = "black")
    
#Frame 0 label
lbl_0 = tk.Label(
    master = frame_0, 
    text = "Your Equations are:\n1)ax+by+cz=d\n2)lx+my+nz=k\n3)px+qy+rz=s\nPlease enter values of:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")

#Frame 1- main body
lbl_1 = tk.Label(
    master = frame_1, 
    text = "a:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v1 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_2 = tk.Label(
    master = frame_1, 
    text = "b:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v2 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_3 = tk.Label(
    master = frame_1, 
    text = "c:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v3 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_4 = tk.Label(
    master = frame_1, 
    text = "l:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v4 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_5 = tk.Label(
    master = frame_1, 
    text = "m:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v5 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_6 = tk.Label(
    master = frame_1, 
    text = "n:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v6 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_7 = tk.Label(
    master = frame_1, 
    text = "p:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v7 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_8 = tk.Label(
    master = frame_1, 
    text = "q:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v8 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_9 = tk.Label(
    master = frame_1, 
    text = "r:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v9 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_10 = tk.Label(
    master = frame_1, 
    text = "d:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v10 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_11 = tk.Label(
    master = frame_1, 
    text = "k:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v11 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")
lbl_12 = tk.Label(
    master = frame_1, 
    text = "s:",
    bg="black",
    fg="#00FFFF", 
    font="Arial")
v12 = tk.Entry(frame_1,
    width=3,
    bg="black", 
    fg="#00FFFF", 
    font="Arial", 
    highlightbackground="#00FFFF", 
    highlightcolor="#00FFFF", 
    highlightthickness=2, 
    insertbackground="#00FFFF")

#frame 2: Answer labels
error = tk.Label(
    master = frame_2, 
    text = "",
    bg="black",
    fg="#FF0000", 
    font=("Arial",10),
    width = 28) 
ans_1 = tk.Label(
    master = frame_2, 
    text = "",
    bg="black",
    fg="#00FFFF", 
    font=("Arial",12),
    width = 28)    
ans_2 = tk.Label(
    master = frame_2, 
    text = "",
    bg="black",
    fg="#00FFFF", 
    font=("Arial",10),
    width = 28)    

#frame 3: buttons    
btn_ans = tk.Button(
    master = frame_3, 
    text = "Calculate", 
    fg="black", 
    bg="#00FFFF", 
    font="Arial",  
    activeforeground="#00FFFF", 
    activebackground="black",
    width = 10,
    command = lambda: calc())  
btn_clr = tk.Button(
    master = frame_3, 
    text = "Clear", 
    fg="black", 
    bg="#00FFFF", 
    font="Arial",  
    activeforeground="#00FFFF", 
    activebackground="black",
    width = 10,
    command = lambda: clear())    
btn_his = tk.Button(
    master = frame_3, 
    text = "History", 
    fg="black", 
    bg="#00FFFF", 
    font="Arial",  
    activeforeground="#00FFFF", 
    activebackground="black",
    width = 10,
    command = lambda: history())        
btn_exit = tk.Button(
    master = frame_3, 
    text = "Exit", 
    fg="black", 
    bg="#00FFFF", 
    font="Arial",  
    activeforeground="#00FFFF", 
    activebackground="black",
    width = 10,
    command = lambda: exit())   
    
#grid
frame_0.grid(row = 0, column = 0, pady = (25,0), padx = (25,0), sticky = "n")
lbl_0.grid(row = 0, column = 0)

frame_1.grid(row = 1, column = 0, padx = (35), sticky = "w")
lbl_1.grid(row = 0, column = 0, pady = (10), padx = (10,0))
v1.grid(row = 0, column = 1, pady = (10), padx = (0,10))
lbl_2.grid(row=0, column =2, pady = (10))
v2.grid(row = 0, column = 3, pady = (10), padx = (0,10))
lbl_3.grid(row=0, column =4, pady = (10))
v3.grid(row = 0, column = 5, pady = (10), padx = (0,10))
lbl_10.grid(row = 0, column = 6, pady = (10))
v10.grid(row = 0, column = 7, pady = (10), padx = (0,10))
lbl_4.grid(row=1, column =0, pady = (0,10), padx = (10,0))
v4.grid(row = 1, column = 1, pady = (0,10), padx = (0,10))
lbl_5.grid(row=1, column =2, pady = (0,10))
v5.grid(row = 1, column = 3, pady = (0,10), padx = (0,10))
lbl_6.grid(row=1, column =4, pady = (0,10))
v6.grid(row = 1, column = 5, pady = (0,10), padx = (0,10))
lbl_11.grid(row=1, column =6, pady = (0,10))
v11.grid(row = 1, column = 7, pady = (0,10), padx = (0,10))
lbl_7.grid(row=2, column =0, pady = (0,10), padx = (10,0))
v7.grid(row = 2, column = 1, pady = (0,10), padx = (0,10))
lbl_8.grid(row=2, column =2, pady = (0,10))
v8.grid(row = 2, column = 3, pady = (0,10), padx = (0,10))
lbl_9.grid(row=2, column =4, pady = (0,10))
v9.grid(row = 2, column = 5, pady = (0,10), padx = (0,10))
lbl_12.grid(row=2, column =6, pady = (0,10))
v12.grid(row = 2, column = 7, pady = (0,10), padx = (0,10))

frame_2.grid(row = 2, column = 0, pady = (0,25), padx = (35), sticky = "w")
error.grid(row = 0)
ans_1.grid(row = 1)
ans_2.grid(row = 2)

frame_3.grid(row = 1, rowspan = 2, column = 1, sticky = "e")
btn_ans.grid(row = 0, pady = (0,25), padx = (0,35))
btn_clr.grid(row = 1, pady = (0,25), padx = (0,35))
btn_his.grid(row = 2, pady = (0,25), padx = (0,35))
btn_exit.grid(row = 3, pady = (0,25), padx = (0,35))



