import os, time
import datetime

import webbrowser
import tkinter as tk
from datetime import date
from tkinter import messagebox

from controller.SalesController import SalesController
from model.Sale import Sale
from model.List import List
from model.Product import Product

class ReturnController:
    def __init__(self):
        pass
    
    def showBill(self):
        sid = int(self.sID.get())
        if sid>0:
            bill = Sale.getbill(self,sid)
            if bill:
                self.tree.delete(*self.tree.get_children())
                if bill[6] == 0:
                    status = "Paid"
                elif bill[6] == 1:
                    status = "Due"
                self.tree.insert("", 'end', text="Text", values=[bill[0], bill[9], bill[2], bill[3], bill[4], bill[5], status, bill[7], bill[8]])
                
            plist = List.getList(self,sid)
            self.treel.delete(*self.treel.get_children())
            for plists in plist:
                self.treel.insert("", 'end', text="L1", values=[plists[0],plists[6],plists[4],plists[5],plists[1],sid,plists[3]])
                
    def productReturn(self):
        sid   = self.sID.get()
        lid   = self.voucher.get()
        pid   = self.proID.get()
        price = self.price.get()
        oqun  = self.oldQun.get()
        pqun  = self.proQun.get()
        nqun  = (oqun-pqun)
        self.tkReturn = 0
        
        if not sid:
            messagebox.showerror("Error", 'Please input Bill number!')
        elif not lid:
            messagebox.showerror("Error", 'Please select product to return!')
        elif oqun<=pqun:
            messagebox.showerror("Error", 'Please change quantity to return!')
        else:
            ans = messagebox.askokcancel("Confirm", "Are you sure to return product?")
            if ans == True:
                bill = Sale.getbill(self,sid)
                oldTotal   = bill[2]
                oldLess    = bill[3]
                oldDue     = bill[4]
                oldPaid    = bill[5]
                oldProfit  = bill[7]
                
                newProfit  = int(oldProfit-Product.getProfit(pid)*nqun)
                
                newTotal   = (oldTotal-(price*nqun))
                newLess    = int((oldLess/oldTotal)*newTotal)
                paidAmount = (newTotal-newLess)
                if paidAmount>oldPaid:
                    newDue = (paidAmount-oldPaid)
                    newPaid = oldPaid
                    newStatus = 1
                elif paidAmount==oldPaid:
                    newDue = 0
                    newPaid = paidAmount
                    newStatus = 0
                elif paidAmount<oldPaid:
                    newDue = 0
                    newPaid = paidAmount
                    newStatus = 0
                    self.tkReturn = (oldPaid-paidAmount)
                    
                if self.tkReturn>0:
                    anss = messagebox.askokcancel("Confirm", str(self.tkReturn) +' Taka has to be refunded.')
                    if anss == True:
                        if Sale.updateReturn(self,[newTotal,newLess,newDue,newPaid,newStatus,newProfit,sid]):
                            if List.updateReturn(pqun,lid):
                                total = (Product.getQun(self,pid)+nqun)
                                if Product.updateQun(self,[pid,total]):
                                    ReturnController.showBill(self)
                                    
                                    messagebox.showinfo("Success", "Product return successfully.")
                else:
                    if Sale.updateReturn(self,[newTotal,newLess,newDue,newPaid,newStatus,newProfit,sid]):
                        if List.updateReturn(pqun,lid):
                            total = (Product.getQun(self,pid)+nqun)
                            if Product.updateQun(self,[pid,total]):
                                ReturnController.showBill(self)
                                messagebox.showinfo("Success", "Product return successfully.")
                
                