import json
from tkinter import messagebox

class JsonController:
    def __init__(self):
        pass

    def updateJson(self,name,velue,index):
            with open("./system.json", "r") as file:
                data = json.load(file)
                data[name]= velue
            with open("./system.json", "w") as file:
                json.dump(data, file, indent=index)

    def updateConfiguration(self):
        mail = self.usermail_entry.get()
        pasw = self.mailPass_entry.get()
        with open("./system.json", "r") as file:
            data = json.load(file)
            data['userMail']= mail
            data['userPass']= pasw
        JsonController.updateJson(self,'userMail',mail,2)
        JsonController.updateJson(self,'userPass',pasw,3)
        messagebox.showinfo("Success", " Successfully update gmail configaration.")     
                
                
    def getJson(self,name):
        with open("./system.json", "r") as file:
            jsondata = json.load(file)
            data = jsondata[name]
        if data is not None:
            return data
        else:
            return None
        
    def bgColor(self):
        with open("./system.json", "r") as file:
            data = json.load(file)
            return data['backgroundColor']
        
    def fgColor(self):
        bg = JsonController.bgColor(self)
        if bg=="Black" or bg=="Green" or bg=="Red":
            JsonController.updateJson(self,"textColor","White",1)
        else:
            JsonController.updateJson(self,"textColor","Black",1)
        with open("./system.json", "r") as file:
            data = json.load(file)
            return data['textColor']
        
    def updateToken(self):
        token = self.token_entry.get()
        JsonController.updateJson(self,'greenwebToken',token,3)
        messagebox.showinfo("Success", " Successfully update api Token.")
            