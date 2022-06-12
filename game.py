from tkinter import *
from tkinter import font
from random import randint
from functools import partial

win = Tk()

select = {
     1:"stone",
     2:"paper",
     3:"scissor",
}

def game(num):
     com = randint(1, 3)
     lbl1["text"] = "computer: " + select[com]
     if num == 0:
          if com == 3:
               userscore["text"] = int(userscore["text"]) + 1
          elif com == 2:
               computerscore["text"] = int(computerscore["text"]) + 1
     elif num == 1:
          if com == 1:
               userscore["text"] = int(userscore["text"]) + 1
          elif com == 3:
               computerscore["text"] = int(computerscore["text"]) + 1
     elif num == 2:
          if com == 2:
               userscore["text"] = int(userscore["text"]) + 1
          elif com == 1:
               computerscore["text"] = int(computerscore["text"]) + 1
def rst():
     computerscore["text"] = 0
     userscore["text"] = 0
     lbl1["text"] = "Select"

win.title("stone paper scissor")
win.minsize(300, 350)
win.rowconfigure([0, 1], weight=1)
win.columnconfigure(0, weight=1) 

lbl1 = Label(master=win, text="Select", height=2, 
    font=("none", 18, "bold"), bg="#fff")
lbl1.grid(column=0, row=0, sticky="nwe")

frmbtn = Frame(master=win, height=100, bg="red")
frmbtn.rowconfigure(0, weight=1)
frmbtn.columnconfigure([0, 1, 2], weight=1)

stonebtn = Button(master=frmbtn, text="stone", height=2, command=partial(game, 0),
     font=("none", 16, "bold")).grid(column=0, row=0, sticky="new", padx=2, pady=3)
paperbtn = Button(master=frmbtn, text="paper", height=2, command=partial(game, 1),
     font=("none", 16, "bold")).grid(column=1, row=0, sticky="new", padx=2, pady=3)
scissorsbtn = Button(master=frmbtn, text="scissor", height=2, command=partial(game, 2),
     font=("none", 16, "bold")).grid(column=2, row=0, sticky="new", padx=2, pady=3)

frmbtn.grid(row=1, column=0, sticky="wen")

frmscore = Frame(master=win, height=200)
frmscore.rowconfigure([0, 1], weight=1)
frmscore.columnconfigure([0, 1], weight=1)

userscorename = Label(master=frmscore, text='     your score   ', relief=RIDGE, borderwidth=3).grid(
     column=0, row=0, sticky='nswe')
computerscorename = Label(master=frmscore, text='computer score', relief=RIDGE, borderwidth=3).grid(
     column=1, row=0, sticky='nswe')
userscore = Label(master=frmscore, text="0", height=5, bg='yellow', font=("none", 22, 'bold'))
userscore.grid(column=0, row=1, sticky='nswe')
computerscore = Label(master=frmscore, text="0", height=5, bg='green', font=("none", 22, 'bold'))
computerscore.grid(column=1, row=1, sticky='nswe')

frmscore.grid(column=0, row=2, sticky='nswe')

btn = Button(master=win, text='new game', relief=RIDGE, borderwidth=3, height=3, command=rst).grid(
     column=0, row=3, sticky='nswe')
     
mainloop()
