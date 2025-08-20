import json
import tkinter as tk
from tkinter import messagebox
from controller.JsonController import JsonController
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
        if info is not None:
            return info

        
    def getDeshboardBackground(self):
        bg = JsonController.bgColor(self)
        # Title Bar
        self.root.configure(background=bg)
        self.topbar_frame.configure(background=bg)
        self.title_frame.configure(background=bg)
        self.label.configure(background=bg)
        self.myshop_name.configure(background=bg)

        # Customer Details
        self.customer_frame.configure(background=bg)
        self.customer_label_frame.configure(background=bg)
        self.billNo_frame.configure(background=bg)
        self.number_frame.configure(background=bg)
        self.name_frame.configure(background=bg)
        self.address_frame.configure(background=bg)
        
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
        self.mail_frame.configure(background=bg)
        self.sms_frame.configure(background=bg)
        self.logout_frame.configure(background=bg)
        
        if bg=='Black' or bg=='Green' or bg=="Red":
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
            self.shop_name.configure(fg='White')
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
            self.shop_name.configure(fg='Black')
            
    def getSettingBackground(self):
        bg = JsonController.bgColor(self)  
        # Shop Details Update
        self.satting_frame.configure(background=bg)
        self.setting_label_frame.configure(background=bg)
        self.name_frame.configure(background=bg)
        self.shop_name_label.configure(background=bg)
        self.address_frame.configure(background=bg)
        self.address_label.configure(background=bg)
        self.number_frame.configure(background=bg)
        self.numbe_label.configure(background=bg)
        self.update_btn_frame.configure(background=bg)
        self.bg_LabelFrame.configure(background=bg)
        self.background_frame.configure(background=bg)
        self.background_label.configure(background=bg)
        self.mail_LabelFrame.configure(background=bg)
        self.mailinfo_frame.configure(background=bg)
        self.mailAdd_frame.configure(background=bg)
        self.usermail_label.configure(background=bg)
        self.mailPass_frame.configure(background=bg)
        self.mailPass_label.configure(background=bg)
        self.mailSave_frame.configure(background=bg)
        self.passNote_frame.configure(background=bg)
        self.passwordApp_label1.configure(background=bg)
        self.passwordApp_label2.configure(background=bg)
        self.passwordApp_label3.configure(background=bg)
        self.sms_LabelFrame.configure(background=bg)
        self.sms_frame.configure(background=bg)
        self.token_frame.configure(background=bg)
        self.token_label.configure(background=bg)
        self.stoken_frame.configure(background=bg)
        self.greenweb_frame.configure(background=bg)
        self.smsnote_label1.configure(background=bg)
        self.smsnote_label2.configure(background=bg)
        self.smsnote_label3.configure(background=bg)
        
        if bg=='Black' or bg=='Green' or bg=="Red":
            self.setting_label_frame.configure(fg='White')
            self.shop_name_label.configure(fg='White')
            self.address_label.configure(fg='White')
            self.numbe_label.configure(fg='White')
            self.bg_LabelFrame.configure(fg='White')
            self.background_label.configure(fg='White')
            self.mail_LabelFrame.configure(fg='White')
            self.usermail_label.configure(fg='White')
            self.mailPass_label.configure(fg='White')
            self.passwordApp_label1.configure(fg='White')
            self.passwordApp_label2.configure(fg='White')
            self.passwordApp_label3.configure(fg='White')
            self.sms_LabelFrame.configure(fg='White')
            self.token_label.configure(fg='White')
            self.smsnote_label1.configure(fg='White')
            self.smsnote_label2.configure(fg='White')
            self.smsnote_label3.configure(fg='White')
        else:
            self.setting_label_frame.configure(fg='Black')
            self.shop_name_label.configure(fg='Black')
            self.address_label.configure(fg='Black')
            self.numbe_label.configure(fg='Black')
            self.bg_LabelFrame.configure(fg='Black')
            self.background_label.configure(fg='Black')
            self.mail_LabelFrame.configure(fg='Black')
            self.usermail_label.configure(fg='Black')
            self.mailPass_label.configure(fg='Black')
            self.passwordApp_label1.configure(fg='Black')
            self.passwordApp_label2.configure(fg='Black')
            self.passwordApp_label3.configure(fg='Black')
            self.sms_LabelFrame.configure(fg='Black')
            self.token_label.configure(fg='Black')
            self.smsnote_label1.configure(fg='Black')
            self.smsnote_label2.configure(fg='Black')
            self.smsnote_label3.configure(fg='Black')
            
