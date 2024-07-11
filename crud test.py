import tkinter.messagebox
from tkinter import ttk
from tkinter import *
from pymongo import MongoClient
# database set
Client = MongoClient('localhost', 27017)
db = Client['Crud']
persons = db['Persons']

# functions


def read(person):
    if int(person["age"]) >= 18:
        persons.insert_one(person)


def onclick_read(event=None):
    if registerBtn.cget("state") == NORMAL:
        try:
            if Exist == False :
                person = {"name": name.get(),
                          "family": family.get(),
                          "age": age.get(),
                          "major": combobox.get()}
                read(person)
                alldata = alldata_read()
                cleandata()
                for data in alldata:
                    add_data_totable(data)
                empty_textbox()
                tkinter.messagebox.showinfo("error", "successful sign in")
        except ValueError or KeyError:
            print("try again")


def add_data_totable(person):
    table.insert("", "end", values=[person['name'], person['family'], person['age'], person['major']])


def alldata_read():
    alldata = persons.find()
    return alldata


def cleandata():
    for j in table.get_children():
        table.delete(j)


def empty_textbox():
    NAME.set("")
    FAMILY.set("")
    AGE.set("")

def btn_activation(event=None):
    if name.get() != "" and family.get() != "" and age.get() != "" and combobox.get() != "":
        registerBtn.configure(state=NORMAL)
    else:
        registerBtn.configure(state=DISABLED)

def Exist(person):
    alldata = alldata_read()
    for data in alldata:
        if data["name"] == person["name"] and data["family"] == person['family'] and data['age'] == person['age'] and data['major'] == person['major'] :
            return True
    return False
# main task


win = Tk()
win.geometry("950x600")
win.title("Crud Project")
win.iconbitmap(r"icons/king_icon-icons.com_69359.ico")
win.configure(background="#22011c", height=100, width=100, borderwidth=1, border=2)

NAME = StringVar()
FAMILY = StringVar()
AGE = StringVar()

# texts
name = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", bg="#eeeee4", textvariable=NAME)
name.place(x=100, y=100)
name.bind("<KeyRelease>", btn_activation)


family = Entry(win, bd=5, font=("arial", 15), justify="center", width=25,
               fg="black", background="#eeeee4", textvariable=FAMILY)
family.place(x=100, y=160)

age = Entry(win, bd=5, font=("arial", 15), justify="center", width=25,
            fg="black", background="#eeeee4", textvariable=AGE)
age.place(x=100, y=220)

combobox = ttk.Combobox(win, font=("arial", 15), justify="center",width=24,
              foreground="black", background="#eeeee4")
combobox['values'] = ["computer", "electrical", 'chemistry']
combobox.place(x=100, y=280)

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
registerBtn.configure(textvariable=DISABLED)
registerBtn.bind("<Enter>", lambda event=None: registerBtn.configure(bg="#033cef", fg="white"))
registerBtn.bind("<Leave>", lambda event=None: registerBtn.configure(fg="black", background="#eeeee4"))
registerBtn.bind("<Button-1>", onclick_read)
registerBtn.bind()

# table
table = ttk.Treeview(win, columns=("name", "family", "age", "major"), show="headings")
columns = ("name", "family", "age", "major")
for i in columns:
    table.heading(i, text=i.title())
    table.column(i, width=100, anchor="center")

table.place(x=500, y=75)

win.mainloop()
