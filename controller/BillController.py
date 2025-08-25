import os
from xhtml2pdf import pisa
import webbrowser
import tkinter as tk
from fpdf import FPDF
from tkinter import messagebox
from datetime import date

from model.Customer import Customer
from model.Sale import Sale
from model.Card import Card
from model.Product import Product
from model.List import List
from model.Shop import Shop

from controller.ProductController import ProductController
from controller.SettingController import SettingController

class BillController:
    def __init__(self):
        pass
    def createBill(self):
        total    = self.cardTotal.get()
        less     = self.less.get()
        due      = self.due.get()
        paid     = self.paid.get()
        profit   = self.profit.get()-less

        name   = self.name.get()
        mobile = self.mobile.get()
        email  = self.email.get()
        dates  = date.today()

        if paid<=0:
            messagebox.showerror("Error", "Your calculation is wrong !")

        elif due>0:
            if name == "":
                messagebox.showerror("Error", "Please enter customer's name")
            elif mobile == "":
                messagebox.showerror("Error", "Please enter customer's mobile number")
            else:
                cid = Customer().getid(mobile)

                if cid:
                    sid = Sale().create([cid,total,less,due,paid,'1',profit,dates])
                    if sid:
                        cards = Card().all()
                        for card in cards:
                            pid = Product().getid(card[1])
                            List().create([cid,sid,pid,card[2],card[3]])
                            Product.updateQun(self, ProductController.chackQun(self,[card[1],card[3]]))

                        if Card.delete(self):
                            self.clearBill()
                            self.billNo.set(sid)
                            BillController.searchBill(self)
                            messagebox.showinfo("Success", "Bill has been created successfully")
                else:
                    cid = Customer.create(self,[name, mobile, email])
                    if cid:
                        sid = Sale().create([cid, total,less,due,paid,'1',profit,dates])
                        if sid:
                            cards = Card().all()
                            for card in cards:
                                pid = Product().getid(card[1])
                                List().create([cid, sid, pid, card[2],card[3]])
                                Product.updateQun(self, ProductController.chackQun(self, [card[1], card[3]]))

                            if Card.delete(self):
                                self.clearBill()
                                self.billNo.set(sid)
                                BillController.searchBill(self)
                                messagebox.showinfo("Success", "Bill has been created successfully")

        elif due == 0:
            if name == "": name="Null"
            if mobile == "": mobile="Null"
            if email == "": email=""

            cid = Customer().getid(mobile)
            if cid:
                sid = Sale().create([cid,total,less,due,paid,'0',profit,dates])
                if sid:
                    cards = Card().all()
                    for card in cards:
                        pid = Product().getid(card[1])
                        List().create([cid,sid,pid,card[2],card[3]])
                        Product.updateQun(self, ProductController.chackQun(self, [card[1], card[3]]))

                    if Card.delete(self):
                        self.clearBill()
                        self.billNo.set(sid)
                        BillController.searchBill(self)
                        messagebox.showinfo("Success", "Bill has been created successfully")
            else:
                cid = Customer.create(self,[name, mobile, email])
                if cid:
                    sid = Sale().create([cid, total,less , due, paid, '0',profit,dates])
                    if sid:
                        cards = Card().all()
                        for card in cards:
                            pid = Product().getid(card[1])
                            List().create([cid, sid, pid, card[2],card[3]])
                            Product.updateQun(self, ProductController.chackQun(self, [card[1], card[3]]))

                        if Card.delete(self):
                            self.clearBill()
                            self.billNo.set(sid)
                            BillController.searchBill(self)
                            messagebox.showinfo("Success", "Bill has been created successfully")


    def searchName(self):
        mobile = self.mobile_number_entry.get()
        if len(mobile)==11:
            name = Customer().onselect(mobile)
            if not name==[]:
                self.name.set(name[0])
                self.email.set(name[1])
        else:
            self.name.set('')
            self.email.set('')

    def searchBill(self):
        shop = Shop().onselect()
        bill = Sale().getbill(self.billNo.get())
        if bill is not None :
            self.mobile.set(bill[10])
            self.name.set(bill[9])
            self.email.set(bill[11])
            list = List().getList(bill[0])

            if shop:
                if bill:
                    if list:
                        self.bill_box.delete('1.0', tk.END)
                        self.bill_box.insert(tk.END, str(shop[0])+'\n',"center")
                        self.bill_box.insert(tk.END, str(shop[1])+'\n', "center")
                        self.bill_box.insert(tk.END, 'Mobile : - '+str(shop[2])+'\n', "center")

                        self.bill_box.insert(tk.END, '\n---------------------------------------------  BILL NUMBER :  '+str(bill[0])+'  -------------------------------')
                        self.bill_box.insert(tk.END, '\nDate :            '+str(bill[8])+'')
                        self.bill_box.insert(tk.END, '\nCustomer Name :  '+str(bill[9])+'')
                        self.bill_box.insert(tk.END, '\nMobile Number :    '+str(bill[10])+'')
                        self.bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------\n")
                        self.bill_box.insert (tk.END, "DESCRIPTION  \t\t\t RATE \t QUANTITY \t\t AMOUNT")
                        self.bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------\n")
                        for lists in list:
                            pname = Product.pname(lists[3])
                            self.bill_box.insert (tk.END, ''+str(pname)+'  \t\t\t '+str(lists[4])+' \t '+str(lists[5])+' \t\t '+str(lists[4]*lists[5])+' \n' )
                        self.bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------\n")
                        self.bill_box.insert (tk.END, '\t\t\t\tTOTAL PRICE \t  = \t '+str(bill[2])+'\n')
                        self.bill_box.insert (tk.END, '\t\t\t\tLess  (-)\t           = \t '+str(bill[3])+'\n ')
                        self.bill_box.insert (tk.END,"\t\t----------------------------------------------------------------------------\n" )
                        self.bill_box.insert (tk.END, '\t\t\t\tNET PAYABLE \t  = \t '+str(bill[2]-bill[3])+'\n' )
                        self.bill_box.insert (tk.END, '\t\t\t\tPaid   (-)\t            = \t '+str(bill[5])+'\n' )
                        self.bill_box.insert (tk.END, "\t\t      ------------------------------------------------------------------------\n" )
                        self.bill_box.insert (tk.END, '\t\t\t\tDUE AMOUNT   \t=\t '+str(bill[4])+'\n ')
        else:
            messagebox.showwarning("Warning", "Invalid your bill number !")

    def print(self):
        shop = Shop().onselect()
        bill = Sale().getbill(self.billNo.get())
        if bill is not None :
            list = List().getList(bill[0])
            if shop:
                if bill:
                    if list:
                        trlist = ""
                        for lists in list:
                            pname = Product.pname(lists[3])
                            tr = '''<tr>
                                    <td>'''+str(str(pname))+'''</td>
                                    <td class="text-center">'''+str(lists[4])+'''</td>
                                    <td class="text-center">'''+str(lists[5])+'''</td>
                                    <td class="text-right">'''+str(lists[4]*lists[5])+'''</td>
                                </tr>'''
                            trlist = str(trlist)+str(tr)

                            if bill[6]==0:
                                status = "Paid"
                            elif bill[6]==1:
                                status = "Due"

                        html = '''<!DOCTYPE html>
                                <html lang="en">  
                                <meta charset="utf-8">
                                <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <meta name="description" content="">
                                <meta name="author" content="">
                                
                                <h4 style="text-align:center; padding:0;margin:0;">'''+ str(shop[0])+'''</h4>
                                <p style="text-align:center; padding:0;margin:0;">'''+ str(shop[1])+'''</p>
                                <p style="text-align:center; padding:0;margin:0;">Mobile : '''+ str(shop[2])+''' </p>
                                <h1 style="text-align:center; font-size:1.2 rem;">SHOPPING INVOICE</h1>

                                <p style="padding:0;margin:0;"><u>Billing Information</u></p>
                                <table class="info">
                                <tr>
                                    <td style="width:90px;">Customer Name</td>
                                    <td style="width:450px;"> : '''+ str(bill[9])+'''</td>
                                    <td style="width:90px;">Bill Number</td>
                                    <td> : <strong>'''+str(bill[0])+'''</strong></td>
                                </tr>
                                <tr>
                                    <td>Mobile Number</td>
                                    <td> : '''+ str(bill[10])+'''</td>
                                    <td>Balling Date</td>
                                    <td> : '''+str(bill[8])+'''</td>
                                </tr>
                                <tr>
                                    <td>Email Address</td>
                                    <td> : '''+ str(bill[11])+'''</td>
                                    <td>Bill Status</td>
                                    <td> : <strong>'''+str(status)+'''</strong></td>
                                </tr>
                                </table>
                                <br/>
                                <p style="padding:0;margin:0;"><u>Shipping Information</u></p>
                                <table>
                                    <thead>
                                        <tr>
                                            <td><strong>Item</strong></td>
                                            <td class="text-center"><strong>Price</strong></td>
                                            <td class="text-center"><strong>Quantity</strong></td>
                                            <td class="text-right"><strong>Totals</strong></td>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        '''+str(trlist)+'''
                                        <tr style="border-top: 1px solid #ddd; weight:20px" ></tr>
                                        <tr>
                                            <td></td>
                                            <td></td>
                                            <td><strong>Subtotal</strong></td>
                                            <td><strong>'''+str(bill[2])+'''</strong></td>
                                        </tr>
                                        <tr>
                                            <td></td>
                                            <td></td>
                                            <td>Less (-)</td>
                                            <td>'''+str(bill[3])+'''</td>
                                        </tr>
                                        <tr>
                                            <td></td>
                                            <td></td>
                                            <td>Total Amount</td>
                                            <td><strong>'''+str(bill[2]-bill[3])+'''</strong></td>
                                        </tr>
                                        <tr>
                                            <td></td>
                                            <td></td>
                                            <td><strong>Paid</strong> (-)</td>
                                            <td><strong>'''+str(bill[5])+'''</strong></td>
                                        </tr>
                                        <tr>
                                            <td></td>
                                            <td></td>
                                            <td>Due Amount</strong></td>
                                            <td>'''+str(bill[4])+'''</td>
                                        </tr>
                                    </tbody>
                                </table>
                                </html>'''
                        pdf_path = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\invoice.pdf")

                        with open(pdf_path, "wb") as pdf_file:
                            pisa_status = pisa.CreatePDF(html, dest=pdf_file)
                            webbrowser.open_new(pdf_path)
                        return not pisa_status.err
        else:
            messagebox.showwarning("Warning", "Invalid your bill number !")