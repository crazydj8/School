#File directory
import os 
cwd = list(os.path.abspath(__file__))

for i in range(18):
    cwd.pop()

file = ""

for i in cwd:
    file += i
file = file + "Score.txt"

condition = 0

def takescore():
    f = open(file, "r")
    global lscore
    s = []
    while True:
        x = f.readline()
        if x == "":
            break
        else:
            l = x.rstrip("\n").split(",")
            s.append(l)
    lscore = sorted(s, key = lambda x: x[1], reverse = True)
    f.close()
    
def checklen(list):
    global condition, x
    x = len(list)
    if x == 0:
        condition = 1
    elif x < 10:
        condition = 2
    elif x >= 10:
        condition = 3
        
def main(lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10, slbl1, slbl2, slbl3, slbl4, slbl5, slbl6, slbl7, slbl8, slbl9, slbl10):
    global condition, lscore, x
    name = [lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10]
    score = [slbl1, slbl2, slbl3, slbl4, slbl5, slbl6, slbl7, slbl8, slbl9, slbl10]
    takescore()
    checklen(lscore)
    if condition == 2:
        for i in range(x):
            name[i]["text"] = lscore[i][0] 
            score[i]["text"] = lscore[i][1]
    elif condition == 3:
        for i in range(10):
            name[i]["text"] = lscore[i][0] 
            score[i]["text"] = lscore[i][1]
            
def lbreset(lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10, slbl1, slbl2, slbl3, slbl4, slbl5, slbl6, slbl7, slbl8, slbl9, slbl10):
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