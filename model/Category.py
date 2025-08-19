from controller.ConnectionController import Database

database = Database()


class Category:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS categories (
                                        id INTEGER PRIMARY KEY,
                                        category_name TEXT NOT NULL
                                    )''')

    def create(self,name):
        query = 'INSERT INTO categories (category_name) VALUES (?)'
        params = (name,)
        result = database.insert(query, params)
        if result > 0:
            return result
        else:
            return None

    def all(self):
        query = ("SELECT * FROM categories")
        result = database.select(query)
        if result:
            return result
        else:
            return None

    def chack(self,name):
        Category.table(self)
        query = 'SELECT * FROM categories WHERE category_name=?'
        params = (name,)
        result = database.onselect(query, params)
        if result:
            return result
        else:
            return None

    def list(self):
        list=[]
        rows = self.all()
        if rows:
            for row in rows:
                list.append(row[1])
        return list

    def update(self,values):
        query = "UPDATE categories SET category_name = ? WHERE id = ?"
        params = (values[0],values[1])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None