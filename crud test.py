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
from tkinter import ttk
from tkinter import *
from pymongo import MongoClient
# database set
Client = MongoClient("localhost", 27017)
db = Client["Crud"]
persons = db["Persons"]

# functions


def read(person):
    persons.insert_one(person)


def onclick_read(event):
    person = {"name": name.get(),
              "family": family.get(),
              "age": age.get(),
              "major": major.get()}
    read(person)
    alldata = alldata_read()
    for data in alldata:
        add_data_totable(data)


def add_data_totable(person):
    table.insert("", "end", values=[person['name'],person['family'], person['age'], person['major']])


def alldata_read():
    alldata = persons.find()
    return alldata

# main task


win = Tk()
win.geometry("950x600")
win.title("Crud Project")
win.iconbitmap(r"icons/king_icon-icons.com_69359.ico")
win.configure(background="#22011c", height=100, width=100, borderwidth=1, border=2)

# texts
name = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", bg="#eeeee4")
name.place(x=100, y=100)

family = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")
family.place(x=100, y=160)

age = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")
age.place(x=100, y=220)

major = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")
major.place(x=100, y=280)

# labels
welcomelabel = tkinter.Label(win, text="Welcome To Crud MiniProject",
                             font=("new times roman", 25), fg="white", bg="#22011c")
welcomelabel.place(x=300, y=0)

nmlabel = tkinter.Label(win, text="Name : ", font=("times", 15), width=5, bd=5, fg="white", bg="#22011c")
nmlabel.place(x=25, y=100)

fmlabel = tkinter.Label(win, text="Family : ", font=("times", 15), width=6, bd=5, fg="white", bg="#22011c")
fmlabel.place(x=20, y=160)

agelabel = tkinter.Label(win, text="age : ", font=("times", 15), width=5, bd=5, fg="white", bg="#22011c")
agelabel.place(x=25, y=220)

majorlabel = tkinter.Label(win, text="Major : ", font=("times", 15), width=5, bd=5, fg="white", bg="#22011c")
majorlabel.place(x=25, y=280)

# button
registerBtn = Button(win, cursor="hand2", text='submit', bd=5,
                     font=("arial", 15), width=12, fg="black", background="#eeeee4")
registerBtn.place(x=165, y=340)
registerBtn.bind("<Enter>", lambda event: registerBtn.configure(bg="#033cef", fg="white"))
registerBtn.bind("<Leave>", lambda event: registerBtn.configure(fg="black", background="#eeeee4"))
registerBtn.bind("<Button-1>", onclick_read)


# table
table = ttk.Treeview(win, columns=("name", "family", "age", "major"), show="headings")
columns = ("name", "family", "age", "major")
for i in columns:
    table.heading(i, text=i.title())
    table.column(i, width=100)

table.place(x=500, y=75)

win.mainloop()
