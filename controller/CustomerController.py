import os
from tkinter import messagebox
import tkinter as tk
import webbrowser
from datetime import date
from xhtml2pdf import pisa
from model.Customer import Customer
from model.Shop import Shop

class CustomerController:
    def __init__(self):
        super().__init__()

    def createCustomer(self):
        name   = self.cName.get()
        mobile = self.cMobile.get()
        email  = self.cEmail.get()
        if name == "":
            messagebox.showerror("Error", "Please enter customer's name")
        elif mobile == "":
            messagebox.showerror("Error", "Please enter customer's mobile number")
        else:
            if Customer.chack(self,mobile) :
                messagebox.showerror("Error", "Customer already exists.")
            else:
                if Customer.create(self,[name,mobile,email]):
                    messagebox.showinfo("Success", "Customer informetion saved successfully.")
                    CustomerController.clearData(self)
                    CustomerController.customerShow(self)

                else:messagebox.showerror("Error", "Something is wrong please try again.")

    def updateCustomer(self):
        id     = self.cID.get()
        name   = self.cName.get()
        mobile = self.cMobile.get()
        email  = self.cEmail.get()
        if name == "":
            messagebox.showerror("Error", "Please enter customer's name")
        elif mobile == "":
            messagebox.showerror("Error", "Please enter customer's mobile number")
        else:
            if Customer.chack(self,mobile) :
                Customer.update(self, [id, name, email])
                messagebox.showinfo("Success", "Informetion update successfully.")
                CustomerController.clearData(self)
                CustomerController.customerShow(self)
            else:
                if Customer.updates(self,[id,name,mobile,email]):
                    messagebox.showinfo("Success", "Informetion update successfully.")
                    CustomerController.clearData(self)
                    CustomerController.customerShow(self)
                else:
                    messagebox.showerror("Error", "Something is wrong please try again.")

    def print(self):
        shop = Shop().onselect()
        plist = Customer.all(self)
        if shop:
            if plist:
                trlist = ""
                for list in plist:
                    tr = '''<tr style="padding:1px; border:0.01px solid #ddd;">
                            <td style="width:60px;">''' + str(list[0]) + '''</td>
                            <td>''' + str(list[1]) + '''</td>
                            <td>''' + str(list[2]) + '''</td>
                            <td> ''' + str(list[3]) + ''' </td>
                        </tr>'''
                    trlist = str(trlist) + str(tr)

                html = '''<!DOCTYPE html>
                        <html lang="en">  
                        <meta charset="utf-8">
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <meta name="description" content="">
                        <meta name="author" content="">
                        <style>td{padding-left:3px;padding-top:3px;}</style>


                        <h4 style="text-align:center; padding:0;margin:0;">''' + str(shop[0]) + '''</h4>
                        <p style="text-align:center; padding:0;margin:0;">''' + str(shop[1]) + '''</p>
                        <p style="text-align:center; padding:0;margin:0;">Mobile : ''' + str(shop[2]) + ''' </p>
                        <h1 style="text-align:center; font-size:1.2 rem;">CUSTOMER LIST</h1>
                        <span> Date : ''' + str(date.today()) + '''</span>
                        <table>
                            <thead>
                                <tr style="padding:2px; border:0.01px solid #ddd;">
                                    <td><strong>No</strong></td>
                                    <td><strong>Name</strong></td>
                                    <td><strong>Mobile Number</strong></td>
                                    <td><strong>Email Address</strong></td>
                                </tr>
                            </thead>
                            <tbody>''' + str(trlist) + '''</tbody>
                        </table>
                    </html>
                '''
                pdf_path = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\customer.pdf")

                with open(pdf_path, "wb") as pdf_file:
                    pisa_status = pisa.CreatePDF(html, dest=pdf_file)
                    webbrowser.open_new(pdf_path)
                return not pisa_status.err

    def customerShow(self):
        lists = Customer.all(self)
        if lists:
            self.tree.delete(*self.tree.get_children())
            for list in lists:
                self.tree.insert("", 'end', text="L1", values=list)

    def clearData(self):
        self.cID.set('')
        self.cName.set("")
        self.cMobile.set("")
        self.cEmail.set("")
