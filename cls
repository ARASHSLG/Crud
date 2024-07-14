[1mdiff --git a/crud test.py b/crud test.py[m
[1mindex d0e189c..9e56534 100644[m
[1m--- a/crud test.py[m	
[1m+++ b/crud test.py[m	
[36m@@ -21,6 +21,7 @@[m [mdef onclick_read(event):[m
               "major": major.get()}[m
     read(person)[m
     alldata = alldata_read()[m
[32m+[m[32m    cleandata()[m
     for data in alldata:[m
         add_data_totable(data)[m
 [m
[36m@@ -33,6 +34,14 @@[m [mdef alldata_read():[m
     alldata = persons.find()[m
     return alldata[m
 [m
[32m+[m
[32m+[m[32mdef cleandata():[m
[32m+[m[32m    for j in table.get_children():[m
[32m+[m[32m        table.delete(j)[m
[32m+[m
[32m+[m
[32m+[m[32mdef empty_textbox():[m
[32m+[m[32m    pass[m
 # main task[m
 [m
 [m
[36m@@ -42,17 +51,20 @@[m [mwin.title("Crud Project")[m
 win.iconbitmap(r"icons/king_icon-icons.com_69359.ico")[m
 win.configure(background="#22011c", height=100, width=100, borderwidth=1, border=2)[m
 [m
[32m+[m[32mNAME = StringVar()[m
[32m+[m[32mFAMILY = StringVar()[m
[32m+[m[32mAGE = StringVar()[m
[32m+[m[32mMAJOR = StringVar()[m
 # texts[m
[31m-name = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", bg="#eeeee4")[m
[31m-name.place(x=100, y=100)[m
[32m+[m[32mname = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", bg="#eeeee4", textvariable=NAME)[m
 [m
[31m-family = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")[m
[32m+[m[32mfamily = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4", textvariable=FAMILY)[m
 family.place(x=100, y=160)[m
 [m
[31m-age = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")[m
[32m+[m[32mage = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4", textvariable=AGE)[m
 age.place(x=100, y=220)[m
 [m
[31m-major = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4")[m
[32m+[m[32mmajor = Entry(win, bd=5, font=("arial", 15), justify="center", width=25, fg="black", background="#eeeee4", textvariable=MAJOR)[m
 major.place(x=100, y=280)[m
 [m
 # labels[m
[36m@@ -86,7 +98,7 @@[m [mtable = ttk.Treeview(win, columns=("name", "family", "age", "major"), show="head[m
 columns = ("name", "family", "age", "major")[m
 for i in columns:[m
     table.heading(i, text=i.title())[m
[31m-    table.column(i, width=100)[m
[32m+[m[32m    table.column(i, width=100, anchor="center")[m
 [m
 table.place(x=500, y=75)[m
 [m
