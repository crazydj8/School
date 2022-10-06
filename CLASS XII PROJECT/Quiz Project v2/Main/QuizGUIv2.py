#Quiz Project

import tkinter as tk
import webbrowser
import loginfunc, signupfunc, deletefunc, editfunc, quizfunc, finishfunc, analysisfunc, leaderfunc
from tkinter import font as tkfont
from tkinter import ttk

#Main Window
window = tk.Tk()
window.title("Quiz")
window.geometry("800x600")
window.configure()
window.resizable(height = False, width = False)

# Font Style for headings, normal text, and text in buttons
heading = tkfont.Font(family = "Arial", size = 40)
text = tkfont.Font(family = "Arial", size = 20)
btntext = tkfont.Font(family = "Arial", size = 14)
analysistext = tkfont.Font(family = "Arial", size = 15)
hyperlink = tkfont.Font(family = "Arial", size = 20, underline = 1)

#God Frame contains all other frames
god = tk.Frame(
    master = window, 
    bg = "black")
god.pack(side = "top", 
    fill = "both", 
    expand = True)
# ALL FRAMES : intro, login, edit, player, quiz, signup, successful, question 1-5

#FRAMES
# # # # # # # # # # # # # # # # Intro Frame # # # # # # # # # # # # # # # # # # # #
intro = tk.Frame(master = god,
    bg = "black")
intro.grid(row = 0, column = 0, sticky = "nsew")

#Intro Title
title = tk.Label(master = intro, 
    bg = "black",
    fg = "lime",
    text = "Welcome to the quiz!",
    width = 26,
    font = heading)
title.grid(row = 0, column = 0, pady = (75, 50), sticky = "w")

#Admin button
btn_login = tk.Button(master = intro,
    bg = "lime",
    fg = "black",
    width = 20,
    activeforeground = "lime",
    activebackground = "black",
    text = "Edit Questions(Admin)",
    font = btntext,
    command = lambda: loginfunc.adminbtn(login, userent))
btn_login.grid(row = 2, column = 0, pady = (20))

#Not admin button
btn_player = tk.Button(master = intro,
    bg = "lime",
    fg = "black",
    width = 20,
    activeforeground = "lime",
    activebackground = "black",
    text = "Start",
    font = btntext,
    command = lambda: loginfunc.start(player))
btn_player.grid(row = 1, column = 0, pady = (20))

#Credit button 
btn_credit = tk.Button(master = intro,
    bg = "lime",
    fg = "black",
    width = 20,
    activeforeground = "lime",
    activebackground = "black",
    text = "Credits",
    font = btntext,
    command = lambda: credit.tkraise())
btn_credit.grid(row = 3, column = 0, pady = (20))

#Exit button
exit_btn = tk.Button(master = intro,
    bg = "lime",
    fg = "black",
    width = 20,
    activeforeground = "lime",
    activebackground = "black",
    text = "Exit",
    font = btntext,
    command = lambda: exit())
exit_btn.grid(row = 4, column = 0, pady = (20, 50))

#Name label
nmlbl = tk.Label(master = intro,
    bg = "black",
    fg = "lime",
    text = "v2.0",
    font = btntext)
nmlbl.grid(row = 5, column = 0, padx = (0, 25), sticky = "e") 

# # # # # # # # # # # # # # # # Credit Frame # # # # # # # # # # # # # # # # # # # #
credit = tk.Frame(master = god,
    bg = "black")
credit.grid(row = 0, column = 0, sticky = "nsew")

credit_title = tk.Label(master = credit,
    bg = "black",
    fg = "lime",
    text = "Credits",
    width = 26,
    font = heading)
credit_title.grid(row = 0, column = 0, columnspan = 2, pady= (50, 35), sticky = "w")

creatorlbl = tk.Label(master = credit,
    bg = "black",
    fg = "lime",
    text = "Creators:",
    font = text)
creatorlbl.grid(row = 1, column = 0, padx = (0, 10), sticky = "ne")

creator = tk.Label(master = credit,
    bg = "black",
    fg = "lime",
    text = "Nilesh\nAkshat",
    font = text)
creator.grid(row = 1, column = 1, rowspan = 2, padx = (10, 0), pady = (0,25), sticky = "w")

betalbl = tk.Label(master = credit,
    bg = "black",
    fg = "lime",
    text = "Beta testers:",
    font = text)
betalbl.grid(row = 3, column = 0, padx = (0, 10), sticky = "ne")

beta = tk.Label(master = credit,
    bg = "black",
    fg = "lime",
    text = "Merril\nAkshat",
    font = text)
beta.grid(row = 3, column = 1, rowspan = 2, padx = (10, 0), pady = (0, 25), sticky = "w")

siteslbl = tk.Label(master = credit,
    bg = "black",
    fg = "lime",
    text = "Sources:",
    font = text)
siteslbl.grid(row = 5, column = 0, padx = (0, 10), sticky = "ne")

site1 = tk.Label(master = credit,
    bg = "black",
    fg = "cyan",
    text = "https://stackoverflow.com/",
    cursor = "hand2",
    font = hyperlink)
site1.grid(row = 5, column = 1, padx = (10, 0), sticky = "w")
site1.bind('<Button-1>', lambda e: [webbrowser.open_new("https://stackoverflow.com/")])

site2 = tk.Label(master = credit,
    bg = "black",
    fg = "cyan",
    text = "https://www.tutorialspoint.com",
    cursor = "hand2",
    font = hyperlink)
site2.grid(row = 6, column = 1, padx = (10, 0), sticky = "w")
site2.bind('<Button-1>', lambda e: [webbrowser.open_new("https://www.tutorialspoint.com")])

site3 = tk.Label(master = credit,
    bg = "black",
    fg = "cyan",
    text = "https://www.geeksforgeeks.org",
    cursor = "hand2",
    font = hyperlink)
site3.grid(row = 7, column = 1, padx = (10, 0), sticky = "w")
site3.bind('<Button-1>', lambda e: [webbrowser.open_new("https://www.geeksforgeeks.org")])

site4 = tk.Label(master = credit,
    bg = "black",
    fg = "cyan",
    text = "https://www.rapidtables.com/",
    cursor = "hand2",
    font = hyperlink)
site4.grid(row = 8, column = 1, padx = (10, 0), sticky = "w")
site4.bind('<Button-1>', lambda e: [webbrowser.open_new("https://www.rapidtables.com/web/color/RGB_Color.html")])

#Back button to go previous page
back_btn = tk.Button(master = credit,
    bg = "lime",
    fg = "black",
    width = 10,
    activeforeground = "lime",
    activebackground = "black",
    text = "Go Back",
    font = btntext,
    command = lambda: intro.tkraise())
back_btn.grid(row = 9, column = 1, padx = (50, 0), pady = (25, 0), sticky = "w")

# # # # # # # # # # # # # # # # Login Frame # # # # # # # # # # # # # # # # # # # #

login = tk.Frame(master = god,
    bg = "black")
login.grid(row = 0, column = 0, sticky = "nsew")

#Login Title
logintitle = tk.Label(master = login,
    bg = "black",
    fg = "lime",
    text = "Login as an Admin",
    width = 26,
    font = heading)
logintitle.grid(row = 0, column = 0, columnspan = 2, pady = (75, 50), sticky = "w")

#Username Label
userlbl = tk.Label(master = login,
    bg = "black",
    fg = "lime",
    text = "Enter Username:",
    font = text)
userlbl.grid(row = 1, column = 0, padx = (0, 10), pady = (25, 10), sticky = "e")

#Entry to enter username
userent = tk.Entry(master = login,
    width = 15,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
userent.grid(row = 1, column = 1, padx = (10, 0), pady = (25, 10), sticky = "w")

#Password Label
passlbl = tk.Label(master = login,
    bg = "black",
    fg = "lime",
    text = "Enter Password:",
    font = text)
passlbl.grid(row = 2, column = 0, padx = (0, 10), pady = (10, 25), sticky = "e")

#Entry to enter the password
passent = tk.Entry(master = login,
    show = "*",
    width = 15,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
passent.grid(row = 2, column = 1, padx = (10, 0), pady = (10, 25), sticky = "w")

#Error label when error is occurred
loginerror = tk.Label(master = login,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
loginerror.grid(row = 3, column = 0, columnspan = 2, pady = (0, 25))

#Login button
login_btn = tk.Button(master = login,
    bg = "lime",
    fg = "black",
    width = 10,
    activeforeground = "lime",
    activebackground = "black",
    text = "Login",
    font = btntext,
    command = lambda: [loginfunc.login(userent, passent, loginerror, edit, remove, user_box, combostyle, cstyle1), R1.select(), editfunc.showques(queslbl, anslbl, choice), nques_ent.focus_set(), loginfunc.reset(userent, passent, loginerror)])
login_btn.grid(row = 4, column = 1, padx = (70, 0), pady = (25, 500), sticky = "w")

#Back button to go previous page
back_btn = tk.Button(master = login,
    bg = "lime",
    fg = "black",
    width = 10,
    activeforeground = "lime",
    activebackground = "black",
    text = "Go Back",
    font = btntext,
    command = lambda: [loginfunc.goback(userent, passent, loginerror, intro, manage)])
back_btn.grid(row = 4, column = 0, padx = (0, 50), pady = (25, 500), sticky = "e")

# # # # # # # # # # # # # # # # Edit Frame # # # # # # # # # # # # # # # # # # # #
edit = tk.Frame(master = god,
    bg="black")
edit.grid(row = 0, column = 0, sticky = "nsew")

#Edit title 
edit_title = tk.Label(master = edit,
    bg = "black",
    fg = "lime",
    text = "Edit question",
    width = 26,
    font = heading)
edit_title.grid(row = 0, column = 0, columnspan = 5, pady = (25), sticky = "w") 

#Radiobuttons (5)   

choice = tk.IntVar()

#R1
R1 = tk.Radiobutton(master = edit,
    text = "Q1",
    bg = "lime",
    fg = "black",
    activebackground = "black",
    activeforeground = "lime",
    selectcolor = "#00FFFF",
    indicator = 0,
    width = 7,
    variable = choice,
    value = 1,
    font = btntext,
    command = lambda: [editfunc.showques(queslbl, anslbl, choice), editfunc.errorreset(qerror)])
R1.grid(row = 1, column = 0)

#R2
R2 = tk.Radiobutton(master = edit,
    text = "Q2",
    bg = "lime",
    fg = "black",
    activebackground = "black",
    activeforeground = "lime",
    selectcolor = "#00FFFF",
    indicator = 0,
    width = 7,
    variable = choice,
    value = 2,
    font = btntext,
    command = lambda: [editfunc.showques(queslbl, anslbl, choice), editfunc.errorreset(qerror)])
R2.grid(row = 1, column = 1) 

#R3
R3 = tk.Radiobutton(master = edit,
    text = "Q3",
    bg = "lime",
    fg = "black",
    activebackground = "black",
    activeforeground = "lime",
    selectcolor = "#00FFFF",
    indicator = 0,
    width = 7,
    variable = choice,
    value = 3,
    font = btntext,
    command = lambda: [editfunc.showques(queslbl, anslbl, choice), editfunc.errorreset(qerror)])
R3.grid(row = 1, column = 2)

#R4
R4 = tk.Radiobutton(master = edit,
    text = "Q4",
    bg = "lime",
    fg = "black",
    activebackground = "black",
    activeforeground = "lime",
    selectcolor = "#00FFFF",
    indicator = 0,
    variable = choice,
    width = 7,
    value = 4,
    font = btntext,
    command = lambda: [editfunc.showques(queslbl, anslbl, choice), editfunc.errorreset(qerror)])
R4.grid(row = 1, column = 3)

#R5
R5 = tk.Radiobutton(master = edit,
    text = "Q5",
    bg = "lime",
    fg = "black",
    activebackground = "black",
    activeforeground = "lime",
    selectcolor = "#00FFFF",
    indicator = 0,
    variable = choice,
    width = 7,
    value = 5,
    font = btntext,
    command = lambda: [editfunc.showques(queslbl, anslbl, choice), editfunc.errorreset(qerror)])    
R5.grid(row = 1, column = 4)

#Question Label according to Radiobutton
queslbl = tk.Label(master = edit,
    bg = "black",
    fg = "lime",
    text = "Question",
    font = text)
queslbl.grid(row = 2, column = 0, columnspan = 5, pady = (20, 5))

#Answer Label according to Question
anslbl = tk.Label(master = edit,
    bg = "black",
    fg = "lime",
    text = "Answer",
    font = text)
anslbl.grid(row = 3, column = 0, columnspan = 5, pady = (5, 10))

#New Question label
nqueslbl = tk.Label(master = edit,
    bg = "black",
    fg = "lime",
    text = "New Question:",
    font = text)
nqueslbl.grid(row = 4, column = 0, columnspan = 2, padx = (0, 10), pady = (10, 5), sticky = "e")

#New Question to be entered
nques_ent = tk.Entry(master = edit,
    bg = "black",
    fg = "lime",
    width = 25,
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
nques_ent.grid(row = 4, column = 2, columnspan = 3, padx = (10, 0), pady = (10, 5), sticky = "w")

#New answer label
nanslbl = tk.Label(master = edit,
    bg = "black",
    fg = "lime",
    text = "New Answer:",
    font = text)
nanslbl.grid(row = 5, column = 0, columnspan = 2, padx = (0, 10), pady = (5, 25), sticky = "e")

#New answer entry
nans_ent = tk.Entry(master = edit,
    bg = "black",
    fg = "lime",
    width = 25,
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
nans_ent.grid(row = 5, column = 2, columnspan = 3, padx = (10, 0), pady = (5, 25), sticky = "w")

#Error to be displayed when something is filled wrong 
qerror = tk.Label(master = edit,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
qerror.grid(row = 6, column = 0, columnspan = 5, pady = (0, 10))

#Edit button to edit question to the file
edit_btn = tk.Button(master = edit,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Edit",
    font = btntext,
    command = lambda: [editfunc.changeques(choice, nques_ent, nans_ent, qerror), editfunc.showques(queslbl, anslbl, choice), editfunc.reset(nques_ent, nans_ent)])
edit_btn.grid(row = 7, column = 3, columnspan = 2, pady = (25, 300), sticky = "w")

#Home button to go back home
home_btn=tk.Button(master = edit,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Home",
    font = btntext,
    command = lambda: [editfunc.back(nques_ent, nans_ent, qerror), intro.tkraise()])
home_btn.grid(row = 7, column = 0, columnspan = 2, pady = (25, 300), sticky = "e")


# # # # # # # # # # # # # # # # Player Frame # # # # # # # # # # # # # # # # # # # #

player = tk.Frame(master = god,
    bg = "black")
player.grid(row = 0, column = 0, sticky = "nsew")

#Not an admin Label
player_lbl = tk.Label(master = player,
    bg = "black",
    fg = "lime",    
    text = "You're not an Admin",
    width = 26,
    font = heading)
player_lbl.grid(row = 0, column = 0, pady = (75), sticky = "w")

#Manage admin button
manageadmin_btn = tk.Button(master = player,
    bg = "lime",
    fg = "black",
    width = 21,
    activeforeground = "lime",
    activebackground = "black",
    text = "Manage Admin",
    font = btntext,
    command = lambda: manage.tkraise())
manageadmin_btn.grid(row = 3, column = 0, pady = (0, 50))

#Play quiz button
play_btn = tk.Button(master = player,
    bg = "lime",
    fg = "black",
    width = 21,
    activeforeground = "lime",
    activebackground = "black",
    text = "Play Quiz!",
    font = btntext,
    command = lambda: [quiz.tkraise(), playername_ent.focus_set()])
play_btn.grid(row = 1, column = 0, pady = (0, 50))

#Leaderboard button
lb_btn = tk.Button(master = player,
    bg = "lime",
    fg = "black",
    width = 21,
    activeforeground = "lime",
    activebackground = "black",
    text = "View Highscore",
    font = btntext,
    command = lambda: [leaderfunc.main(name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10), leaderboard.tkraise()])
lb_btn.grid(row = 2, column = 0, pady = (0, 50))

#Back button
back_btn1 = tk.Button(master = player,
    bg = "lime",
    fg = "black",
    width = 21,
    activeforeground = "lime",
    activebackground = "black",
    text = "Go Back",
    font = btntext,
    command = lambda: intro.tkraise())
back_btn1.grid(row = 4, column = 0, pady = (0, 600))


# # # # # # # # # # # # # # # # Quiz Frame # # # # # # # # # # # # # # # # # # # #
quiz = tk.Frame(master = god,
    bg = "black")
quiz.grid(row = 0, column = 0, sticky = "nsew")

#Quiz Title
quiz_title = tk.Label(master = quiz,
     bg = "black",
    fg = "lime",
    text = "Start quiz",
    width = 26,
    font = heading)
quiz_title.grid(row = 0, column = 0, columnspan = 2, pady = (75, 100), sticky = "w")

#Playername Label
playername_lbl = tk.Label(master = quiz,
    bg = "black",
    fg = "lime",
    text = "Enter your name:",
    font = text)
playername_lbl.grid(row = 1, column = 0, padx = (0, 10), pady = (25), sticky = "e")

#Playername entry
playername_ent = tk.Entry(master = quiz,
    bg = "black",
    fg = "lime",
    width = 13,
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
playername_ent.grid(row = 1, column = 1, padx = (10, 0), pady = (25), sticky = "w")


#Error message when playername is blank
playerror = tk.Label(master = quiz,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
playerror.grid(row = 2, column = 0, columnspan = 2, pady = (0, 50))

#Start Quiz Button
start_btn = tk.Button(master = quiz,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "► Start Quiz",
    font = btntext,
    command = lambda: [quizfunc.savename(playername_ent, playerror), quizfunc.play(playername_ent, q1, playerror, q1_lbl, q2_lbl, q3_lbl, q4_lbl, q5_lbl),
    quizfunc.reset(playername_ent, playerror), a1_ent.focus_set()])
start_btn.grid(row = 3, column = 1, padx = (60, 0), pady = (25, 550), sticky = "w")

#Back button
back_btn1 = tk.Button(master = quiz,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Go Back",
    font = btntext,
    command = lambda: [quizfunc.back(playername_ent, playerror), player.tkraise()])
back_btn1.grid(row = 3, column = 0, padx = (0, 50), pady = (25, 550), sticky = "e")


# # # # # # # # # # # # # # # # Manage Admin Frame # # # # # # # # # # # # # # # # # # # #
manage = tk.Frame(master = god,
    bg = "black")
manage.grid(row = 0, column = 0, sticky = "nsew")

#Title - Manage Admin
manage_title = tk.Label(master = manage,
    bg = "black",
    fg = "lime",
    text = "Manage Admin",
    width = 26,
    font = heading)
manage_title.grid(row = 0, column = 0, pady = (75, 100), sticky = "w")

#Signup for admin button
signup_btn = tk.Button(master = manage,
    bg = "lime",
    fg = "black",
    width = 21,
    activeforeground = "lime",
    activebackground = "black",
    text = "Sign up for Admin",
    font = btntext,
    command = lambda: [signup.tkraise(), user_ent.focus_set()])
signup_btn.grid(row = 1, column = 0, pady = (0, 50))

#Remove admin button
removeadmin_btn = tk.Button(master = manage,
    bg = "lime",
    fg = "black",
    width = 21,
    activeforeground = "lime",
    activebackground = "black",
    text = "Delete Admin",
    font = btntext,
    command = lambda: [login.tkraise(), userent.focus_set()])
removeadmin_btn.grid(row = 2, column = 0, pady = (0, 50))

#Back button
back_btn = tk.Button(master = manage,
    bg = "lime",
    fg = "black",
    width = 21,
    activeforeground = "lime",
    activebackground = "black",
    text = "Back",
    font = btntext,
    command = lambda: player.tkraise())
back_btn.grid(row = 3, column = 0, pady = (0, 50))


# # # # # # # # # # # # # # # # Signup Frame # # # # # # # # # # # # # # # # # # # #
signup = tk.Frame(master = god,
    bg = "black")
signup.grid(row = 0, column = 0, sticky = "nsew")

#Title - Sign as admin
signup_title = tk.Label(master = signup,
    bg = "black",
    fg = "lime",
    text = "Sign up as Admin",
    width = 26,
    font = heading)
signup_title.grid(row = 0, column = 0, columnspan = 2, pady = (75, 50), sticky = "w")

#Username label
user_lbl = tk.Label(master = signup,
    bg = "black",
    fg = "lime",
    text = "Create username:",
    font = text)
user_lbl.grid(row = 1, column = 0, padx = (0, 10), pady = (25, 10), sticky = "e")

#Username to be created
user_ent = tk.Entry(master = signup,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    width = 13,
    font = text)
user_ent.grid(row = 1, column = 1, padx = (10, 0), pady = (25, 10), sticky = "w")

#Password label
password_lbl = tk.Label(master = signup,
    bg = "black",
    fg = "lime",
    text = "Create password:",
    font = text)
password_lbl.grid(row = 2, column = 0, padx = (0, 10), pady = (10), sticky = "e")

#Password for the username which is created
password_ent = tk.Entry(master = signup,
    bg = "black",
    fg = "lime",
    width = 13,
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    show = "*",
    font = text)
password_ent.grid(row = 2, column = 1, padx = (10, 0), pady = (10), sticky = "w")

#Confirm Password Label
cpasslbl = tk.Label(master = signup,
    bg = "black",
    fg = "lime",
    text = "Confirm Password:",
    font = text)
cpasslbl.grid(row = 3, column = 0, padx = (0, 10), pady = (10, 25), sticky = "e")

#Entry to enter the confirm password
cpassent = tk.Entry(master = signup,
    show = "*",
    width = 13,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
cpassent.grid(row = 3, column = 1, padx = (10, 0), pady = (10, 25), sticky = "w")

#Error which occurs if any
signuperror = tk.Label(master = signup,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
signuperror.grid(row = 4, column = 0, columnspan = 2, pady = (0, 25))

#Sign up button to register the user as admin
signupnow_btn = tk.Button(master = signup,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Sign Up Now",
    font = btntext,
    command = lambda: [signupfunc.register(user_ent, password_ent, cpassent, signuperror, successful)])
signupnow_btn.grid(row = 5, column = 1, padx = (45, 0), pady = (25, 400), sticky = "w")

#Back button to go back
back_btn2 = tk.Button(master = signup,
    bg ="lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Go Back",
    font = btntext,
    command = lambda: [signupfunc.back(user_ent, password_ent, cpassent, signuperror), manage.tkraise()])
back_btn2.grid(row = 5, column = 0, padx = (0, 55), pady = (25, 400), sticky = "e")


# # # # # # # # # # # # # # # # Remove Admin Frame # # # # # # # # # # # # # # # # # # # #
remove = tk.Frame(master = god,
    bg = "black")
remove.grid(row = 0, column = 0, sticky = "nsew")

#Title - Delete Admin
removetitle = tk.Label(master = remove,
    bg = "black",
    fg = "lime",
    text = "Delete Admin",
    width = 26,
    font = heading)
removetitle.grid(row = 0, column = 0, columnspan = 2, pady = (75, 100), sticky = "w")

#Username to be removed label
removeuser = tk.Label(master = remove,
    bg = "black",
    fg = "lime",
    text = "Enter the username to be removed:",
    font = text)
removeuser.grid(row = 1, column = 0, padx = (0, 10), sticky = "e")
#ComboBox representing the usernames 

combostyle = ttk.Style()

combostyle.theme_create("combostyle1", parent = "alt",
                         settings = {"TCombobox" :
                                     {"configure" :
                                      {"selectforeground" : "red",
                                       "selectbackground" : "lime",
                                       "fieldbackground" : "lime",
                                       "background" : "lime"
                                       }}}
                        )

cstyle1 = "combostyle1"

s = tk.StringVar()

user_box = ttk.Combobox(master = remove,
    width = 18,
    textvariable = s,
    font = text)   
user_box.grid(row = 1, column = 1, padx = (10, 0), ipady = (1), sticky = "w")
user_box["state"] = "readonly"

#Deleted successfully label
removed = tk.Label(master = remove,
    bg = "black",
    fg = "lime",
    text = "",
    font = text)
removed.grid(row = 2, column = 0, columnspan = 2, pady = (0, 20))

#Remove button
removebtn = tk.Button(master = remove,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Delete",
    font = btntext,
    command = lambda: [deletefunc.delete(s, removed), loginfunc.combobox(user_box, combostyle, cstyle1)])
removebtn.grid(row = 3, column = 1, pady = (100, 0), sticky = "w")

#Home button
homebtn = tk.Button(master = remove,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Home",
    font = btntext,
    command = lambda: [deletefunc.home(removed), intro.tkraise()])
homebtn.grid(row = 3, column = 0, padx = (0, 200), pady = (100, 0), sticky = "e")


# # # # # # # # # # # # # # # # Successful Frame # # # # # # # # # # # # # # # # # # # #
successful = tk.Frame(master = god,
    bg = "black")
successful.grid(row = 0, column = 0, sticky = "nsew")

#Title - Sign up is successful 
successful_title = tk.Label(master = successful,
    bg = "black",
    fg = "lime",
    text = "Sign up successful!",
    width = 26,
    font = heading)
successful_title.grid(row = 0, column = 0, pady = (150, 50), sticky = "w")

#Home button to go to home
home_btn=tk.Button(master = successful,
    bg ="lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "⌂ Home",
    font = btntext,
    command = lambda: [signupfunc.back(user_ent, password_ent, cpassent, signuperror), intro.tkraise()])
home_btn.grid(row = 1, column = 0, pady = (75, 300))


# # # # # # # # # # # # # # # # Question 1 Frame # # # # # # # # # # # # # # # # # # # #
q1 = tk.Frame(master = god,
    bg = "black")
q1.grid(row = 0, column = 0, sticky = "nsew")

#Title - Quiz
q1_title = tk.Label(master = q1,
    bg = "black",
    fg = "lime",
    text = "Question 1",
    font = heading)
q1_title.grid(row = 0, column = 0, columnspan = 2, pady = (50))

#Question 1 Label
q1_lbl = tk.Label(master = q1,
    bg = "black",
    fg = "lime",
    text = "Question 1",
    width = 50,
    font = text)
q1_lbl.grid(row = 1, column = 0, columnspan = 2, pady = (25), sticky = "w")

#Answer 1 label
a1_lbl = tk.Label(master = q1,
    bg = "black",
    fg = "lime",
    text = "Answer :",
    font = text)
a1_lbl.grid(row = 2, column = 0, padx = (0, 10), pady = (25), sticky ="e")

#Answer 1 to be entered
a1_ent = tk.Entry(master = q1,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
a1_ent.grid(row = 2, column = 1, padx = (10, 0), pady = (25), sticky = "w")
 

#Error to be occured if any
q1error = tk.Label(master = q1,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
q1error.grid(row = 3, column = 0, columnspan = 2, pady = (0, 35))

#Next button to go to next question
nextbtn = tk.Button(master = q1,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Next",
    font = btntext,
    command = lambda: [quizfunc.answer(q1_title, a1_ent, q1error, q2),
quizfunc.take(a1_ent, q1error), quizfunc.reset(a1_ent, q1error), a2_ent.focus_set()])
nextbtn.grid(row = 4, column = 1, pady = (25, 400))


# # # # # # # # # # # # # # # # Question 2 Frame # # # # # # # # # # # # # # # # # # # #

q2 = tk.Frame(master = god,
    bg = "black")
q2.grid(row = 0, column = 0, sticky = "nsew")

#Title - Quiz
q2_title = tk.Label(master = q2,
    bg = "black",
    fg = "lime",
    text = "Question 2",
    font = heading)
q2_title.grid(row = 0, column = 0, columnspan = 2, pady = (50))

#Question 2 Label
q2_lbl = tk.Label(master = q2,
    bg = "black",
    fg = "lime",
    text = "Question 2:",
    width = 50,
    font = text)
q2_lbl.grid(row = 1, column = 0, columnspan = 2, pady = (25), sticky = "w")

#Answer 2 label
a2_lbl = tk.Label(master = q2,
    bg = "black",
    fg = "lime",
    text = "Answer :",
    font = text)
a2_lbl.grid(row = 2, column = 0, padx = (0, 10), pady = (25), sticky = "e")

#Answer 2 to be entered
a2_ent = tk.Entry(master = q2,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
a2_ent.grid(row = 2, column = 1, padx = (10, 0), pady = (25), sticky = "w")


#Error to be occured if any
q2error = tk.Label(master = q2,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
q2error.grid(row = 3, column = 0, columnspan = 2, pady = (0, 35))

#Next button to go to next question
nextbtn = tk.Button(master = q2,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Next",
    font = btntext,
    command = lambda: [quizfunc.answer(q2_title, a2_ent, q2error, q3), quizfunc.take(a2_ent, q2error), quizfunc.reset(a2_ent, q2error), a3_ent.focus_set()])
nextbtn.grid(row = 4, column = 1, pady = (25, 400))


# # # # # # # # # # # # # # # # Question 3 Frame # # # # # # # # # # # # # # # # # # # #

q3 = tk.Frame(master = god,
    bg = "black")
q3.grid(row = 0, column = 0, sticky = "nsew")

#Title - Quiz
q3_title = tk.Label(master = q3,
    bg = "black",
    fg = "lime",
    text = "Question 3",
    font = heading)
q3_title.grid(row = 0, column = 0, columnspan = 2, pady = (50))

#Question 3 Label
q3_lbl = tk.Label(master = q3,
    bg = "black",
    fg = "lime",
    text = "Question 3:",
    width = 50,
    font = text)
q3_lbl.grid(row = 1, column = 0, columnspan = 2, pady = (25), sticky = "w")

#Answer 3 label
a3_lbl = tk.Label(master = q3,
    bg = "black",
    fg = "lime",
    text = "Answer :",
    font = text)
a3_lbl.grid(row = 2, column = 0, padx = (0, 10), pady = (25), sticky = "e")

#Answer 3 to be entered
a3_ent = tk.Entry(master = q3,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
a3_ent.grid(row = 2, column = 1, padx = (10, 0), pady = (25), sticky = "w")


#Error to be occured if any
q3error = tk.Label(master = q3,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
q3error.grid(row = 3, column = 0, columnspan = 2, pady = (0, 35))

#Next button to go to next question
nextbtn = tk.Button(master = q3,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Next",
    font = btntext,
    command = lambda: [quizfunc.answer(q3_title, a3_ent, q3error, q4), quizfunc.take(a3_ent, q3error), quizfunc.reset(a3_ent, q3error), a4_ent.focus_set()])
nextbtn.grid(row = 4, column = 1, pady = (25,   400))


# # # # # # # # # # # # # # # # Question 4 Frame # # # # # # # # # # # # # # # # # # # #

q4 = tk.Frame(master = god,
    bg = "black")
q4.grid(row = 0, column = 0, sticky = "nsew")

#Title - Quiz
q4_title = tk.Label(master = q4,
    bg = "black",
    fg = "lime",
    text = "Question 4",
    font = heading)
q4_title.grid(row = 0, column = 0, columnspan = 2, pady = (50))

#Question 4 Label
q4_lbl = tk.Label(master = q4,
    bg = "black",
    fg = "lime",
    text = "Question 4:",
    width = 50,
    font = text)
q4_lbl.grid(row = 1, column = 0, columnspan = 2, pady = (25))

#Answer 4 label
a4_lbl = tk.Label(master = q4,
    bg = "black",
    fg = "lime",
    text = "Answer :",
    font = text)
a4_lbl.grid(row = 2, column = 0, padx = (10, 0), pady = (25), sticky = "e")

#Answer 4 to be entered
a4_ent = tk.Entry(master = q4,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
a4_ent.grid(row = 2, column = 1, padx = (10, 0), pady = (25), sticky = "w")


#Error to be occured if any
q4error = tk.Label(master = q4,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
q4error.grid(row = 3, column = 0, columnspan = 2, pady = (0, 35))

#Next button to go to next question
nextbtn = tk.Button(master = q4,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Next",
    font = btntext,
    command = lambda: [quizfunc.answer(q4_title, a4_ent, q4error, q5), quizfunc.take(a4_ent, q4error), quizfunc.reset(a4_ent, q4error), a5_ent.focus_set()])
nextbtn.grid(row = 4, column = 1, pady = (25,   400))


# # # # # # # # # # # # # # # # Question 5 Frame # # # # # # # # # # # # # # # # # # # #

q5 = tk.Frame(master = god,
    bg = "black")
q5.grid(row = 0, column = 0, sticky = "nsew")

#Title - Quiz
q5_title = tk.Label(master = q5,
    bg = "black",
    fg = "lime",
    text = "Question 5",
    font = heading)
q5_title.grid(row = 0, column = 0, columnspan = 2, pady = (50))

#Question 5 Label
q5_lbl = tk.Label(master = q5,
    bg = "black",
    fg = "lime",
    text = "Question 5:",
    width = 50,
    font = text)
q5_lbl.grid(row = 1, column = 0, columnspan = 2, pady = (25))

#Answer 5 label
a5_lbl = tk.Label(master = q5,
    bg = "black",
    fg = "lime",
    text = "Answer :",
    font = text)
a5_lbl.grid(row = 2, column = 0, padx = (0, 10), pady = (25), sticky = "e")

#Answer 5 to be entered 
a5_ent = tk.Entry(master = q5,
    bg = "black",
    fg = "lime",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2,
    insertbackground = "lime",
    font = text)
a5_ent.grid(row = 2, column = 1, padx = (10, 0), pady = (25), sticky = "w")


#Error to be occured if any
q5error = tk.Label(master = q5,
    bg = "black",
    fg = "red",
    text = "",
    font = text)
q5error.grid(row = 3, column = 0, columnspan = 2, pady = (0, 50))

#Finish button for quiz
finishbtn = tk.Button(master = q5,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Finish",
    font = btntext,
    command = lambda: [quizfunc.answer(q5_title, a5_ent, q5error, finishscrn), quizfunc.scores(a5_ent, q5error), quizfunc.finish(name_lbl, score_lbl, a5_ent, q5error), quizfunc.take(a5_ent, q5error), quizfunc.analyseques(q1lbl, q2lbl, q3lbl, q4lbl, q5lbl), quizfunc.analyse(yourans, yourans1, yourans2, yourans3, yourans4, cans, cans1, cans2, cans3, cans4), quizfunc.reset(a5_ent, q5error)])
finishbtn.grid(row = 4, column = 1, pady = (25, 400))


# # # # # # # # # # # # # # # # Finish Frame # # # # # # # # # # # # # # # # # # # #
finishscrn = tk.Frame(master = god,
    bg = "black")
finishscrn.grid(row = 0, column = 0, sticky = "nsew")

f_title = tk.Label(master = finishscrn,
    bg = "black",
    fg = "lime",
    text = "Congratulations!\n You finished the quiz",
    width = 26,
    font = heading)
f_title.grid(row = 0, column = 0, columnspan = 3, pady = (50), sticky = "w")

name_lbl = tk.Label(master = finishscrn,
    bg = "black",
    fg = "lime",
    text = "",
    font = text)
name_lbl.grid(row = 1, column = 0, columnspan = 3, pady = (25))

score_lbl = tk.Label(master = finishscrn,
    bg = "black",
    fg = "lime",
    text = "",
    font = text)
score_lbl.grid(row = 2, column = 0, columnspan = 3, pady = (25))

leaderboardbtn = tk.Button(master = finishscrn,
    bg = "lime",
    fg = "black",
    width = 14,
    activeforeground = "lime",
    activebackground = "black",
    text = "View Highscore",
    font = btntext,
    command = lambda: [leaderfunc.main(name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10), finishfunc.reset(name_lbl, score_lbl), leaderboard.tkraise()])
leaderboardbtn.grid(row = 3, column = 1, pady = (25, 400))

analysisbtn = tk.Button(master = finishscrn,
    bg = "lime",
    fg = "black",
    width = 14,
    activeforeground = "lime",
    activebackground = "black",
    text = "Analysis",
    font = btntext,
    command = lambda: [finishfunc.reset(name_lbl, score_lbl), analysis.tkraise()])
analysisbtn.grid(row = 3, column = 2, pady = (25, 400))

homebtn = tk.Button(master = finishscrn,
    bg = "lime",
    fg = "black",
    width = 14,
    activeforeground = "lime",
    activebackground = "black",
    text = "Home",
    font = btntext,
    command = lambda: [finishfunc.reset(name_lbl, score_lbl), quizfunc.scorereset(), intro.tkraise()])
homebtn.grid(row = 3, column = 0, pady = (25, 400))


# # # # # # # # # # # # # # # # Analysis Frame # # # # # # # # # # # # # # # # # # # #

analysis = tk.Frame(master = god,
    bg = "black")
analysis.grid(row = 0, column = 0, sticky = "nsew")

analysistitle = tk.Label(master = analysis,
    bg = "black",
    fg = "lime",
    text = "Analysis",
    width = 26,
    font = heading)
analysistitle.grid(row = 0, column = 0, columnspan = 2, sticky = "w")

#Q1 Frame
q1frame = tk.Frame(master = analysis,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
q1frame.grid(row = 1, column = 0, columnspan = 2, sticky = "w")

#Displaying Q1
q1lbl = tk.Label(master = q1frame,
    bg = "black",
    fg = "lime",
    text = "",
    width = 71,
    font = analysistext)
q1lbl.grid(row = 0, column = 0, columnspan = 2, sticky = "w")

#User entered answer 1 label
youranslbl =  tk.Label(master = q1frame,
    bg = "black",
    fg = "lime",
    text= "Your Answer:",
    font = analysistext)
youranslbl.grid(row = 1, column = 0, padx = (100, 0), sticky = "w")

# displays user entered answer 1
yourans =  tk.Label(master = q1frame,
    bg = "black",
    fg = "lime",
    text = "",
    font = analysistext)
yourans.grid(row = 1, column = 1, sticky = "w")

#correct answer 1 label
canslbl =  tk.Label(master = q1frame,
    bg = "black",
    fg = "lime",
    text= "Correct Answer:",
    font = analysistext)
canslbl.grid(row = 2, column = 0, padx = (100, 0), sticky = "w")

#displays correct answer 1
cans =  tk.Label(master = q1frame,
    bg = "black",
    fg = "lime",
    text = "",
    font = analysistext)
cans.grid(row = 2, column = 1, sticky = "w")

#Q2 Frame
q2frame = tk.Frame(master = analysis,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
q2frame.grid(row = 2, column = 0, columnspan = 2, sticky = "w")

#Displaying Q2
q2lbl = tk.Label(master = q2frame,
    bg = "black",
    fg = "lime",
    width = 71,
    font = analysistext)
q2lbl.grid(row = 0, column = 0, columnspan = 2)

#User entered answer 2 label
youranslbl1 =  tk.Label(master = q2frame,
    bg = "black",
    fg = "lime",
    text= "Your Answer:",
    font = analysistext)
youranslbl1.grid(row = 1, column = 0, padx = (100, 0), sticky = "w")

# displays user entered answer 2
yourans1 =  tk.Label(master = q2frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
yourans1.grid(row = 1, column = 1, sticky = "w")

#correct answer 2 label
canslbl1 =  tk.Label(master = q2frame,
    bg = "black",
    fg = "lime",
    text= "Correct Answer:",
    font = analysistext)
canslbl1.grid(row = 2, column = 0, padx = (100, 0), sticky = "w")

#displays correct answer 2
cans1 =  tk.Label(master = q2frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
cans1.grid(row = 2, column = 1, sticky = "w")

#Q3 Frame
q3frame = tk.Frame(master = analysis,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
q3frame.grid(row = 3, column = 0, columnspan = 2, sticky = "w")

#Displaying Q3
q3lbl = tk.Label(master = q3frame,
    bg = "black",
    fg = "lime",
    width = 71,
    font = analysistext)
q3lbl.grid(row = 0, column = 0, columnspan = 2)

#User entered answer 3 label
youranslbl2 =  tk.Label(master = q3frame,
    bg = "black",
    fg = "lime",
    text= "Your Answer:",
    font = analysistext)
youranslbl2.grid(row = 1, column = 0, padx = (100, 0), sticky = "w")

# displays user entered answer 3
yourans2 =  tk.Label(master = q3frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
yourans2.grid(row = 1, column = 1, sticky = "w")

#correct answer 3 label
canslbl2 =  tk.Label(master = q3frame,
    bg = "black",
    fg = "lime",
    text= "Correct Answer:",
    font = analysistext)
canslbl2.grid(row = 2, column = 0, padx = (100, 0), sticky = "w")

#displays correct answer 3
cans2 =  tk.Label(master = q3frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
cans2.grid(row = 2, column = 1, sticky = "w")

#Q4 Frame
q4frame = tk.Frame(master = analysis,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
q4frame.grid(row = 4, column = 0, columnspan = 2, sticky = "w")

#Displaying Q4
q4lbl = tk.Label(master = q4frame,
    bg = "black",
    fg = "lime",
    width = 71,
    font = analysistext)
q4lbl.grid(row = 0, column = 0, columnspan = 2)

#User entered answer 4 label
youranslbl3 =  tk.Label(master = q4frame,
    bg = "black",
    fg = "lime",
    text= "Your Answer:",
    font = analysistext)
youranslbl3.grid(row = 1, column = 0, padx = (100, 0), sticky = "w")

# displays user entered answer 4
yourans3 =  tk.Label(master = q4frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
yourans3.grid(row = 1, column = 1, sticky = "w")

#correct answer 4 label
canslbl3 =  tk.Label(master = q4frame,
    bg = "black",
    fg = "lime",
    text= "Correct Answer:",
    font = analysistext)
canslbl3.grid(row = 2, column = 0, padx = (100, 0), sticky = "w")

#displays correct answer 4
cans3 =  tk.Label(master = q4frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
cans3.grid(row = 2, column = 1, sticky = "w")

#Q5 Frame
q5frame = tk.Frame(master = analysis,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
q5frame.grid(row = 5, column = 0, columnspan = 2, sticky = "w")

#Displaying Q5
q5lbl = tk.Label(master = q5frame,
    bg = "black",
    fg = "lime",
    width = 71,
    font = analysistext)
q5lbl.grid(row = 0, column = 0, columnspan = 2)

#User entered answer 5 label
youranslbl4 =  tk.Label(master = q5frame,
    bg = "black",
    fg = "lime",
    text= "Your Answer:",
    font = analysistext)
youranslbl4.grid(row = 1, column = 0, padx = (100, 0), sticky = "w")

# displays user entered answer 5
yourans4 =  tk.Label(master = q5frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
yourans4.grid(row = 1, column = 1, sticky = "w")

#correct answer 5 label
canslbl4 =  tk.Label(master = q5frame,
    bg = "black",
    fg = "lime",
    text= "Correct Answer:",
    font = analysistext)
canslbl4.grid(row = 2, column = 0, padx = (100, 0), sticky = "w")

#displays correct answer 5
cans4 =  tk.Label(master = q5frame,
    bg = "black",
    fg = "lime",
    font = analysistext)
cans4.grid(row = 2, column = 1, sticky = "w")

#Leaderboard button
leaderboardbtn = tk.Button(master = analysis,
    bg = "lime",
    fg = "black",
    width = 14,
    activeforeground = "lime",
    activebackground = "black",
    text = "View Highscore",
    font = btntext,
    command = lambda: [leaderfunc.main(name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10), analysisfunc.reset(yourans, yourans1, yourans2, yourans3, yourans4, cans, cans1, cans2, cans3, cans4, q1lbl, q2lbl, q3lbl, q4lbl, q5lbl), leaderboard.tkraise()])
leaderboardbtn.grid(row = 6, column = 1, pady = (20, 300))

#Home button
homebtn = tk.Button(master = analysis,
    bg = "lime",
    fg = "black",
    width = 14,
    activeforeground = "lime",
    activebackground = "black",
    text = "Home",
    font = btntext,
    command = lambda: [analysisfunc.reset(yourans, yourans1, yourans2, yourans3, yourans4, cans, cans1, cans2, cans3, cans4, q1lbl, q2lbl, q3lbl, q4lbl, q5lbl), quizfunc.scorereset(), intro.tkraise()])
homebtn.grid(row = 6, column = 0,  pady = (20, 300))


# # # # # # # # # # # # # # # # Leaderboard Frame # # # # # # # # # # # # # # # # # # # #

leaderboard = tk.Frame(master = god,
    bg = "black")
leaderboard.grid(row = 0, column = 0, sticky = "nsew")

#Leaderboard title 
lbtitle = tk.Label(master = leaderboard,
    bg = "black",
    fg = "lime",
    text = "Top 10 Highscores :",
    font = heading,
    width = 26)
lbtitle.grid(row = 0, column = 0, columnspan = 2, pady = (50, 25), sticky = "w")

#Name Frame
nameframe = tk.Frame(master = leaderboard,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
nameframe.grid(row = 1, column = 0, sticky = "e")

#Name heading
nametitle = tk.Label(master = nameframe,
    bg = "black",
    fg = "lime",
    text = "Name:",
    width = 20,
    font = analysistext,)
nametitle.grid(row = 0, column = 0)
 
#Score Frame 
scoreframe = tk.Frame(master = leaderboard,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
scoreframe.grid(row = 1, column = 1, sticky = "w")

#Score heading

scoretitle = tk.Label(master = scoreframe,
    bg = "black",
    fg = "lime",
    text = "Score:",
    width = 20,
    font = analysistext,)
scoretitle.grid(row = 0, column = 1)

#Name Frame 1
nameframe1 = tk.Frame(master = leaderboard,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
nameframe1.grid(row = 2, column = 0, sticky = "e")

#Name 1 Label
name1 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    width = 20,
    font = analysistext,)
name1.grid(row = 0, column = 0)

#Score Frame 1 
scoreframe1 = tk.Frame(master = leaderboard,
    bg = "black",
    highlightbackground = "lime",
    highlightcolor = "lime",
    highlightthickness = 2)
scoreframe1.grid(row = 2, column = 1, sticky = "w")

#Score 1 Label
score1 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    width = 20,
    font = analysistext,)
score1.grid(row = 0, column = 0)

#Name 2 Label
name2 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name2.grid(row = 1, column = 0)

#Score 2 Label
score2 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score2.grid(row = 1, column = 0)

#Name 3 Label
name3 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name3.grid(row = 2, column = 0)

#Score 3 Label
score3 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score3.grid(row = 2, column = 0)

#Name 4 Label
name4 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name4.grid(row = 3, column = 0)

#Score 4 Label
score4 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score4.grid(row = 3, column = 0)

#Name 5 Label
name5 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name5.grid(row = 4, column = 0)

#Score 5 Label
score5 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score5.grid(row = 4, column = 0)

#Name 6 Label
name6 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name6.grid(row = 5, column = 0)

#Score 6 Label
score6 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score6.grid(row = 5, column = 0)

#Name 7 Label
name7 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name7.grid(row = 6, column = 0)

#Score 7 Label
score7 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score7.grid(row = 6, column = 0)

#Name 8 Label
name8 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name8.grid(row = 7, column = 0)

#Score 8 Label
score8 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score8.grid(row = 7, column = 0)

#Name 9 Label
name9 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name9.grid(row = 8, column = 0)

#Score 9 Label
score9 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score9.grid(row = 8, column = 0)

#Name 10 Label
name10 = tk.Label(master = nameframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
name10.grid(row = 9, column = 0)

#Score 10 Label
score10 = tk.Label(master = scoreframe1,
    bg = "black",
    fg = "lime",
    text = "-",
    font = analysistext,)
score10.grid(row = 9, column = 0)

homebtn = tk.Button(master = leaderboard,
    bg = "lime",
    fg = "black",
    width = 13,
    activeforeground = "lime",
    activebackground = "black",
    text = "Home",
    font = btntext,
    command = lambda: [leaderfunc.lbreset(name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10), quizfunc.scorereset(), intro.tkraise()])
homebtn.grid(row = 3, column = 0, columnspan = 2, pady = (25, 0))

intro.tkraise()