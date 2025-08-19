from controller.ConnectionController import Database
database = Database()

class Card:
    def __init__(self):
        self.table()

    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS cards (
                                        id INTEGER PRIMARY KEY,
                                        product_name TEXT NOT NULL,
                                        price INTEGER NOT NULL,
                                        quantity INTEGER NOT NULL
                                    )''')

    def create(self,data):
        query = 'INSERT INTO cards (product_name, price, quantity) VALUES (?,?,?)'
        params = (data[0], data[1], data[2])
        result = database.insert(query, params)
        if not result == []:
            return result
        else:
            return None

    def all(self):
        query = ("SELECT * FROM cards")
        result = database.select(query)
        if not result == []:
            return result
        else:
            return None
        
    def chack(self,name):
        Card.table(self)
        query = 'SELECT * FROM cards WHERE product_name=?'
        params = (name,)
        result = database.onselect(query,params)
        if not result == []:
            return result
        else:
            return None

    def update(self,data):
        query = "UPDATE cards SET quantity = ? WHERE product_name = ?"
        params = (data[2],data[0])
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None

    def delete(self):
        query = "DELETE FROM cards"
        result = database.delete(query)
        if result == True:
            return True
        else:
            return None

    def total(self):
        query = ("SELECT c.*,p.sall_price FROM cards as c, products as p WHERE p.product_name = c.product_name")
        result = database.select(query)
        if not result == []:
            total = 0
            for row in result:
                total += row[2]*row[3]
            return total
        else:
            return 0

    def profit(self):
        query = ("SELECT c.*,p.cost_price FROM cards as c, products as p WHERE p.product_name = c.product_name")
        result = database.select(query)
        if not result == []:
            total = 0
            cost  = 0
            for row in result:
                total  += row[2]*row[3]
                cost   += row[3]*row[4]
            return (total - cost)
        else:
            return 0


