#File directory
import os 
cwd = list(os.path.abspath(__file__))

for i in range(16):
    cwd.pop()
file1 = ""
file2 = ""
file3 = ""
for i in cwd:
    file1 += i
    file2 += i
    file3 += i
file1 = file1 + "Questions.txt"
file2 = file2 + "Answers.txt"
file3 = file3 + "Score.txt"
userans = []
score = 0

def error(ent, lbl):
    x = ent.get()
    if x == "" :
        lbl["text"] = "Field cannot be blank"
        return False
    else:
        return True

def play(ent, frame, lbl, q1, q2, q3, q4, q5):
    if error(ent, lbl) == True:
        frame.tkraise()
        q = open(file1, "r")
        a = open(file2, "r")
        global l1, l2
        l1 = []
        while True:
            x = q.readline()
            if x == "":
                break
            else:
                l = x.rstrip("\n")
                l1.append(l)
        l2 = []
        while True:
            x = a.readline()
            if x == "":
                break
            else:
                l = x.rstrip("\n")
                l2.append(l)
        q.close()
        a.close()
        q1["text"] = "Q1. " + l1[0]
        q2["text"] = "Q2. " + l1[1]
        q3["text"] = "Q3. " + l1[2]
        q4["text"] = "Q4. " + l1[3]
        q5["text"] = "Q5. " + l1[4]
        
def savename(ent, lbl):
    global nm
    if ent.get() != "":
        nm = ent.get()

def reset(ent, lbl):
    if error(ent, lbl) == True:
        ent.delete(0, "end")
        lbl["text"] = ""
    
def back(ent, lbl):
    ent.delete(0, "end")
    lbl["text"] = ""

def answer(lbl, entry, lbl1, frame):
    if error(entry, lbl1) == True:
        global l2, score
        x = lbl.cget("text")
        n = int(x[-1])
        if entry.get().lower() == l2[n-1].lower():
            score += 1
        frame.tkraise()

def scores(entry, lbl1):
    if error(entry, lbl1) == True:
        s = open(file3, "a")
        global nm, score
        s1 = nm + "," + str(score) +"\n"
        s.write(s1)
        s.close()
    
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
    lbl1["text"] = userans[0]
    if userans[0].lower() != l2[0].lower():
        lbl1.config(fg = "red")
    lbl2["text"] = userans[1]
    if userans[1].lower() != l2[1].lower():
        lbl2.config(fg = "red")
    lbl3["text"] = userans[2]
    if userans[2].lower() != l2[2].lower():
        lbl3.config(fg = "red")
    lbl4["text"] = userans[3]
    if userans[3].lower() != l2[3].lower():
        lbl4.config(fg = "red")
    lbl5["text"] = userans[4]
    if userans[4].lower() != l2[4].lower():
        lbl5.config(fg = "red")
    clbl1["text"] = l2[0]
    clbl2["text"] = l2[1]
    clbl3["text"] = l2[2]
    clbl4["text"] = l2[3]
    clbl5["text"] = l2[4]
    
def analyseques(lbl1, lbl2, lbl3, lbl4, lbl5):
    global l1
    lbl1["text"] = "Q1. " + l1[0]
    lbl2["text"] = "Q2. " + l1[1]
    lbl3["text"] = "Q3. " + l1[2]
    lbl4["text"] = "Q4. " + l1[3]
    lbl5["text"] = "Q5. " + l1[4]
    
def scorereset():
    global score, userans
    score = 0
    userans = []