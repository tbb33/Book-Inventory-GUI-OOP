"""
This program stores book info including:
Title, Year, Author, and ISBN.

User can:
View all records
Search for an entry
Add Entry
Update Entry
Delete Entry
close
"""

import tkinter
from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    try:
        index = list.curselection()[0]
        selected_tuple = list.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1]) #insert title to title entry widget
        e3.delete(0,END)
        e3.insert(END,selected_tuple[2]) #author
        e2.delete(0,END)
        e2.insert(END,selected_tuple[3]) #year
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4]) #isbn
    except IndexError:
        pass

def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        list.insert(END,row)

def add_command():
    backend.add(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    list.delete(0,END)
    list.insert(END, (title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_value.get(),author_value.get(),year_value.get(),isbn_value.get())

window=Tk()
window.title("Bookstore Inventory")

#labels
b1=Label(window, text="Title")
b1.grid(row=0,column=0)
b2=Label(window, text="Year")
b2.grid(row=1,column=0)
b3=Label(window, text="Author")
b3.grid(row=0,column=2)
b4=Label(window, text="ISBN")
b4.grid(row=1,column=2)

#entries
title_value=StringVar()
e1=Entry(window, textvariable=title_value, width=14)
e1.grid(row=0,column=1)

year_value=StringVar()
e2=Entry(window, textvariable=year_value,width=14)
e2.grid(row=1,column=1)

author_value=StringVar()
e3=Entry(window, textvariable=author_value,width=14)
e3.grid(row=0,column=3)

isbn_value=StringVar()
e4=Entry(window, textvariable=isbn_value,width=14)
e4.grid(row=1,column=3)

#buttons
b1=Button(window, text="View all", width=14, command=view_command)
b1.grid(row=2,column=3)
b2=Button(window, text= "Search entry",width=14, command=search_command)
b2.grid(row=3,column=3)
b3=Button(window, text="Add entry",width=14, command=add_command)
b3.grid(row=4,column=3)
b4=Button(window, text="Update",width=14, command=update_command)
b4.grid(row=5,column=3)
b5=Button(window, text="Delete",width=14, command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window, text="Close",width=14, command=window.destroy)
b6.grid(row=7,column=3)

#listbox
list=Listbox(window,height=6,width=35)
list.grid(row=2,column=0, rowspan=6, columnspan=2)

s=Scrollbar(window)
s.grid(row=3,column=2, rowspan=4, sticky='ns')
list.configure(yscrollcommand=s.set)
s.configure(command=list.yview)

list.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()
