from controller.ConnectionController import Database

database = Database()


class Dealer:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS dealers (
                                        id INTEGER PRIMARY KEY,
                                        company TEXT NOT NULL,
                                        mobile TEXT NOT NULL,
                                        srname TEXT NOT NULL
                                    )''')

    def create(self,data):
        query = 'INSERT INTO dealers (company,mobile,srname) VALUES (?,?,?)'
        params = (data[0],data[1],data[2])
        result = database.insert(query, params)
        if not result == []:
            return result
        else:
            return None

    def all(self):
        Dealer.table(self)
        query = ("SELECT * FROM dealers")
        result = database.select(query)
        if not result == []:
            return result
        else:
            return None

    def getid(self,name):
        query = 'SELECT id FROM dealers WHERE company=?'
        params = (name,)
        result = database.onselect(query,params)
        if not result == []:
            return result[0][0]
        else:
            return None

    def company(self,id):
        query = 'SELECT * FROM dealers WHERE id=?'
        params = (id,)
        result = database.onselect(query,params)
        if not result == []:
            return result[0]
        else:
            return None

    def chack(self,data):
        Dealer.table(self)
        query = 'SELECT * FROM dealers WHERE company=? OR mobile=?'
        params = (data[0],data[1])
        result = database.onselect(query, params)
        if not result == []:
            return result
        else:
            return None

    def list(self):
        list=[]
        rows = Dealer.all(self)
        if rows:
            for row in rows:
                list.append(row[1])
        return list

    def update(self,data):
        query = "UPDATE dealers SET company = ?, mobile=?, srname=? WHERE id = ?"
        params = (data[0],data[1],data[2],data[3])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None

    def updatesr(self,data):
        query = "UPDATE dealers SET srname=? WHERE id = ?"
        params = (data[0],data[1])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None

    def chackDelete(self,did):
        query = 'SELECT * FROM purchases WHERE did=?'
        params = (did)
        result = database.onselect(query, params)
        if not result == []:
            return result
        else:
            return None


    def delete(self,id):
        query = 'DELETE FROM dealers WHERE id='+str(id)
        result = database.delete(query)
        if result == True:
            return True
        else:
            return None

