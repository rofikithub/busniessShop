import sqlite3
from tkinter import messagebox
from controller.ConnectionController import Database
database = Database()

class Sale:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS sales (
                                        id INTEGER PRIMARY KEY,
                                        cid INT NOT NULL,
                                        total INTEGER NOT NULL,
                                        less INTEGER NULL,
                                        due INTEGER NULL,
                                        paid INTEGER NOT NULL,
                                        status INT DEFAULT 0,
                                        profit INTEGER NOT NULL,
                                        created DATE NOT NULL
                                    )''')

    def create(self,data):
        query = 'INSERT INTO sales (cid, total, less, due, paid,status,profit,created) VALUES (?,?,?,?,?,?,?,?)'
        params = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        result = database.insert(query, params)
        if result > 0:
            return result
        else:
            return None

    def all(self):
        query = ("SELECT * FROM sales")
        result = database.select(query)
        if not len(result) == 0:
            return result
        else:
            return None

    def getall(self):
        query = 'SELECT s.*, c.customer_name, c.mobile, c.email FROM sales as s, customers as c WHERE c.id = s.cid'
        result = database.select(query)
        if result:
            return result
        else:
            return None

    def getdue(self):
        query = 'SELECT s.*, c.customer_name, c.mobile, c.email FROM sales as s, customers as c WHERE c.id = s.cid AND s.status=1'
        result = database.select(query)
        if result:
            return result
        else:
            return None

    def fromTo(self,data):
        query = 'SELECT s.*, c.customer_name, c.mobile, c.email FROM sales as s, customers as c WHERE c.id = s.cid AND s.created BETWEEN ? AND ?'
        params = (data[0], data[1])
        result = database.onselect(query,params)
        if result:
            return result
        else:
            return None

    def getid(self,name):
        query = 'SELECT id FROM sales WHERE cid=?'
        params = (name,)
        result = database.onselect(query,params)
        if result:
            return result[0]
        else:
            return None


    def getbill(self,id):
        query = 'SELECT s.*, c.customer_name, c.mobile, c.email FROM sales as s, customers as c WHERE c.id = s.cid AND s.id = ?'
        params = (id,)
        result = database.onselect(query,params)
        if result:
            return result[0]
        else:
            return None

    def update(self,data):
        query = "UPDATE sales SET due = ?, paid = ?, status = ? WHERE id = ?"
        params = (data[0],data[1],data[2],data[3])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None
        
    def updateReturn(self,data):
        query = "UPDATE sales SET total = ?, less = ?, due = ?, paid = ?, status = ?, profit =? WHERE id = ?"
        params = (data[0],data[1],data[2],data[3],data[4],data[5],data[6])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None