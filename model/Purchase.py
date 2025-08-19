from controller.ConnectionController import Database
database = Database()

class Purchase:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS purchases (
                                        id INTEGER PRIMARY KEY,
                                        did INT NOT NULL,
                                        voucher INTEGER NULL,
                                        purchase INTEGER NOT NULL,
                                        payment INTEGER NOT NULL,
                                        newDue INTEGER NOT NULL,
                                        previous INTEGER NOT NULL,
                                        totalDue INTEGER NOT NULL,
                                        created DATE NOT NULL
                                    )''')

    def create(self,data):
        query = 'INSERT INTO purchases (did, voucher, purchase, payment, newDue,previous,totalDue,created) VALUES (?,?,?,?,?,?,?,?)'
        params = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        result = database.insert(query, params)
        if result:
            return result
        else:
            return None


    def chack(self,data):
        Purchase.table(self)
        query = 'SELECT * FROM purchases WHERE did=? AND voucher=?'
        params = (data[0],data[1])
        result = database.onselect(query, params)
        if result:
            return result
        else:
            return None

    def all(self,did):
        Purchase.table(self)
        query = 'SELECT p.*, d.company FROM purchases as p, dealers as d WHERE d.id = p.did AND p.did = ?'
        params = (did,)
        result = database.onselect(query, params)
        if result:
            return result
        else:
            return None

    def getdue(self,did):
        query = 'SELECT totalDue FROM purchases WHERE did = ? ORDER BY id DESC LIMIT 1'
        params = (did,)
        result = database.onselect(query, params)
        if result:
            return result[0][0]
        else:
            return 0


    def update(self,data):
        query = "UPDATE purchases SET voucher=?,purchase=?,payment=?,newDue=?,previous=?,totalDue=? WHERE id = ?"
        params = (data[0],data[1],data[2],data[3],data[4],data[5],data[6])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None

    def delete(self,id):
        query = 'DELETE FROM purchases WHERE id='+str(id)
        result = database.delete(query)
        if result == True:
            return True
        else:
            return None