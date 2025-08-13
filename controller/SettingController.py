import json
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
            if chack:
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
    def updateJsonFile(self,name,velue):
            with open("./system.json", "r") as file:
                data = json.load(file)
                data[name]= velue
            with open("./system.json", "w") as file:
                json.dump(data, file, indent=0)
        
    def getDeshboardBackground(self):
        with open("./system.json", "r") as file:
            data = json.load(file)
            bg = data['backgroundColor']
        # Title Bar
        self.root.configure(background=bg)
        self.topbar_frame.configure(background=bg)
        self.title_frame.configure(background=bg)
        self.label.configure(background=bg)
        self.myshop_name.configure(background=bg)

        # Customer Details
        self.customer_frame.configure(background=bg)
        self.customer_label_frame.configure(background=bg)
        
        # Product and billing Frame
        self.details_frame.configure(background=bg)
        self.details_label_frame.configure(background=bg)
        self.category_frame.configure(background=bg)
        self.category_label.configure(background=bg)
        self.product_frame.configure(background=bg)
        self.product_name_label1.configure(background=bg)
        self.quntaty_frame.configure(background=bg)
        self.quntaty_label1.configure(background=bg)
        self.camera_frame.configure(background=bg)
        self.camera_frame_label.configure(background=bg)
        self.label_frame.configure(background=bg)
        self.name_label_frame.configure(background=bg)
        self.frame_inside_canvas.configure(background=bg)
        self.bill_frame.configure(background=bg)
        self.add_card_frame1.configure(background=bg)
        self.add_card_frame2.configure(background=bg)
        
        # Bill Area
        self.bill_frame.configure(background=bg)
        self.bill_label_frame.configure(background=bg)
        self.bill_box.configure(background=bg)
        self.shop_name.configure(background=bg)
        
        # Footer Options
        self.option_frame.configure(background=bg)
        self.card_label_frame.configure(background=bg)
        self.total_frame.configure(background=bg)
        self.less_frame.configure(background=bg)
        self.due_frame.configure(background=bg)
        self.paid_frame.configure(background=bg)
        self.refresh_frame.configure(background=bg)
        self.volume_frame.configure(background=bg)
        self.save_frame.configure(background=bg)
        self.print_frame.configure(background=bg)
        self.logout_frame.configure(background=bg)
        
        if bg=='Black':
            self.label.configure(fg='White')
            self.myshop_name.configure(fg='White')
            self.customer_label_frame.configure(fg='White')
            self.details_label_frame.configure(fg='White')
            self.category_label.configure(fg='White')
            self.product_name_label1.configure(fg='White')
            self.quntaty_label1.configure(fg='White')
            self.camera_frame_label.configure(fg='White')
            self.label_frame.configure(fg='White')
            self.bill_frame.configure(fg='White')
            self.bill_box.configure(fg='White')
            self.card_label_frame.configure(fg='White')
            self.bill_label_frame.configure(fg='White')
        else:
            self.label.configure(fg='Black')
            self.myshop_name.configure(fg='Black')
            self.customer_label_frame.configure(fg='Black')
            self.details_label_frame.configure(fg='Black')
            self.category_label.configure(fg='Black')
            self.product_name_label1.configure(fg='Black')
            self.quntaty_label1.configure(fg='Black')
            self.camera_frame_label.configure(fg='Black')
            self.label_frame.configure(fg='Black')
            self.bill_frame.configure(fg='Black')
            self.bill_box.configure(fg='Black')
            self.card_label_frame.configure(fg='Black')
            self.bill_label_frame.configure(fg='Black')
            
    def bgColor(self):
        with open("./system.json", "r") as file:
            data = json.load(file)
            return data['backgroundColor']