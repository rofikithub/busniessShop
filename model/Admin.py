from controller.ConnectionController import Database
database = Database()

class Admin:
    def __init__(self):
        pass
    def table(self):
        database.crate_table('''CREATE TABLE IF NOT EXISTS admins (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        softwar TEXT NOT NULL,
                                        version TEXT NOT NULL,
                                        start DATE,
                                        end DATE,
                                        status INTEGER
                                    )''')

    def create(self,values):
        query = 'INSERT INTO admins (name, softwar, version, start, end, status) VALUES (?,?,?,?,?,?)'
        params = (values['name'], values['softwar'], values['version'], values['start'], values['end'], values['status'])
        result = database.insert(query, params)
        if result > 0:
            return result
        else:
            return None



    def onselect(self):
        Admin.table(self)
        list = []
        query = 'SELECT * FROM admins WHERE id=?'
        params = ('1',)
        result = database.onselect(query,params)
        if result:
            for item in result:
                list.append(item[1])
                list.append(item[2])
                list.append(item[3])
                list.append(item[4])
                list.append(item[5])
                list.append(item[6])
        return list



    def update(self,values):
        query = "UPDATE admins SET name=?, softwar=?, version=?, start=?, end=?, status=? WHERE id = ?"
        params = (values['name'], values['softwar'], values['version'], values['start'], values['end'], values['status'],'1')
        result = database.update(query,params)
        if result == True:
            return True
        else:
            return None