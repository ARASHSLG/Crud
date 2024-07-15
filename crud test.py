from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from pymongo import MongoClient
# database set
Client = MongoClient('localhost', 27017)
db = Client['Crud']
persons = db['Persons']

# functions


def btnhovers(e):
    if e.widget["text"] == "Submit":
        registerBtn.configure(bg="#eeeee4", fg="black")
    elif e.widget["text"] == "Search":
        searchBtn.configure(bg="#3f91fc", fg="black")
    elif e.widget["text"] == "Delete":
        deleteBtn.configure(bg="#fc3f3f", fg="black")
    else:
        updateBtn.configure(bg="#5F5F5F", fg="white")


def default_style(e):
    if e.widget["text"] == "Submit":
        registerBtn.configure(fg="white", background="#ff7a05")
    elif e.widget["text"] == "Search":
        searchBtn.configure(fg="white", background="#154c79")
    elif e.widget["text"] == "Delete":
        deleteBtn.configure(fg="white", background="#820404")
    else:
        updateBtn.configure(bg="white", fg="black")
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


def onclick_delete(e):
    msg = messagebox.askyesno("Deleting Data", "Are You Sure ?")
    if msg:
        select = table.selection()
        if select != ():
            data = table.item(select)["values"]
            delete(data)
            table.delete(select)


def delete(del_data):
    alldata = alldata_read()
    for data in alldata:
        if (data["name"] == del_data[0] and data["family"] == del_data[1] and
                data['age'] == del_data[2] and data['major'] == del_data[3]):
            persons.delete_one(data)


def selected_item(e):
    select = table.selection()
    if select != ():
        data = table.item(select)["values"]
        NAME.set(data[0])
        FAMILY.set(data[1])
        combobox.set(data[2])
        AGE.set(data[3])


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


def onclick_update(e):
    msg = messagebox.askyesno("Updating Data", "Are You Sure ?")
    if msg:
        select = table.selection()
        if select != ():
            data = table.item(select)["values"]
            old_data = {"name": data[0], "family": data[1], "age": data[2], "major": data[3]}
            newdata = {"name": name.get(), "family": family.get(), "age": age.get(), "major": combobox.get()}
            update(old_data, newdata)
            cleandata()
            load_data()


def update(old_data, new_data):
    alldata = alldata_read()
    for data in alldata:
        if (data["name"] == old_data[0] and data["family"] == old_data[1] and
                data['age'] == old_data[2] and data['major'] == old_data[3]):
            new = {"$set": new_data}
            persons.update_one(old_data, new)


# main task
win = Tk()
win.attributes("-fullscreen", True)
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
name.place(x=150, y=250)
name.bind("<KeyRelease>", btn_activation)


family = Entry(win, bd=5, font=("arial", 15), justify="center", width=25,
               fg="black", background="#eeeee4", textvariable=FAMILY)
family.place(x=150, y=310)
family.bind("<KeyRelease>", btn_activation)

age = Entry(win, bd=5, font=("arial", 15), justify="center", width=25,
            fg="black", background="#eeeee4", textvariable=AGE)
age.place(x=150, y=370)
age.bind("<KeyRelease>", btn_activation)

combobox = ttk.Combobox(win, font=("arial", 15), justify="center", width=24,
                        foreground="black", background="#eeeee4")
combobox['values'] = ["computer", "electrical", 'chemistry']
combobox.place(x=150, y=430)
combobox.bind("<KeyRelease>", btn_activation)

search_by_name = Entry(win, bd=45, font=("arial", 15), justify="center", width=30,
                       fg="#22011c", bg="#eeeee4", border=5, textvariable=SEARCH)
search_by_name.place(x=526, y=245)
search_by_name.bind("<KeyRelease>", btn_activation)

# labels
welcomelabel = Label(win, text="Welcome To Crud MiniProject",
                     font=("segoe script", 32), fg="white", bg="#22011c")
welcomelabel.place(x=400, y=10)

partlabel = Label(win, text="Adding Part", font=("elephant", 20), bd=5, fg="white", bg="#22011c")
partlabel.place(x=200, y=175)

nmlabel = Label(win, text="Name : ", font=("elephant", 15), bd=5, fg="white", bg="#22011c")
nmlabel.place(x=20, y=250)

fmlabel = Label(win, text="Family : ", font=("elephant", 15), bd=5, fg="white", bg="#22011c")
fmlabel.place(x=17, y=310)

agelabel = Label(win, text="Age : ", font=("elephant", 15), width=5, bd=5, fg="white", bg="#22011c")
agelabel.place(x=28, y=370)

majorlabel = Label(win, text="Major : ", font=("elephant", 15), width=5, bd=5, fg="white", bg="#22011c")
majorlabel.place(x=35, y=430)

searchlabel = Label(win, text="Search Box", font=("elephant", 20), bd=5, fg="white", bg="#22011c")
searchlabel.place(x=620, y=175)

# button
registerBtn = Button(win, cursor="hand2", text='Submit', bd=5,
                     font=("arial", 15), width=12, fg="white", background="#ff7a05")
registerBtn.place(x=212, y=510)
# registerBtn.configure(textvariable=DISABLED)
registerBtn.bind("<Enter>", btnhovers)
registerBtn.bind("<Leave>", default_style)
registerBtn.bind("<Button-1>", onclick_read)
registerBtn.bind()

searchBtn = Button(win, cursor="hand2", text='Search', bd=5,
                   font=("arial", 15), width=12, fg="white", background="#154c79")
searchBtn.place(x=620, y=300)
# searchBtn.configure(textvariable=DISABLED)
searchBtn.bind("<Enter>", btnhovers)
searchBtn.bind("<Leave>", default_style)
searchBtn.bind("<Button-1>", onclick_search)

deleteBtn = Button(win, cursor="hand2", text='Delete', bd=5,
                   font=("arial", 15), width=12, fg="white", background="#820404")
deleteBtn.place(x=1355, y=510)
# deleteBtn.configure(textvariable=DISABLED)
deleteBtn.bind("<Enter>", btnhovers)
deleteBtn.bind("<Leave>", default_style)
deleteBtn.bind("<Button-1>", onclick_delete)

updateBtn = Button(win, cursor="hand2", text='Update', bd=5,
                   font=("arial", 15), width=12, fg="black", background="white")
updateBtn.place(x=900, y=510)
# deleteBtn.configure(textvariable=DISABLED)
updateBtn.bind("<Enter>", btnhovers)
updateBtn.bind("<Leave>", default_style)
updateBtn.bind("<Button-1>", onclick_update)

exit_image = PhotoImage(file="image/icons8-exit-24.png")
exitbtn = Button(win, image=exit_image, width=25, height=25)
exitbtn.place(x=1500, y=0)
exitbtn.bind("<Button-1>", exit)
# table
table = ttk.Treeview(win, columns=("name", "family", "age", "major"), show="headings", height=15)
columns = ("name", "family", "age", "major")
for i in columns:
    table.heading(i, text=i.title())
    table.column(i, width=150, anchor="center")
table.bind("<Button-1>", selected_item)
table.place(x=900, y=175)
# load_data()
win.mainloop()
