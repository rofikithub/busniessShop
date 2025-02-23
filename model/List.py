import sqlite3
from tkinter import messagebox
from controller.ConnectionController import Database
database = Database()

class List:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS lists (
                                        id INTEGER PRIMARY KEY,
                                        cid INT NULL,
                                        sid INT NOT NULL,
                                        pid INTEGER NOT NULL,
                                        price INTEGER NOT NULL,
                                        qun INTEGER NOT NULL
                                    )''')

    def create(self,values):
        query = 'INSERT INTO lists (cid, sid, pid, price, qun) VALUES (?,?,?,?,?)'
        params = (values[0], values[1], values[2], values[3],values[4])
        result = database.insert(query, params)
        if result > 0:
            return result
        else:
            return None

    def all(self):
        query = ("SELECT * FROM lists")
        result = database.select(query)
        if not result == []:
            return result
        else:
            return None


    def update(sid):
        query = "UPDATE lists SET status = 0 WHERE sid = ?"
        params = (sid)
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None


    def getList(self,sid):
        query = 'SELECT l.*,p.product_name FROM lists as l, products as p WHERE p.id = l.pid AND l.sid = ?'
        params = (sid,)
        result = database.onselect(query,params)
        if not result == []:
            return result
        else:
            return None
        
    def updateReturn(qun,lid):
        query = "UPDATE lists SET qun = ? WHERE id = ?"
        params = (qun,lid)
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None