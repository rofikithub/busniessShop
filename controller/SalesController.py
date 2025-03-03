import os, time
import datetime
from xhtml2pdf import pisa
import webbrowser
import tkinter as tk
from tkinter import messagebox
from datetime import date

from model.Customer import Customer
from model.Sale import Sale
from model.Shop import Shop

class SalesController:
    def __init__(self):
        pass

    def duePaid(self):
        id     = int(self.sID.get())
        taka   = self.taka.get()
        total  = self.total.get()
        less   = self.less.get()
        due    = self.due.get()
        paid   = self.paid.get()
        status = self.status.get()

        if id>0:
            if status==1:
                if taka==0:
                    messagebox.showwarning("Warning", "Please enter the amount you received.")
                elif taka>due:
                    messagebox.showerror("Error", "Please enter the right amount.")
                elif due>=taka:
                    ans = messagebox.askokcancel("Confirm", 'Are you make sure you get to '+ str(taka)+' ?')
                    if ans==True:
                        if total==(less+paid+taka):
                            data = [(due-taka),(paid+taka),0,id]
                        else:
                            data = [(due-taka),(paid+taka),1,id]

                        if Sale.update(self,data):
                            messagebox.showinfo("Success", "The amount you received is added.")
                            SalesController.clearData(self)
                            SalesController.salesShow(self)
                else:
                    messagebox.showwarning("Warning", "Select a iteam from sales table")
        else:
            messagebox.showwarning("Warning", "Select a iteam from sales table")

    def salesSaearch(self):
        id = self.sID.get()
        lists = Sale.getbill(self,id)
        if lists:
            self.tree.delete(*self.tree.get_children())
            if lists[6] == 0:
                status = "Paid"
            elif lists[6] == 1:
                status = "Due"
            self.total.set(lists[2])
            self.less.set(lists[3])
            self.due.set(lists[4])
            self.paid.set(lists[5])
            self.status.set(lists[6])
            self.tree.insert("", 'end', text="Text", values=[lists[0], lists[9], lists[2], lists[3], lists[4], lists[5], lists[7], status,lists[8]])

    def salesShow(self):
        lists = Sale.getall(self)
        if lists:
            self.tree.delete(*self.tree.get_children())
            for list in lists:
                if list[6] == 0:
                    status = "Paid"
                elif list[6] == 1:
                    status = "Due"
                self.tree.insert("", 'end', text="Text", values=[list[0], list[9], list[2], list[3], list[4], list[5], list[7], status,list[8]])


    def clearData(self):
        self.sID.set('')
        self.cName.set("")
        self.total.set('')
        self.less.set('')
        self.due.set('')
        self.paid.set('')
        self.status.set('')
        self.taka.set('')



    def print(self,status):
        shop = Shop().onselect()
        if status==0:
            plist = Sale.getall(self)
            title = "SALES LIST"
            pdf_path = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\salesList.pdf")

        elif status==1:
            plist = Sale.getdue(self)
            title = "DUE LIST"
            pdf_path = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\dueList.pdf")

        elif status==2:
            fm  = self.from_entry.get()
            to  = self.to_entry.get()
            plist = Sale.fromTo(self,[fm,to])
            if plist:
                title = 'SALES LIST <br>'+str(fm)+' TO '+str(to)
                pdf_path = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\fromTo.pdf")
            else:
                messagebox.showwarning("Warning", "Please select the correct date!")

        if shop:
            if plist:
                trlist = ""
                total = 0
                less  = 0
                due   = 0
                paid  = 0
                profit= 0
                for list in plist:
                    if list[6]==1:
                        stts="Due"
                    elif list[6]==0:
                        stts = "Paid"

                    tr = '''<tr style="padding:1px; border:0.01px solid #ddd;">
                            <td style="width:80px;">''' + str(list[0]) + '''</td>
                            <td style="width:150px;">''' + str(list[9]) + '''</td>
                            <td style="width:75px;">''' + str(list[10]) + '''</td>
                            <td> ''' + str(list[2]) + ''' </td>
                            <td> ''' + str(list[3]) + ''' </td>
                            <td> ''' + str(list[4]) + ''' </td>
                            <td> ''' + str(list[5]) + ''' </td>
                            <td> ''' + str(list[7]) + ''' </td>
                            <td> ''' + str(stts) + ''' </td>
                            <td style="width:65px;"> ''' + str(list[8]) + ''' </td>
                        </tr>'''

                    total  += list[2]
                    less   += list[3]
                    due    += list[4]
                    paid   += list[5]
                    profit += list[6]
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
                        <h1 style="text-align:center; font-size:1.2 rem;">'''+str(title)+'''</h1>
                        <span> Date : ''' + str(date.today()) + '''</span>
                        <table>
                            <thead>
                                <tr style="padding:2px; border:0.01px solid #ddd;">
                                    <td><strong>No</strong></td>
                                    <td><strong>Name</strong></td>
                                    <td><strong>Mobile</strong></td>
                                    <td><strong>Total</strong></td>
                                    <td><strong>Less</strong></td>
                                    <td><strong>Due</strong></td>
                                    <td><strong>Paid</strong></td>
                                    <td><strong>Profit</strong></td>
                                    <td><strong>Status</strong></td>
                                    <td><strong>Date</strong></td>
                                </tr>
                            </thead>
                            <tbody>''' + str(trlist) + ''' 
                                <tr style="padding:2px; border:0.01px solid #ddd;">
                                    <td colspan=3  style="text-align:center;"><strong>Total</strong></td>
                                    <td><strong>'''+str(total)+'''</strong></td>
                                    <td><strong>'''+str(less)+'''</strong></td>
                                    <td><strong>'''+str(due)+'''</strong></td>
                                    <td><strong>'''+str(profit)+'''</strong></td>
                                    <td colspan=3 ><strong>'''+str(paid)+'''</strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </html>
                '''

                with open(pdf_path, "wb") as pdf_file:
                    pisa_status = pisa.CreatePDF(html, dest=pdf_file)
                    webbrowser.open_new(pdf_path)
                return not pisa_status.err