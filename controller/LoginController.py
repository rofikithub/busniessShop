import json
import tkinter as tk
import requests
from view.messageView import messageView
from tkinter import messagebox 
from model.Admin import Admin

class LoginController:
    def __init__(self, mobile, password):
        self.mobile = mobile
        self.password = password
        self.userLogin()


    def checkConnection(self):
        url = "http://www.google.com"
        timeout = 50
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.ConnectionError:
            return False
        except requests.Timeout:
            return False



    def userLogin(self):
        mobile   = self.mobile_entry.get()
        password = self.password_entry.get()
        #link = 'http://127.0.0.1:8000/softwar/login/'+ str(mobile) + '/' + str(password)
        link = 'https://rofikit.com/softwar/login/'+ str(mobile) + '/' + str(password)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive",
            'Content-Type': 'application/json',
        }
        res = requests.get(link, headers=headers)
        data = (res.json())
        return data


    def loginAction(self):
        mobile   = self.mobile_entry.get()
        password = self.password_entry.get()

        if mobile=='':
            messagebox.showwarning("Warning", "Please enter a valid phone number")
        elif password == '':
             messagebox.showwarning("Warning", "Please enter your secure password!")
        else:
            if LoginController.checkConnection(self):
                data = LoginController.userLogin(self)
                if data == []:
                    messagebox.showerror("Error", "Invalid your number or password ! ")
                else:
                    user = Admin.onselect(self)
                    if user==[]:
                        Admin.create(self,data)
                    else:
                        Admin.update(self,data)
                    self.root.destroy()
                    messageView(tk.Tk(), data)
            else:
                user = Admin.onselect(self)
                if user==[]:
                    messagebox.showwarning("Connection Error","Chack your internet connection!")
                else:
                    data = {
                        "name": user[0],
                        "softwar": user[1],
                        "version": user[2],
                        "start": user[3],
                        "end": user[4],
                        "status": str(user[5])
                    }
                    self.root.destroy()
                    messageView(tk.Tk(), data)








