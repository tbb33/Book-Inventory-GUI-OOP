import sqlite3

class Database:

    #function executes when class is called
    #initialize the  minimal object (est conn to db, create cursor obj,
    #check if tbl exists)
    def __init__(self, db): #add self and db parameters
        self.conn = sqlite3.connect(db) #sends db param to connect method
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
        self.conn.commit()

    def add(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        self.conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? or year=? or isbn=?",(title, author, year, isbn))
        rows=self.cur.fetchall()
        self.conn.close()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        self.conn.close()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book set title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
        self.conn.commit()
        self.conn.close()
