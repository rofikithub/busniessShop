import os
import time
from pyzbar.pyzbar import decode
import cv2
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from num2words import num2words
import playsound        # pip install --upgrade setuptools wheel  # pip install playsound
from gtts import gTTS
import requests   # pip install gTTS

from controller.ProductController import ProductController
from model.Category import Category
from model.Card import Card
from model.Product import Product
from model.Shop import Shop


class CardController:
    def __init__(self):
        super().__init__()

    def getQuntaty(self):
        for name, entry in self.entries.items():
            if entry.get()!="":
                price = Product.price(name)
                values = [name, price, entry.get()]
                if (Card.chack(self,name)):
                    if ProductController.chackQun(self, [name, entry.get()]):
                        if (Card.update(self,values)):
                            self.cardTotal.set(Card.total(self))
                            self.paid.set(Card.total(self))
                else:
                    if ProductController.chackQun(self, [name, entry.get()]):
                        if (Card.create(self,values)):
                            self.cardTotal.set(Card.total(self))
                            self.paid.set(Card.total(self))
        CardController.cardBox(self)
        self.profit.set(Card.profit(self))
        messagebox.showinfo("Success", "This list Successfully added to card")

    def addToCard(self):
        name = self.product_name_entry1.get()
        qunt = self.quntaty_entry1.get()
        price = Product.price(name)
        values = [name,price,qunt]

        if(Card.chack(self,name)):
            if ProductController.chackQun(self, [name, qunt]):
                if(Card.update(self,values)):
                    self.cardTotal.set(Card.total(self))
                    self.paid.set(Card.total(self))
                    messagebox.showinfo("Update", "Successfully update quantity of "+name)
        else:
            if ProductController.chackQun(self,[name,qunt]):
                if(Card.create(self,values)):
                    self.cardTotal.set(Card.total(self))
                    self.paid.set(Card.total(self))
                    messagebox.showinfo("Success", name+" Successfully added to card")

        CardController.cardBox(self)
        self.profit.set(Card.profit(self))

    def scanToCard(self):
        qunt   = '1'
        name   = Product.pname(self.code)
        price  = Product.price(name)
        values = [name,price,qunt]

        if(Card.chack(self,name)):
            if ProductController.chackQun(self, [name, qunt]):
                if(Card.update(self,values)):
                    self.cardTotal.set(Card.total(self))
                    self.paid.set(Card.total(self))
                    # messagebox.showinfo("Update", "Successfully update quantity of "+name)
                    # playsound.playsound(os.path.abspath("scan.mp3"), True)
        else:
            if ProductController.chackQun(self,[name,qunt]):
                if(Card.create(self,values)):
                    self.cardTotal.set(Card.total(self))
                    self.paid.set(Card.total(self))
                    # messagebox.showinfo("Success", name+" Successfully added to card")
                    # playsound.playsound(os.path.abspath("scan.mp3"), True)

        CardController.cardBox(self)
        self.profit.set(Card.profit(self))
        return True

    def camera(self):
        if self.camera_image["toggle"]:
            
            self.camera_frame_btn.config(image=self.cm_of)
            self.camera_frame_btn.image = self.cm_of
            
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                decoded_objects = decode(frame)
                for obj in decoded_objects:
                    self.code = obj.data.decode("utf-8")
                    if CardController.scanToCard(self):
                        playsound.playsound(os.path.abspath("scan.mp3"), True)
                        cv2.putText(frame, self.code, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        break
                cv2.imshow("QR Code Scanner", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        else:
            self.camera_frame_btn.config(image=self.cm_on)
            self.camera_frame_btn.image = self.cm_on
            
        self.camera_image["toggle"] = not self.camera_image["toggle"]


    def refreshCard(self):
        ans = messagebox.askokcancel("Confirm", "Are you sure to refresh card?")
        if ans == True:
            shop = Shop().onselect()
            sms = Card.delete(self)
            if(sms==True):
                self.cardTotal.set(Card.total(self))
                self.paid.set(self.cardTotal.get())
                self.profit.set(Card.profit(self))
                self.bill_box.delete('1.0', tk.END)
                self.bill_box.insert(tk.END, str(shop[0])+'\n',"center")
                self.bill_box.insert(tk.END, str(shop[1])+'\n', "center")
                self.bill_box.insert(tk.END, 'Mobile : - '+str(shop[2])+'\n', "center")
                messagebox.showinfo("Success", " Successfully refresh your card")


    def cardCalculate(self):
        total  = self.cardTotal.get()
        less   = self.less.get()
        due    = int(self.due.get())
        paid   = self.paid.get()
        profit = self.profit.get()

        if less > 0:
            if less>profit:
                messagebox.showerror("Error", 'You can give maximum discount '+str(profit))
                self.less.set(profit)
                self.paid.set(total - profit - due)
            else:
                self.paid.set(total-less-due)

        if due > 0:
            self.paid.set(total-less-due)

        CardController.cardBox(self)


    def cardBox(self):
        shop = Shop().onselect()
        list = Card.all(self)

        if shop:
            if list:

                self.bill_box.delete('1.0', tk.END)
                self.bill_box.insert(tk.END, str(shop[0])+'\n',"center")
                self.bill_box.insert(tk.END, str(shop[1])+'\n', "center")
                self.bill_box.insert(tk.END, 'Mobile : - '+str(shop[2])+'\n', "center")

                self.bill_box.insert(tk.END, '\n---------------------------------------------  SHOPPING CARD :    --------------------------------')
                self.bill_box.insert(tk.END, '\nCustomer Name :  '+str(self.name.get())+'')
                self.bill_box.insert(tk.END, '\nMobile Number :    '+str(self.mobile.get())+'')
                self.bill_box.insert(tk.END, "\n-----------------------------------------------------------------------------------------------------------\n")
                self.bill_box.insert (tk.END, "DESCRIPTION  \t\t\t RATE \t QUANTITY \t\t AMOUNT")
                self.bill_box.insert(tk.END, "\n-----------------------------------------------------------------------------------------------------------\n")
                for lists in list:
                    self.bill_box.insert (tk.END, ''+str(lists[1])+'  \t\t\t '+str(lists[2])+' \t '+str(lists[3])+' \t\t '+str(lists[2]*lists[3])+' \n' )
                self.bill_box.insert(tk.END, "\n-----------------------------------------------------------------------------------------------------------\n")
                self.bill_box.insert (tk.END, '\t\t\t\tTOTAL PRICE \t  = \t '+str(self.cardTotal.get())+'\n')
                self.bill_box.insert (tk.END, '\t\t\t\tLess  (-)\t            = \t '+str(self.less.get())+'\n ')
                self.bill_box.insert (tk.END,"\t\t-------------------------------------------------------------------------------\n" )
                self.bill_box.insert (tk.END, '\t\t\t\tNET PAYABLE \t  = \t '+str(self.cardTotal.get()-self.less.get())+'\n' )
                self.bill_box.insert (tk.END, '\t\t\t\tPaid   (-)\t           = \t '+str(self.cardTotal.get()-self.less.get()-self.due.get())+'\n' )
                self.bill_box.insert (tk.END, "\t\t      ---------------------------------------------------------------------------\n" )
                self.bill_box.insert (tk.END, '\t\t\t\tDUE AMOUNT   \t=\t '+str(self.due.get())+'\n ')
    def checkConnection(self):
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

    def cardSpeaker(self):
        ctotal = self.cardTotal.get()
        less   = self.less.get()
        paid   = self.paid.get()
        due    = self.due.get()
        if self.volume_image["toggle"]:
            self.volume_button.config(image=self.au_of)
            self.volume_button.image = self.au_of
            
            list = Card.all(self)
            texts = ''
            if list:
                if CardController.checkConnection(self):
                    for lists in list:
                        texts = '. Product name.'+str(lists[1])+'.  price .  '+num2words(str(lists[2]), lang='en-US')+'.    quantity.   '+num2words(str(lists[3]), lang='en-US')+'. Total Amount.  '+num2words(str(lists[2]*lists[3]), lang='en-US')+'. \n'
                        toSpeak = gTTS(text=texts, lang='en-US', tld='us')
                        file = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\audio.mp3")
                        toSpeak.save(file)
                        playsound.playsound(file, True)
                        os.remove(file)
                        
                    texts = 'Total Price.'+num2words(str(ctotal), lang='en-US')+'.  Total Discount .  '+num2words(str(less), lang='en-US')+'.    Total Payable Amount.   '+num2words(str(paid), lang='en-US')+'. Total Due .  '+num2words(str(due), lang='en-US')+'.  Thanks You.'
                    toSpeak = gTTS(text=texts, lang='en-US', tld='us')
                    file = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\audio.mp3")
                    toSpeak.save(file)
                    playsound.playsound(file, True)
                    os.remove(file)
                else:
                    messagebox.showwarning("Info","Internet connection required!")
        else:
            self.volume_button.config(image=self.au_on)
            self.volume_button.image = self.au_on
            
        self.volume_image["toggle"] = not self.volume_image["toggle"]
        
        