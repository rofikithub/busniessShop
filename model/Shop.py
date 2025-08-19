from controller.ConnectionController import Database
database = Database()

class Shop:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS shops (
                                        id INTEGER PRIMARY KEY,
                                        sname TEXT NOT NULL,
                                        address TEXT NOT NULL,
                                        mobile TEXT NOT NULL
                                    )''')

    def create(self,values):
        query = 'INSERT INTO shops (sname, address, mobile) VALUES (?,?,?)'
        params = (values[0], values[1], values[2])
        result = database.insert(query, params)
        if result > 0:
            return result
        else:
            return None

    def chack(self):
        query = 'SELECT * FROM shops WHERE id=?'
        params = ('1',)
        result = database.onselect(query,params)
        if result:
            return result
        else:
            return None


    def onselect(self):
        list = []
        query = 'SELECT * FROM shops WHERE id=?'
        params = ('1',)
        result = database.onselect(query,params)
        if result:
            for item in result:
                list.append(item[1])
                list.append(item[2])
                list.append(item[3])
        return list



    def update(self,values):
        query = "UPDATE shops SET sname = ?, address = ?, mobile = ? WHERE id = ?"
        params = (values[0],values[1],values[2],'1')
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None