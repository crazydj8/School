import tkinter as tk

symbols = ["+", "-", "*", "/", "**"] #will be referenced later

def answer(ex): #the calculator will only answer if the expression ends with operand
    while True:
        if ex[-1] in symbols:
            ex = ex[:len(ex)-1]
        else:
            break
    ans = eval(ex)
    lbl_2["text"] = ans

def press1(num): #a new operator will replace an operator if at the end of statement
    expression = lbl_1["text"]
    
    if len(expression) != 0:
        if expression[-1] not in symbols:
            expression = expression + num
        else:
            if expression[-1] != "-":
                if expression[len(expression)-2:] == "**": #special check for ** operator
                    expression = expression[:len(expression)-2] + num
                else:
                    expression = expression[:len(expression)-1] + num
            else:
                if expression != "-": #compability with change sign function
                    if expression[-2] not in symbols:
                         expression = expression[:len(expression)-1] + num

    lbl_1["text"] = expression
    
def press2(num): #addition of digits to expression
    expression = lbl_1["text"]
    expression = expression + num
    lbl_1["text"] = expression
    answer(expression)
#change function inspired by samsung calculator    
def change(): #to change the sign of the most recent operand or the operand which will be entered next
    expression = lbl_1["text"]
    if expression == "":
        expression = "-"
    elif expression == "-":
        expression = ""    
    else:
        for i in range(-1, (-1 * len(expression)) -1, -1): #check for presence of operator
            if expression[i] in symbols:
                sym = expression[i]
                pos = len(expression) + i
                break
        if i == -1 * len(expression): #compability of negative sign with '-' operator
            if expression[0] == "-":
                expression = expression[1:]
            else:
                expression = "-" + expression
        else:
            if sym == "-":
                if expression[pos-1] in symbols:
                    expression = expression[:pos] + expression[pos+1:]
                else:
                    expression = expression[:pos+1] + "-" + expression[pos+1:]
            else:
                expression = expression[:pos+1] + "-" + expression[pos+1:]
        answer(expression)
    lbl_1["text"] = expression
    
def dec(): #function for addition of decimal point in equation
    expression = lbl_1["text"]
    if expression == "":
        expression = "0."
    else:
        if expression[-1] in symbols:
            expression = expression + "0."
        else:
            expression = expression + "."
    lbl_1["text"] = expression
    
def delete(): #backspace button
    expression = lbl_1["text"]
    if expression != "":
        expression = expression[:len(expression)-1]
    lbl_1["text"] = expression
    if expression == "":
        lbl_2["text"] = ""
    else: #as the calculator instantly answers we need to update answer immeditely
        if expression == "-":
            lbl_2["text"] = ""
        else:
            answer(expression)
    
    
def clear(): #clear button on calc
    lbl_1["text"] = ""
    lbl_2["text"] = ""

#gui

window = tk.Tk()
window.title("Calculator")
window.configure()
window.resizable(height = False, width = False)

#Widgets
frame_1 = tk.Frame(
    master = window,
    highlightbackground="#FFFFFF",
    highlightcolor="#FFFFFF", 
    highlightthickness=2, 
    bg="white")
frame_2 = tk.Frame(master = window)
lbl_1 = tk.Label(
    master = frame_1, 
    text = "", 
    bg = "#000000", 
    fg = "#FFFFFF", 
    height = 3, 
    width =33)
lbl_2 = tk.Label(
    master = frame_1, 
    text = "", 
    bg = "#000000", 
    fg = "#696969", 
    height = 3, 
    width = 33)
    
btn_his = tk.Button(
    master = frame_2, 
    text = "History", 
    bg = "#FFD700", 
    fg = "#FFFFFF", 
    height = 2, 
    width = 15)
    
btn_bck = tk.Button(
    master = frame_2, 
    text = "<-", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: delete())

btn_clr = tk.Button(
    master = frame_2, 
    text = "C", 
    bg = "#FFD700", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: clear())
btn_exp = tk.Button(
    master = frame_2, 
    text = "x^y", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press1("**"))
btn_div = tk.Button(
    master = frame_2, 
    text = "/", 
    bg = "#696969", 
    fg = "#FFD700", 
    height = 3, 
    width = 7,
    command = lambda: press1("/"))
btn_7 = tk.Button(
    master = frame_2, 
    text = "7", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("7"))
btn_8 = tk.Button(
    master = frame_2, 
    text = "8", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("8"))
btn_9 = tk.Button(
    master = frame_2, 
    text = "9", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("9"))
btn_prod = tk.Button(
    master = frame_2, 
    text = "*", 
    bg = "#696969", 
    fg = "#FFD700", 
    height = 3, 
    width = 7,
    command = lambda: press1("*"))
btn_4 = tk.Button(
    master = frame_2, 
    text = "4", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("4"))
btn_5 = tk.Button(
    master = frame_2, 
    text = "5", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("5"))
btn_6 = tk.Button(
    master = frame_2, 
    text = "6", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("6"))
btn_sub = tk.Button(
    master = frame_2, 
    text = "-", 
    bg = "#696969", 
    fg = "#FFD700", 
    height = 3, 
    width = 7,
    command = lambda: press1("-"))
btn_1 = tk.Button(
    master = frame_2, 
    text = "1", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("1"))
btn_2 = tk.Button(
    master = frame_2, 
    text = "2", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("2"))
btn_3 = tk.Button(
    master = frame_2, 
    text = "3", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("3"))
btn_add = tk.Button(
    master = frame_2, 
    text = "+", 
    bg = "#696969", 
    fg = "#FFD700", 
    height = 3, 
    width = 7,
    command = lambda: press1("+"))
btn_sign = tk.Button(
    master = frame_2, 
    text = "(+/-)", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: change())
btn_0 = tk.Button(
    master = frame_2, 
    text = "0", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: press2("0"))
btn_dec = tk.Button(
    master = frame_2, 
    text = ".", 
    bg = "#696969", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7,
    command = lambda: dec())
btn_ans = tk.Button(
    master = frame_2, 
    text = "=", 
    bg = "#FFD700", 
    fg = "#FFFFFF", 
    height = 3, 
    width = 7)

#placement
frame_1.grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
frame_2.grid(row = 2, column = 0, rowspan = 6, columnspan = 4)
lbl_1.grid(row = 0, columnspan = 4)
lbl_2.grid(row = 1, columnspan = 4)
btn_his.grid(row = 0, column = 0, columnspan = 2)
btn_bck.grid(row = 1, column = 2)
btn_clr.grid(row = 1, column=0)
btn_exp.grid(row = 1, column=1)
btn_div.grid(row = 1, column=3)
btn_7.grid(row = 2, column=0)
btn_8.grid(row = 2, column=1)
btn_9.grid(row = 2, column=2)
btn_prod.grid(row = 2, column=3)
btn_4.grid(row = 3, column=0)
btn_5.grid(row = 3, column=1)
btn_6.grid(row = 3, column=2)
btn_sub.grid(row = 3, column=3)
btn_1.grid(row = 4, column=0)
btn_2.grid(row = 4, column=1)
btn_3.grid(row = 4, column=2)
btn_add.grid(row = 4, column=3)
btn_sign.grid(row = 5, column=0)
btn_0.grid(row = 5, column=1)
btn_dec.grid(row = 5, column=2)
btn_ans.grid(row = 5, column=3)


#Made by Akshat Aryan

#chief beta tester and guidance by Subh Chaturvedi

