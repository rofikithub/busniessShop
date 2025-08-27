import os
import json
import tkinter as tk
from tkinter import messagebox

class JsonController:
    def __init__(self):
        pass
    def getPath(self):
        home_directory = os.path.expanduser( '~' )
        db_path = (home_directory+"\\AppData\\Local\\BMS")
        if not os.path.exists(db_path):
            os.mkdir(db_path)
        path=(home_directory+"\\AppData\\Local\\BMS\\system.json")
        
        if not os.path.exists(path):
            default_data = {
                "backgroundColor": "#eeeeee",
                "textColor": "Black",
                "userMail": "",
                "userPass": "",
                "greenwebToken": ""
            }
            with open(path, "w", encoding="utf-8") as f:
                json.dump(default_data, f, indent=5, ensure_ascii=False)
                
        return path
        
        
    def updateJson(self,name,velue,index):
            with open(JsonController.getPath(self), "r") as file:
                data = json.load(file)
                data[name]= velue
            with open(JsonController.getPath(self), "w") as file:
                json.dump(data, file, indent=index)

    def updateConfiguration(self):
        mail = self.usermail_entry.get()
        pasw = self.mailPass_entry.get()
        with open(JsonController.getPath(self), "r") as file:
            data = json.load(file)
            data['userMail']= mail
            data['userPass']= pasw
        JsonController.updateJson(self,'userMail',mail,2)
        JsonController.updateJson(self,'userPass',pasw,3)
        messagebox.showinfo("Success", " Successfully update gmail configaration.")     
                
                
    def getJson(self,name):
        with open(JsonController.getPath(self), "r") as file:
            jsondata = json.load(file)
            data = jsondata[name]
        if data is not None:
            return data
        else:
            return None
        
    def bgColor(self): 
        with open(JsonController.getPath(self), "r") as file:
            data = json.load(file)
            return data['backgroundColor']
        
    def fgColor(self):
        bg = JsonController.bgColor(self)
        if bg=="Black" or bg=="Green" or bg=="Red":
            JsonController.updateJson(self,"textColor","White",1)
        else:
            JsonController.updateJson(self,"textColor","Black",1)
        with open(JsonController.getPath(self), "r") as file:
            data = json.load(file)
            return data['textColor']
        
    def updateToken(self):
        token = self.token_entry.get()
        JsonController.updateJson(self,'greenwebToken',token,3)
        messagebox.showinfo("Success", " Successfully update api Token.")
            