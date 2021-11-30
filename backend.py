import sqlite3

class Database:

    #function executes when class is called
    #initialize the  minimal object (est conn to db, create cursor obj,
    #check if tbl exists)
    def __init__(self, db): #add self and db parameters
        conn = sqlite3.connect(db) #sends db param to connect method
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
        conn.commit()
        conn.close()

    def add(title, author, year, isbn):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        conn.commit()
        conn.close()

    def view():
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(title="", author="", year="", isbn=""):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? or year=? or isbn=?",(title, author, year, isbn))
        rows=cur.fetchall()
        conn.close()
        return rows

    def delete(id):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(id, title, author, year, isbn):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("UPDATE book set title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
        conn.commit()
        conn.close()
