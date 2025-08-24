import os
import yagmail
import requests 
import tkinter as tk
from tkinter import messagebox
from model.Customer import Customer
from controller.JsonController import JsonController
from model.Shop import Shop

class SmsController:
    def __init__(self):
        pass
        
    def checkNet(self):
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
        
    def sendBillMail(self):
        # jmdr sekk dhpq vouz
        customerName = self.customer_name_entry.get()
        mailAddress  = self.email_address_entry.get()
        net          = SmsController.checkNet(self)
        if not customerName or not mailAddress:
            messagebox.showerror("Error", "Invalid customer name or email address ! ")
        elif net is not True:
            messagebox.showwarning("No Internet","Chack your internet connection!")
        else :
            shop    = Shop.onselect(self)
            invoice = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\report\\invoice.pdf")
            subject = ('Invoice from '+str(shop[0]))
            message = ('''\
                        <html>
                        <body>
                            <h2 style="padding:0;margin:0;" >Dear '''+str(customerName)+'''</h2>
                            <p>Thank you for choosing <u>'''+str(shop[0])+'''</u>.<br>Please find attached the invoice for your recent transaction.We kindly request you to review the invoice and make the payment by the due date mentioned above.
                            If you have any questions regarding this invoice, please feel free to contact us at <b>'''+str(shop[2])+'''</b>.</p>
                            <h3 style="padding:0;margin:0;">Best Regards</h3>,
                            <p style="padding:0;margin:0;"><b>Manager</b><br>'''+str(shop[0])+'''<br>'''+str(shop[1])+'''</p>
                        </body>
                        </html>
                        ''')
            
            userMail = JsonController.getJson(self,'userMail')
            userPass = JsonController.getJson(self,'userPass')
            if not userMail or not userPass:
                messagebox.showerror("Error", "Invalid your gmail configuration setting!")
            else:
                mailbox = yagmail.SMTP(
                    user = userMail, 
                    password = userPass
                )
                mailbox.send(
                    to=mailAddress, 
                    subject=subject,
                    contents=message,
                    attachments=invoice
                    ) 
                messagebox.showinfo("Success", "Email sent successfully.")
                
                
    def sendSMS(self,number,sms):
        
        greenweburl = "https://api.bdbulksms.net/api.php"
        # token = "90711209121675836552c51ffb7a986bde0f360da57de5712f09"
        greenwebtoken = JsonController.getJson(self,'greenwebToken')

        to = number

        data = {
                'token':greenwebtoken, 
                'to':number, 
                'message':sms
                } 
        
        responses = requests.post(url = greenweburl, data = data) 
        return responses

    def shopingsms(self):
        mobile = self.mobile_number_entry.get()
        if mobile=='':
            messagebox.showerror("Error", "Customer mobile number empty!")
        elif mobile is not None:
            user = Customer.chack(self,mobile)
            if user is None:
                messagebox.showinfo("Error", "Customer not found at this number!")
        else:
            sms = 'Dear Rafiq Talukder, you purchased a total of 1000 taka of products from my shop, discount 100 taka, paid 700 taka. The current outstanding amount is 200 taka.'
            text = SmsController.sendSMS(self,'+88'+mobile,sms)
            messagebox.showinfo("Info", text)
            
