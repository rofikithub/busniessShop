import tkinter as tk
from tkinter import messagebox
from model.Shop import Shop


class SettingController:
    def __init__(self):
        pass

    def createShop(self):
        sname   = self.sname.get()
        address = self.address.get()
        mobile  = self.mobile.get()

        if sname == "":
            messagebox.showwarning("Warning", "Please enter your shop name ! ")
        elif address =="":
            messagebox.showwarning("Warning", "Please enter your shop address ! ")
        elif mobile =="":
            messagebox.showwarning("Warning", "Please enter shop number ! ")
        else:
            chack = Shop().chack()
            if not len(chack) == 0:
                if Shop().update([sname,address,mobile]):
                    messagebox.showinfo("Update", "Successfully update shop informetion. ")
            else:
                if Shop().create([sname,address,mobile]) :
                    messagebox.showinfo("Success", "Shop informetion saved successfully.")

    def showUpdate(self):
        info = Shop().onselect()
        self.sname.set(info[0])
        self.address.set(info[1])
        self.mobile.set(info[2])

    def showShop(self):
        info = Shop().onselect()
        if info:
            return info
