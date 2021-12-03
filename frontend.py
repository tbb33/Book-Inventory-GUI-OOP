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
#import Database class from backend script - Database blueprint
from backend import Database
selected_tuple=()

#create object from Database blueprint
database=Database("book.db")

class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.title("Bookstore Inventory")

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
        self.title_value=StringVar()
        self.e1=Entry(window, textvariable=self.title_value, width=14)
        self.e1.grid(row=0,column=1)

        self.year_value=StringVar()
        self.e2=Entry(window, textvariable=self.year_value,width=14)
        self.e2.grid(row=1,column=1)

        self.author_value=StringVar()
        self.e3=Entry(window, textvariable=self.author_value,width=14)
        self.e3.grid(row=0,column=3)

        self.isbn_value=StringVar()
        self.e4=Entry(window, textvariable=self.isbn_value,width=14)
        self.e4.grid(row=1,column=3)

        #buttons
        b1=Button(window, text="View all", width=14, command=self.view_command)
        b1.grid(row=2,column=3)
        b2=Button(window, text= "Search entry",width=14, command=self.search_command)
        b2.grid(row=3,column=3)
        b3=Button(window, text="Add entry",width=14, command=self.add_command)
        b3.grid(row=4,column=3)
        b4=Button(window, text="Update",width=14, command=self.update_command)
        b4.grid(row=5,column=3)
        b5=Button(window, text="Delete",width=14, command=self.delete_command)
        b5.grid(row=6,column=3)
        b6=Button(window, text="Close",width=14, command=window.destroy)
        b6.grid(row=7,column=3)

        #listbox
        self.list=Listbox(window,height=6,width=35)
        self.list.grid(row=2,column=0, rowspan=6, columnspan=2)

        s=Scrollbar(window)
        s.grid(row=3,column=2, rowspan=4, sticky='ns')
        self.list.configure(yscrollcommand=s.set)
        s.configure(command=self.list.yview)
        self.list.bind('<<ListboxSelect>>', self.get_selected_row)


    def get_selected_row(self, event):
        global selected_tuple
        try:
            index = self.list.curselection()[0] #grabs 1st item form tuple;index of from listbox
            self.selected_tuple = self.list.get(index) #gets tuple from listbox with specified index
            self.e1.delete(0,END) #empty entry widget
            self.e1.insert(END,self.selected_tuple[1]) #insert author to author entry widget
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[2]) #author
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[3]) #year
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4]) #isbn
        except IndexError:
            pass

    def view_command(self):
        self.list.delete(0,END)
        #refers to view func of database obj which is instance of Database class
        for row in database.view():
            self.list.insert(END,row)

    def search_command(self):
        self.list.delete(0,END)
        for row in database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()):
            self.list.insert(END,row)

    def add_command(self):
        database.add(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.list.delete(0,END)
        self.list.insert(END, (self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())

window=Tk()
Window(window)
window.mainloop()
