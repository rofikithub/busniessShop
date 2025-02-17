import os
import time
import cv2
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog as fd
from num2words import num2words
import playsound        # pip install --upgrade setuptools wheel  # pip install playsound
from gtts import gTTS   # pip install gTTS

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

    def refreshCard(self):
        ans = messagebox.askokcancel("Confirm", "Are you sure to refresh card?")
        if ans == True:
            sms = Card.delete(self)
            if(sms==True):
                self.cardTotal.set(Card.total(self))
                self.paid.set(self.cardTotal.get())
                self.profit.set(Card.profit(self))
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
                self.bill_box.insert(tk.END, '\t\t\t'+str(shop[0])+'\n')
                self.bill_box.insert(tk.END, '\t\t\t        '+str(shop[1])+'\n')
                self.bill_box.insert(tk.END, '\t\t\t           Mobile : - '+str(shop[2])+'\n')

                self.bill_box.insert(tk.END, '\n---------------------------------------------  SHOPPING CARD :    -----------------------------------------')
                self.bill_box.insert(tk.END, '\nCustomer Name :  '+str(self.name.get())+'')
                self.bill_box.insert(tk.END, '\nMobile Number :    '+str(self.mobile.get())+'')
                self.bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------------------------\n")
                self.bill_box.insert (tk.END, "DESCRIPTION  \t\t\t RATE \t QUANTITY \t\t AMOUNT")
                self.bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------------------------\n")
                for lists in list:
                    self.bill_box.insert (tk.END, ''+str(lists[1])+'  \t\t\t '+str(lists[2])+' \t '+str(lists[3])+' \t\t '+str(lists[2]*lists[3])+' \n' )
                self.bill_box.insert(tk.END, "\n--------------------------------------------------------------------------------------------------------------------------\n")
                self.bill_box.insert (tk.END, '\t\t\t\tTOTAL PRICE \t  = \t '+str(self.cardTotal.get())+'\n')
                self.bill_box.insert (tk.END, '\t\t\t\tLess  (-)\t            = \t '+str(self.less.get())+'\n ')
                self.bill_box.insert (tk.END,"\t\t------------------------------------------------------------------------------------\n" )
                self.bill_box.insert (tk.END, '\t\t\t\tNET PAYABLE \t  = \t '+str(self.cardTotal.get()-self.less.get())+'\n' )
                self.bill_box.insert (tk.END, '\t\t\t\tPaid   (-)\t           = \t '+str(self.cardTotal.get()-self.less.get()-self.due.get())+'\n' )
                self.bill_box.insert (tk.END, "\t\t      ------------------------------------------------------------------------\n" )
                self.bill_box.insert (tk.END, '\t\t\t\tDUE AMOUNT   \t=\t '+str(self.due.get())+'\n ')

    def camera(self):
        cam = cv2.VideoCapture(0)
        cam.set(5, 640)
        cam.set(6, 480)

        camera = True
        while camera == True:
            ret, frame = cam.read()
            if not ret:
                print("Failed to grab frame")
            cv2.imshow("QR CODE SCANNER", frame)
            cv2.waitKey(1)

    def cardSpeaker(self):
        if self.volume_image["toggle"]:
            self.volume_button.config(image=self.v_on_img)
            self.volume_button.image = self.v_on_img
            
            list = Card.all(self)
            texts = ''
            
            for lists in list:
                    texts = '   '+str(lists[1])+'  price   '+num2words(str(lists[2]), lang='en-US')+'    quantity   '+num2words(str(lists[3]), lang='en-US')+' \n\n\n'
                    toSpeak = gTTS(text=texts, lang='en', tld='us')
                    file = "audio.mp3"
                    toSpeak.save(file)
                    playsound.playsound(file, True)
                    os.remove(file)
        else:
            self.volume_button.config(image=self.v_off_img)
            self.volume_button.image = self.v_off_img
            
        self.volume_image["toggle"] = not self.volume_image["toggle"]
        
        