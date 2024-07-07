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
win.configure(background="#22011c", height=100, width=100, borderwidth=1, border=2)

# txt
name = Entry(cursor="", width=25, fg="black", background="#eeeee4")
label = win.
name.place(x=100 , y=100)
win.iconbitmap(r"icons/king_icon-icons.com_69359.ico")

# lbl


# btn
# registerBtn=
win.mainloop()
