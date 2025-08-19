import os
from tkinter import messagebox
import webbrowser
import qrcode
from datetime import date

from PIL.ImImagePlugin import number
from xhtml2pdf import pisa

from model.Dealer import Dealer
from model.Purchase import Purchase
from model.Shop import Shop


class PurchaseController:
    def __init__(self):
        pass
    def createPurchase(self):
        did      = self.did.get()
        voucher  = self.voucher.get()
        purchase = int(self.purchase.get())
        payment  = int(self.payment.get())
        newDue   = int(self.newDue.get())
        previous = int(self.previous.get())
        totalDue = int(self.totalDue.get())
        created  = date.today()

        if voucher=="":
            voucher=created

        if did == "":
            messagebox.showwarning("Error", "Please select a company name ! ")
        elif payment == 0 & totalDue == 0:
            messagebox.showwarning("Error", "Something is wrong please try again !")
        else:
            if Purchase.chack(self,[did,voucher]):
                messagebox.showerror("Error", "Voucher already exists.")
            else:
                nDue = (purchase-payment)
                if nDue < 0:
                    nDue = 0
                    tDUe = (previous - payment)
                else:
                    tDUe = (previous+nDue)
                if Purchase.create(self, [did,voucher,purchase,payment,nDue,previous,tDUe,created]):
                    messagebox.showinfo("Success", "Voucher saved successfully.")
                    PurchaseController.clearData(self)
                    PurchaseController.purchaseShow(self,did)

    def getprevious(self,name):
        did = Dealer.getid(self,name)
        if did > 0:
            self.previous.set('0')
            self.previous.set(Purchase.getdue(self,did))

    def purchaseCalculate(self):
        purchase = int(self.purchase.get())
        payment  = int(self.payment.get())
        newDue   = int(self.newDue.get())
        previous = int(self.previous.get())
        totalDue = int(self.totalDue.get())

        if not payment>=0:
            messagebox.showerror("Error", "Something is wrong please try again !")
        else:
            nDue = (purchase - payment)
            if nDue<0:
                tDUe = (previous + nDue)
                nDue=0
                self.newDue.set(nDue)
                self.totalDue.set(tDUe)
            else:
                self.newDue.set(nDue)
                tDUe = (previous + nDue)
                self.totalDue.set(tDUe)



    def updatePurchase(self):
        pid      = self.pid.get()
        did      = self.did.get()
        voucher  = self.voucher.get()
        purchase = int(self.purchase.get())
        payment  = int(self.payment.get())
        newDue   = int(self.newDue.get())
        previous = int(self.previous.get())
        totalDue = int(self.totalDue.get())
        if pid == '':
            messagebox.showerror("Error", "Something is wrong please try again.")
        elif did == "":
            messagebox.showwarning("Error", "Please select a company name ! ")
        elif payment == 0 & totalDue == 0:
            messagebox.showwarning("Error", "Something is wrong please try again !")
        else:
            Purchase.update(self, [voucher,purchase,payment,newDue,previous,totalDue, pid])
            messagebox.showinfo("Success", "Purchase updated successfully.")
            PurchaseController.clearData(self)
            PurchaseController.purchaseShow(self,did)

    def print(self):
        shop    = Shop().onselect()
        did     = self.did.get()
        plist   = Purchase.all(self,did)
        company = Dealer.company(self,did)
        if shop:
            if plist:
                trlist = ""
                purchase = 0
                payment  = 0
                newDue   = 0
                no   = 1
                for list in plist:
                    tr = '''<tr style="padding:1px; border:0.01px solid #ddd;">
                            <td style="width:60px;">''' + str(no) + '''</td>
                            <td>''' + str(list[8]) + '''</td>
                            <td>''' + str(list[2]) + '''</td>
                            <td>''' + str(list[3]) + '''</td>
                            <td>''' + str(list[4]) + '''</td>
                            <td>''' + str(list[5]) + '''</td>
                            <td>''' + str(list[6]) + '''</td>
                            <td>''' + str(list[7]) + '''</td>
                        </tr>'''
                    no +=no
                    purchase += list[3]
                    payment  += (list[4])
                    newDue   += (list[5])
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
                        <h1 style="text-align:center; font-size:1.2 rem;">PURCHASE LIST</h1>
                        <span> Company : ''' + str(company[1]) + '''</span></br>
                        <span> SR Name : ''' + str(company[3]) + '''</span></br>
                        <span> Number : ''' + str(company[2]) + '''</span></br>
                        <span> Print Date : ''' + str(date.today()) + '''</span>
                        <table>
                            <thead>
                                <tr style="padding:2px; border:0.01px solid #ddd;">
                                    <td><strong>No</strong></td>
                                    <td><strong>Date</strong></td>
                                    <td><strong>Voucher</strong></td>
                                    <td><strong>Purchase</strong></td>
                                    <td><strong>Payment</strong></td>
                                    <td><strong>New Due</strong></td>
                                    <td><strong>Previous Due</strong></td>
                                    <td><strong>Total Due</strong></td>
                                </tr>
                            </thead>
                            <tbody>''' + str(trlist) + ''' 
                                <tr style="padding:2px; border:0.01px solid #ddd;">
                                    <td colspan=3  style="text-align:center;"><strong>Total</strong></td>
                                    <td><strong>''' + str(purchase) + '''</strong></td>
                                    <td colspan=3><strong>''' + str(payment) + '''</strong></td>
                                    <td ><strong>''' + str(purchase-payment) + '''</strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </html>
                '''
                pdf_path = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\purchase.pdf")

                with open(pdf_path, "wb") as pdf_file:
                    pisa_status = pisa.CreatePDF(html, dest=pdf_file)
                    webbrowser.open_new(pdf_path)
                return not pisa_status.err

    def purchaseShow(self,did):
        lists = Purchase.all(self,did)
        if lists:
            self.treep.delete(*self.treep.get_children())
            no = 1
            for list in lists:
                row = [no,list[8],list[2],list[3],list[4],list[5],list[6],list[7],list[1],list[0]]
                no+=no
                self.treep.insert("", 'end', text="L1", values=row)

    def clearData(self):
        self.pid.set(0)
        self.voucher.set("")
        self.purchase.set('0')
        self.payment.set('0')
        self.newDue.set('0')
        self.previous.set('0')
        self.totalDue.set('0')

    def deletePurchase(self):
        id = self.pid.get()
        if id > 0:
            ans = messagebox.askokcancel("Confirm", "Are you sure to delete voucher?")
            if ans == True:
                if Purchase.delete(self,id):
                    PurchaseController.purchaseShow(self, self.did.get())
                    messagebox.showinfo("Confirmation", "Voucher has been deleted")
        else:
            messagebox.showwarning("Warning", "Please select a voucher ! ")
