import os
from tkinter import messagebox
import webbrowser
import qrcode
from datetime import date

from PIL.ImImagePlugin import number
from xhtml2pdf import pisa
from model.Product import Product
from model.Shop import Shop


class ProductController:
    def __init__(self):
        pass

    def createProduct(self):
        name     = self.proName.get()
        category = self.catName.get()
        quantity = self.proQun.get()
        sprice   = self.sPrice.get()
        cprice   = self.cPrice.get()

        if name == "":
            messagebox.showwarning("Error", "Please enter a product name ! ")
        elif category == "":
            messagebox.showwarning("Error", "Please enter a product category ! ")
        elif quantity == "":
            messagebox.showwarning("Error", "Please enter a product quantity ! ")
        elif sprice == "":
            messagebox.showwarning("Error", "Please enter a product selling price ! ")
        elif cprice == "":
            messagebox.showwarning("Error", "Please enter a product cost price ! ")
        else:
            chack = Product.chack(name)
            if chack:
                messagebox.showerror("Error", "Product already exists.")
            else:
                if Product.create(self,[name,category,quantity,sprice,cprice]):
                    messagebox.showinfo("Success", "Product saved successfully.")
                    ProductController.clearData(self)
                    ProductController.productShow(self)



    def update(self):
        id       = self.proID.get()
        name     = self.proName.get()
        category = self.catName.get()
        quantity = self.proQun.get()
        sprice   = self.sPrice.get()
        cprice   = self.cPrice.get()

        if id =='':
            messagebox.showerror("Error", "Something is wrong please try again.")
        elif name == "":
            messagebox.showwarning("Error", "Please enter a product name ! ")
        elif category == "":
            messagebox.showwarning("Error", "Please enter a product category ! ")
        elif quantity == "":
            messagebox.showwarning("Error", "Please enter a product quantity ! ")
        elif sprice == "":
            messagebox.showwarning("Error", "Please enter a product selling price ! ")
        elif cprice == "":
            messagebox.showwarning("Error", "Please enter a product cost price ! ")
        else:
            if Product.chack(name):
                Product.update(self, [id, category, quantity, sprice, cprice])
                messagebox.showinfo("Success", "Product updated successfully.")
                ProductController.clearData(self)
                ProductController.productShow(self)
            else:
                if Product.updateName(self, [id, name, category, quantity, sprice, cprice]):
                    messagebox.showinfo("Success", "Product updated successfully.")
                    ProductController.clearData(self)
                    ProductController.productShow(self)
                else:
                    messagebox.showerror("Error", "Something is wrong please try again.")


    def productShow(self):
        lists = Product.all(self)
        if lists:
            self.tree.delete(*self.tree.get_children())
            for list in lists:
                self.tree.insert("", 'end', text="L1", values=list)

    def print(self):
        shop = Shop().onselect()
        plist = Product.all(self)
        if shop:
            if plist:
                trlist = ""
                qun  = 0
                sall = 0
                cost = 0
                for list in plist:
                    tr = '''<tr style="padding:1px; border:0.01px solid #ddd;">
                            <td style="width:60px;">''' + str(list[0]) + '''</td>
                            <td>''' + str(list[1]) + '''</td>
                            <td>''' + str(list[2]) + '''</td>
                            <td>''' + str(list[3]) + '''</td>
                            <td>''' + str(list[4]) + '''</td>
                            <td>''' + str(list[3]*list[4]) + '''</td>
                            <td>''' + str(list[5]) + '''</td>
                            <td>''' + str(list[3]*list[5]) + '''</td>
                        </tr>'''
                    qun  += list[3]
                    sall += (list[3]*list[4])
                    cost += (list[3]*list[5])
                    trlist = str(trlist) + str(tr)

                html = '''<!DOCTYPE html>
                        <html lang="en">  
                        <meta charset="utf-8">
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <meta name="description" content="">
                        <meta name="author" content="">
                        <style>td{padding-left:3px;padding-top:3px;}</style>
        
                        <h4 style="text-align:center; padding:0;margin:0;">'''+ str(shop[0])+'''</h4>
                        <p style="text-align:center; padding:0;margin:0;">'''+ str(shop[1])+'''</p>
                        <p style="text-align:center; padding:0;margin:0;">Mobile : '''+ str(shop[2])+''' </p>
                        <h1 style="text-align:center; font-size:1.2 rem;">PRODUCT LIST</h1>
                        <span> Date : '''+str(date.today())+'''</span>
                        <table>
                            <thead>
                                <tr style="padding:2px; border:0.01px solid #ddd;">
                                    <td><strong>No</strong></td>
                                    <td><strong>Name</strong></td>
                                    <td><strong>Category</strong></td>
                                    <td><strong>Quantity</strong></td>
                                    <td><strong>Sall Price</strong></td>
                                    <td><strong>Total Sall Price</strong></td>
                                    <td><strong>Cost Price</strong></td>
                                    <td><strong>Total Cost Price</strong></td>
                                </tr>
                            </thead>
                            <tbody>'''+str(trlist)+''' 
                                <tr style="padding:2px; border:0.01px solid #ddd;">
                                    <td colspan=3  style="text-align:center;"><strong>Total</strong></td>
                                    <td colspan=2><strong>'''+str(qun)+'''</strong></td>
                                    <td colspan=2><strong>'''+str(sall)+'''</strong></td>
                                    <td><strong>'''+str(cost)+'''</strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </html>
                '''
                pdf_path = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\product.pdf")

                with open(pdf_path, "wb") as pdf_file:
                    pisa_status = pisa.CreatePDF(html, dest=pdf_file)
                    webbrowser.open_new(pdf_path)
                return not pisa_status.err

    def clearData(self):
        self.proID.set('')
        self.proName.set("")
        self.catName.set("")
        self.proQun.set('')
        self.sPrice.set('')
        self.cPrice.set('')

    def chackQun(self,data):
        name  = data[0]
        qun   = int(data[1])
        id  = int(Product.getid(self,name))
        total = int(Product.getQun(self,id))

        if qun>total:
            messagebox.showerror("Error", 'Not enough '+str(name)+' in stock')
            return None
        else:
            return [id,(total-qun)]


    def printqr(self):
        qrpng = os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\qrpng"
        for filename in os.listdir(qrpng):
            if filename.endswith('.png'):
                os.remove(os.path.join(qrpng, filename))

        id = self.proID.get()
        if not id:
            messagebox.showerror("Error", 'Please select a product for QR')
        else:
            name = self.proName.get()
            qun = self.proQun.get()
            for no in range(qun):
                img = qrcode.make(id)
                img.save(qrpng + '\\'+str(id)+'_'+str(no)+'.png')

            images = ""
            for sl in range(1, qun+1):
                br = ""
                if int(repr(sl)[-1])==0:
                    br = '</br>'
                elif int(repr(sl)[-1])==5:
                    br = '</br>'

                url = qrpng + '\\'+str(id)+'_'+str(no)+'.png'
                img = '''<span><img src="'''+str(url)+'''" width="145" height="145">'''+str(br)+'''</span>'''
                images = str(images) + str(img)

            html = '''<!DOCTYPE html>
                    <html lang="en">  
                    <meta charset="utf-8">
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <meta name="description" content="">
                    <meta name="author" content="">
                    <style>span{display: inline-block;} p{padding:0; margin:0;}</style>
                    <body>
                        <p>Product ID : '''+str(id)+'''<p>
                        <p>Product Name : '''+str(name)+'''<p>
                        <p>QR Code Quantity : '''+str(qun)+'''<p></br></br>
                        <div>'''+str(images)+'''</div>
                    </body>
                </html>
            '''
            pdf_qrpath = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\qrcode.pdf")

            with open(pdf_qrpath, "wb") as pdf_file:
                pisa_status = pisa.CreatePDF(html, dest=pdf_file)
                webbrowser.open_new(pdf_qrpath)
            return not pisa_status.err




