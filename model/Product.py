import sqlite3
from tkinter import messagebox
from controller.ConnectionController import Database
database = Database()

class Product:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS products (
                                        id INTEGER PRIMARY KEY,
                                        product_name TEXT NOT NULL,
                                        category TEXT NOT NULL,
                                        quantity INTEGER NOT NULL,
                                        sall_price REAL NOT NULL,
                                        cost_price REAL NOT NULL
                                    )''')

    def create(self,data):
        query = 'INSERT INTO products (product_name, category, quantity, sall_price, cost_price) VALUES (?,?,?,?,?)'
        params = (data[0], data[1], data[2], data[3], data[4])
        result = database.insert(query, params)
        if result > 0:
            return result
        else:
            return None

    def all(self):
        query = ("SELECT * FROM products")
        result = database.select(query)
        if result:
            return result
        else:
            return None
        
    def chack(name):
        query = 'SELECT * FROM products WHERE product_name=?'
        params = (name,)
        result = database.onselect(query,params)
        if result:
            return result
        else:
            return None

    def onselect(name):
        list = []
        query = 'SELECT * FROM products WHERE category=?'
        params = (name,)
        result = database.onselect(query,params)
        if result:
            for item in result:
                list.append(item[1])
        return list

    def price(name):
        query = 'SELECT sall_price FROM products WHERE product_name=?'
        params = (name,)
        result = database.onselect(query,params)
        if result:
            return result[0][0]
        else:
            return None

    def getid(self,name):
        query = 'SELECT id FROM products WHERE product_name=?'
        params = (name,)
        result = database.onselect(query,params)
        if not result == []:
            return result[0][0]
        else:
            return None

    def pname(id):
        query = 'SELECT product_name FROM products WHERE id=?'
        params = (id,)
        result = database.onselect(query,params)
        if result:
            return result[0][0]
        else:
            return None


    def updateName(self,values):
        query = "UPDATE products SET product_name=?,category=?,quantity=?,sall_price=?,cost_price=? WHERE id=?"
        params = (values[1],values[2],values[3],values[4],values[5],values[0])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None

    def update(self,values):
        query = "UPDATE products SET category=?,quantity=?,sall_price=?,cost_price=? WHERE id=?"
        params = (values[1],values[2],values[3],values[4],values[0])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None


    def getQun(self,id):
        query = 'SELECT quantity FROM products WHERE id=?'
        params = (id,)
        result = database.onselect(query,params)
        if result:
            return result[0][0]
        else:
            return None

    def updateQun(self,data):
        query = "UPDATE products SET quantity=? WHERE id=?"
        params = (data[1],data[0])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None