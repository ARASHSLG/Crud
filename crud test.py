from tkinter import messagebox
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
            if not exist:
                person = {"name": name.get(),
                          "family": family.get(),
                          "age": age.get(),
                          "major": combobox.get()}
                read(person)
                cleandata()
                load_data()
                empty_textbox()
                messagebox.showinfo("error", "successful sign in")
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


def exist(person):
    alldata = alldata_read()
    for data in alldata:
        if (data["name"] == person["name"] and data["family"] == person['family'] and
                data['age'] == person['age'] and data['major'] == person['major']):
            return True
    return False


def onclick_delete():
    user_request = search_by_name.get()
    persons.find(user_request)
def delete_by_name():
    pass
def onclick_search(e):
    user_request = search_by_name.get()
    result = search(user_request)
    cleandata()
    for data in result:
        add_data_totable(data)


def search(user_request):
    alldata = alldata_read()
    result = []
    for data in alldata:
        if (data["name"] == user_request or data["family"] == user_request
                or data["major"] == user_request or data["age"] == user_request):
            result.append(data)
    return result


def load_data():
    alldata = alldata_read()
    for data in alldata:
        add_data_totable(data)


# main task
win = Tk()
win.geometry("950x600")
win.title("Crud Project")
win.iconbitmap(r"icons/king_icon-icons.com_69359.ico")
win.configure(background="#22011c", height=100, width=100, borderwidth=1, border=2)

# vars
NAME = StringVar()
FAMILY = StringVar()
AGE = StringVar()
SEARCH = StringVar()
DELETE = StringVar()
# texts
name = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", bg="#eeeee4", textvariable=NAME)
name.place(x=100, y=100)
name.bind("<KeyRelease>", btn_activation)


family = Entry(win, bd=5, font=("arial", 15), justify="center", width=25,
               fg="black", background="#eeeee4", textvariable=FAMILY)
family.place(x=100, y=160)
family.bind("<KeyRelease>", btn_activation)

age = Entry(win, bd=5, font=("arial", 15), justify="center", width=25,
            fg="black", background="#eeeee4", textvariable=AGE)
age.place(x=100, y=220)
age.bind("<KeyRelease>", btn_activation)

combobox = ttk.Combobox(win, font=("arial", 15), justify="center", width=24,
                        foreground="black", background="#eeeee4")
combobox['values'] = ["computer", "electrical", 'chemistry']
combobox.place(x=100, y=280)
combobox.bind("<KeyRelease>", btn_activation)

search_by_name = Entry(win, bd=45, font=("arial", 15), justify="center", width=30,
                       fg="#22011c", bg="#eeeee4", border=5, textvariable=SEARCH)
search_by_name.place(x=526, y=400)
search_by_name.bind("<KeyRelease>", btn_activation)

# labels
welcomelabel = Label(win, text="Welcome To Crud MiniProject",
                     font=("segoe script", 25), fg="white", bg="#22011c")
welcomelabel.place(x=300, y=0)

nmlabel = Label(win, text="Name : ", font=("elephant", 15), bd=5, fg="white", bg="#22011c")
nmlabel.place(x=5, y=100)

fmlabel = Label(win, text="Family : ", font=("elephant", 15), bd=5, fg="white", bg="#22011c")
fmlabel.place(x=2, y=160)

agelabel = Label(win, text="Age : ", font=("elephant", 15), width=5, bd=5, fg="white", bg="#22011c")
agelabel.place(x=13, y=220)

majorlabel = Label(win, text="Major : ", font=("elephant", 15), width=5, bd=5, fg="white", bg="#22011c")
majorlabel.place(x=10, y=280)

search_deletelabel = Label(win, text="Search & Delete Box", font=("elephant", 15), bd=5, fg="white", bg="#22011c")
search_deletelabel.place(x=580, y=350)

# button
registerBtn = Button(win, cursor="hand2", text='submit', bd=5,
                     font=("arial", 15), width=12, fg="white", background="#ffba7a")
registerBtn.place(x=165, y=340)
registerBtn.configure(textvariable=DISABLED)
registerBtn.bind("<Enter>", lambda event=None: registerBtn.configure(bg="#eeeee4", fg="black"))
registerBtn.bind("<Leave>", lambda event=None: registerBtn.configure(fg="white", background="#ffba7a"))
registerBtn.bind("<Button-1>", onclick_read)
registerBtn.bind()

searchBtn = Button(win, cursor="hand2", text='Search', bd=5,
                   font=("arial", 15), width=12, fg="white", background="#154c79")
searchBtn.place(x=550, y=450)
# searchBtn.configure(textvariable=DISABLED)
searchBtn.bind("<Enter>", lambda event=None: searchBtn.configure(bg="#3f91fc", fg="black"))
searchBtn.bind("<Leave>", lambda event=None: searchBtn.configure(fg="white", background="#154c79"))
searchBtn.bind("<Button-1>", onclick_search)

deleteBtn = Button(win, cursor="hand2", text='Delete', bd=5,
                   font=("arial", 15), width=12, fg="white", background="#820404")
deleteBtn.place(x=700, y=450)
# deleteBtn.configure(textvariable=DISABLED)
deleteBtn.bind("<Enter>", lambda event=None: deleteBtn.configure(bg="#fc3f3f", fg="black"))
deleteBtn.bind("<Leave>", lambda event=None: deleteBtn.configure(fg="white", background="#820404"))
# deleteBtn.bind("<Button-1>", onclick_search)


# table
table = ttk.Treeview(win, columns=("name", "family", "age", "major"), show="headings")
columns = ("name", "family", "age", "major")
for i in columns:
    table.heading(i, text=i.title())
    table.column(i, width=100, anchor="center")

table.place(x=500, y=75)
# load_data()
win.mainloop()
