import sqlite3
from tkinter import messagebox
from controller.ConnectionController import Database
database = Database()

class Customer:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS customers (
                                        id INTEGER PRIMARY KEY,
                                        customer_name TEXT NOT NULL,
                                        mobile TEXT NOT NULL,
                                        email TEXT NULL
                                    )''')

    def create(self,data):
            query = 'INSERT INTO customers (customer_name, mobile, email) VALUES (?,?,?)'
            params = (data[0], data[1], data[2])
            result = database.insert(query, params)
            if not result == []:
                return result
            else:
                return None

    def all(self):
        query = ("SELECT * FROM customers")
        result = database.select(query)
        if not result == []:
            return result
        else:
            return None
        
    def chack(self,mobile):
        Customer.table(self)
        query = 'SELECT * FROM customers WHERE mobile=?'
        params = (mobile,)
        result = database.onselect(query,params)
        if not result == []:
            return result
        else:
            return None

    def onselect(self,mobile):
        list = []
        query = 'SELECT * FROM customers WHERE mobile=?'
        params = (mobile,)
        result = database.onselect(query,params)
        if not result == []:
            for item in result:
                list.append(item[1])
                list.append(item[3])
        return list

    def getemail(self,name):
        query = 'SELECT email FROM customers WHERE customer_name=?'
        params = (name,)
        result = database.onselect(query,params)
        if not result == []:
            return result
        else:
            return None

    def getid(self,mobile):
        query = 'SELECT id FROM customers WHERE mobile=?'
        params = (mobile,)
        result = database.onselect(query,params)
        if not result == []:
            return result[0][0]
        else:
            return None

    def update(self,data):
        query = "UPDATE customers SET customer_name=?,email=? WHERE id=?"
        params = (data[1],data[2],data[0])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None

    def updates(self,data):
        query = "UPDATE customers SET customer_name=?,mobile=?,email=? WHERE id=?"
        params = (data[1],data[2],data[3],data[0])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None