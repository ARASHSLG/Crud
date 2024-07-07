# from tkinter import *
# from pymongo import MongoClient
# client = MongoClient("localhost", 27017)
# db = client['Crud']
# persons = db['Person']
# win = Tk()
# win.geometry("800x200")
# win.title('Crud Project')
# win.iconbitmap(r"C:\Users\arash\Desktop\Coding\Python\crud\icons\Screenshot 2024-05-23 013137.png")
#
# win.mainloop()
import tkinter
from tkinter import *
from pymongo import MongoClient
# server set
Client = MongoClient("localhost", 27017)
db = Client["Crud"]
persons = db["Persons"]

# main task
win = Tk()
win.geometry("800x600")
win.title("Crud Project")
win.iconbitmap(r"icons/king_icon-icons.com_69359.ico")
win.configure(background="#22011c", height=100, width=100, borderwidth=1, border=2)

# txt
name = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", bg="#eeeee4")
name.place(x=100, y=100)

family = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")
family.place(x=100, y=160)

age = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")
age.place(x=100, y=220)


# lbl
nmlabel = tkinter.Label(win, text="Name : ", font=("arial", 15), width=5, bd=5, fg="white", bg="#22011c")
nmlabel.place(x=25, y=100)

fmlabel = tkinter.Label(win, text="Family : ", font=("arial", 15), width=6, bd=5, fg="white", bg="#22011c")
fmlabel.place(x=20, y=160)

agelabel = tkinter.Label(win, text="age : ", font=("arial", 15), width=5, bd=5, fg="white", bg="#22011c")
agelabel.place(x=25, y=220)

# btn
registerBtn = Button(win, cursor="hand2", text='submit', bd=5, font=("arial", 15), width=12, fg="black", background="#eeeee4")
registerBtn.place(x=165, y=280)

win.mainloop()
