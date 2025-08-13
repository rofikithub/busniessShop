import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from PIL import ImageTk,Image
from tkinter import messagebox
import PIL
from tkinter_webcam import webcam
from importlib.metadata import files
from PIL import Image as PIM, ImageTk

from controller.VoiceController import VoiceController
from view.dealerView import dealerView
from view.salesView import salesView
from view.settingView import settingView
from view.categoryView import categoryView
from view.productView import productView
from view.customerView import customerView
from view.returnView import returnView

from controller.CardController import CardController
from controller.BillController import BillController
from controller.SettingController import SettingController

from model.Category import Category
from model.Product import Product
from model.Card import Card



class dashboardView:
    def __init__(self,root):
        # self.attributes('-fullscreen', True)
        self.root = root
        root.title("User Dashboard")
        root.protocol('WM_DELETE_WINDOW', root.quit)
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()-60
        root.geometry(f'{sw}x{sh}+{-10}+{0}')
        root.iconbitmap(r'image/winico.ico')

        self.qun       = tk.IntVar()
        self.cardTotal = tk.IntVar()
        self.less      = tk.IntVar()
        self.due       = tk.IntVar()
        self.paid      = tk.IntVar()
        self.billNo    = tk.IntVar()
        self.profit    = tk.IntVar()

        self.name   = tk.StringVar()
        self.mobile = tk.StringVar()
        self.email  = tk.StringVar()

        self.billDetails = []

        #Card.delete()

        menu_bar = tk.Menu(root)
        menu_bar.add_command(label="Dealer", command=self.viewDealer)
        menu_bar.add_command(label="Product", command=self.viewProduct)
        menu_bar.add_command(label="Category", command=self.viewCategory)
        menu_bar.add_command(label="Customer", command=self.viewCustomer)
        menu_bar.add_command(label="Sales", command=self.viewSales)
        menu_bar.add_command(label="Return", command=self.viewReturn)
        menu_bar.add_command(label="Setting", command=self.setting)
        menu_bar.add_command(label="Help")
        root.config(menu=menu_bar)
        # root.configure(background="#eeeeee")

        # Title Bar
        self.topbar_frame = tk.Frame(root)
        self.topbar_frame.pack(side=TOP, expand = True)
        
        self.logo_frame = tk.Frame(self.topbar_frame)
        self.logo_frame.pack(side=LEFT)
        
        self.title_frame = tk.Frame(self.topbar_frame)
        self.title_frame.pack(side='left')
        
        self.label = tk.Label(self.title_frame, text="Bill Management System", font=("Times New Roman", 20))
        self.label.pack()
        
        self.myshop_name = tk.Label(self.title_frame, text="ESHOP ONLINE MARCATE CENTER", font=("Times New Roman", 8))
        self.myshop_name.pack()
        
        
        
        # self.options_frame = tk.Frame(self.topbar_frame)
        # self.options_frame.pack(side='left')
        # self.screen_frame = tk.Frame(self.options_frame)
        # self.screen_frame.pack(side='right')
        # self.screen_label = tk.Label(self.screen_frame, text="Screen")
        # self.screen_label.pack(side='left')
        self.background = ttk.Combobox(self.title_frame, values=['Default','White', 'Red', 'Black', 'Green','Yellow'], state="readonly", width=17, background='white')
        self.background.pack()
        self.background.set(".. Windows Color ..")
        self.background.bind('<<ComboboxSelected>>', self.thisBackground)  


        # Customer Details
        self.customer_frame = tk.Frame(root, pady=5, padx=20)
        self.customer_frame.pack(fill=tk.BOTH,side='top', expand=True)
        self.customer_label_frame = tk.LabelFrame(self.customer_frame, text="Customer Details", pady=10, padx=10)
        self.customer_label_frame.pack(fill=tk.BOTH, side='left', expand=True)

        bill_number_label = tk.Label(self.customer_label_frame, text="Bill Number:", pady=2, padx=20)
        bill_number_label.pack(side='left')
        self.bill_number_entry = tk.Entry(self.customer_label_frame, textvariable=self.billNo, bd=0.5, width=15, border=0, font=('Ubuntu', 13), highlightthickness=1,highlightbackground = "#ddd")
        self.bill_number_entry.pack(side='left')
        bill_number_search = tk.Button(self.customer_label_frame, command=lambda : BillController.searchBill(self),text="Search", padx=20, bg="#ddd", fg="black", font=("Arial", 9), border=0.5)
        bill_number_search.pack(side='left')

        mobile_number_label = tk.Label(self.customer_label_frame, text="Mobile Number:", pady=2, padx=20)
        mobile_number_label.pack(side='left')
        self.mobile_number_entry = tk.Entry(self.customer_label_frame, textvariable=self.mobile, bd=0.5, width=15, font=('Ubuntu', 13), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.mobile_number_entry.pack(side='left')
        self.mobile.trace("w", lambda name, index, mode, var=self.mobile: BillController.searchName(self))

        customer_name_label = tk.Label(self.customer_label_frame, text="Customer Name", pady=2, padx=20)
        customer_name_label.pack(side='left')
        self.customer_name_entry = tk.Entry(self.customer_label_frame, textvariable=self.name, bd=0.5, width=20, font=('Ubuntu', 13), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.customer_name_entry.pack(side='left')


        email_address_label = tk.Label(self.customer_label_frame, text="Email Address:", pady=2, padx=20)
        email_address_label.pack(side='left')
        self.email_address_entry = tk.Entry(self.customer_label_frame, textvariable=self.email, bd=0.5, width=20, font=('Ubuntu', 13), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.email_address_entry.pack(side='left')
        #self.email_address_entry.insert(0, "rofik@gmail.com")


        # Product and billing Frame
        self.details_frame = tk.Frame(root, pady=5, padx=20)
        self.details_frame.pack(fill=tk.BOTH, side='top', expand=True)

        # Select by category
        self.details_label_frame = tk.LabelFrame(self.details_frame, text="Select product by category", pady=20, padx=20)
        self.details_label_frame.pack(fill=tk.BOTH, side='left', expand=True)


        self.category_frame = tk.Frame(self.details_label_frame)
        self.category_frame.pack(fill=tk.BOTH, side='top' )
        self.category_label = tk.Label(self.category_frame, text="Product Category", padx=20, pady=10)
        self.category_label.pack(side='left')
        self.category_select = ttk.Combobox(self.category_frame, state="readonly",values=Category().list(), width=30)
        self.category_select.pack(side='left')
        self.category_select.bind('<<ComboboxSelected>>', self.thisCategory)

        self.product_frame = tk.Frame(self.details_label_frame)
        self.product_frame.pack(fill=tk.BOTH, side='top' )
        self.product_name_label1 = tk.Label(self.product_frame, text="Product Name     ", padx=20, pady=10)
        self.product_name_label1.pack(side='left')
        self.product_name_entry1 = ttk.Combobox(self.product_frame, state="readonly", values=[], width=30)
        self.product_name_entry1.pack(side='left')
        self.product_name_entry1.bind('<<ComboboxSelected>>', self.defaultQuntaty)

        self.quntaty_frame = tk.Frame(self.details_label_frame)
        self.quntaty_frame.pack(fill=tk.BOTH, side='top' )
        self.quntaty_label1 = tk.Label(self.quntaty_frame, text="Product Quantity  ", padx=20, pady=10)
        self.quntaty_label1.pack(side='left')
        self.quntaty_entry1 = tk.Entry(self.quntaty_frame, textvariable=self.qun, width=22, font=12, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.quntaty_entry1.pack(side='left')


        self.add_card_frame1 = tk.Frame(self.details_label_frame)
        self.add_card_frame1.pack(fill=tk.Y, side='top', pady=20 )
        self.add_to_cart_btn1 = tk.Button(self.add_card_frame1, command=lambda:CardController.addToCard(self), text="Add to card", padx=20, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        self.add_to_cart_btn1.pack(side='bottom')

        cmof_img = Image.open("./image/camera_of.png").resize((30, 20))
        cmon_img = Image.open("./image/camera_on.png").resize((35, 20))
        self.cm_of = ImageTk.PhotoImage(cmof_img)
        self.cm_on = ImageTk.PhotoImage(cmon_img)
        self.camera_image = {"toggle": True}
        self.camera_frame = tk.Frame(self.details_label_frame)
        self.camera_frame.pack(fill=tk.BOTH, side='top', pady=15 )
        self.camera_frame_btn = tk.Button(self.camera_frame, text="Camera", image=self.cm_on, command=lambda:CardController.camera(self), padx=20, cursor='hand2', border=0.1)
        self.camera_frame_btn.pack()
        self.camera_frame_btn.image=self.cm_on
        
        self.camera_frame_label = Label(self.details_label_frame, text="Click camera icon for open and Close for tab - q", font=("Arial", 8))
        self.camera_frame_label.pack(side='bottom')

        # mpof_img = Image.open("./image/microphone_of.png").resize((20, 30))
        # mpon_img = Image.open("./image/microphone_on.png").resize((20, 30))
        # self.mp_of = ImageTk.PhotoImage(mpof_img)
        # self.mp_on = ImageTk.PhotoImage(mpon_img)
        # self.speek_image = {"toggle": True}
        # speek_frame = tk.Frame(self.details_label_frame)
        # speek_frame.pack(fill=tk.BOTH, side='top', pady=15 )
        # self.speek_button = tk.Button(speek_frame, image=self.mp_on, command=lambda:VoiceController.voice(self), cursor='hand2', padx=20, fg="black", font=("Arial", 8), border=0.1)
        # self.speek_button.pack()
        # self.speek_button.image = self.mp_on


        # Select by nane
        self.label_frame = tk.LabelFrame(self.details_frame, text="Select product by name", padx=10, pady=10)
        self.label_frame.pack(fill=tk.BOTH, side='left' )

        self.name_label_frame = tk.Frame(self.label_frame)
        self.name_label_frame.pack(fill=tk.BOTH, side=TOP, expand=True)

        def on_configure(event):
            canvas.configure ( scrollregion=canvas.bbox ( 'all' ) )
        
        canvas = tk.Canvas ( self.name_label_frame)
        canvas.pack ( side="left", fill="both")

        scrollbar = tk.Scrollbar ( self.name_label_frame, orient="vertical", command=canvas.yview, background='red')
        scrollbar.pack ( side="right", fill="y" )

        canvas.configure ( yscrollcommand=scrollbar.set )
        canvas.bind ( '<Configure>', on_configure )

        self.frame_inside_canvas = tk.Frame ( canvas )
        canvas.create_window ( (0, 0), window=self.frame_inside_canvas, anchor='nw' )

        products = Product().all()
        if products :
            self.checkbox_values = []
            self.checkbox_vars = []
            self.entries = {}
            for product in products:
                var = tk.IntVar()
                self.checkbox_vars.append(var)
                self.checkbox_values.append(product[1])
                name_frame = tk.Frame(self.frame_inside_canvas, bg="white")
                name_frame.pack(side='top', fill=tk.BOTH, expand=False)
                product_checkbutton = tk.Checkbutton(name_frame, text=product[1], variable=var, height=1, bg="white")
                product_checkbutton.pack(side='left', anchor=tk.NW, expand=True)
                self.product_name_entry = tk.Entry(name_frame, width=20, border=0, highlightthickness=1,highlightbackground = "#ddd")
                self.product_name_entry.pack(side='left')
                self.entries[product[1]] = self.product_name_entry

        canvas.update_idletasks ()
        # Set the canvas scroll region
        canvas.config ( scrollregion=canvas.bbox ( "all" ) )

        self.add_card_frame2 = tk.Frame(self.label_frame, pady=5)
        self.add_card_frame2.pack(side=TOP, anchor='s')
        self.add_to_cart_btn2 = tk.Button(self.add_card_frame2, command=lambda:CardController.getQuntaty(self), text="Add to card", padx=20, fg="black", font=("Arial", 8), border=0.5)
        self.add_to_cart_btn2.pack()

        # Bill Area
        self.bill_frame = tk.LabelFrame(self.details_frame, text="Bill Area", padx=10, pady=5, width=50, height=50)
        self.bill_frame.pack(fill=tk.BOTH, side='top', expand=True)

        self.bill_box = tk.Text(self.bill_frame, fg="black", font=("Arial", 9))
        self.bill_box.pack(side='left')

        self.bill_box.delete('1.0', tk.END)
        shop = SettingController.showShop(self)
        if shop:
            self.bill_box.insert(tk.END, '\t\t\t'+str(shop[0])+'\n')
            self.bill_box.insert(tk.END, '\t\t\t        '+str(shop[1])+'\n')
            self.bill_box.insert(tk.END, '\t\t\t           Mobile : - '+str(shop[2])+'\n')
        self.billDetails

        # Footer Options
        self.option_frame = tk.Frame(root, pady=5, padx=20)
        self.option_frame.pack(fill=tk.BOTH, expand=True, side='top')

        # Card option
        self.card_label_frame = tk.LabelFrame(self.option_frame, text="Card Options", pady=10, padx=10)
        self.card_label_frame.pack(fill=tk.BOTH, expand=True, side='left')


        self.total_frame = tk.Frame(self.card_label_frame, padx=10)
        self.total_frame.pack(fill=tk.BOTH, side='left')
        total_label = tk.Label(self.total_frame, text="Total", padx=15, pady=2, bg="#999")
        total_label.pack(side='left')
        self.total_entry = tk.Entry(self.total_frame, textvariable=self.cardTotal, width=10, font=13, border=0, highlightthickness=1,highlightbackground = "#ddd", state='readonly')
        self.total_entry.pack(side='left')

        self.less_frame = tk.Frame(self.card_label_frame, padx=10)
        self.less_frame.pack(fill=tk.BOTH, side='left' )
        total_label = tk.Label(self.less_frame, text="Less", padx=10, pady=2, bg="#ddd")
        total_label.pack(side='left')
        self.less_entry = tk.Entry(self.less_frame, textvariable=self.less, width=7, font=5, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.less_entry.pack(side='left')
        self.less.trace("w", lambda name, index, mode, var=IntVar: CardController.cardCalculate(self))

        self.due_frame = tk.Frame(self.card_label_frame, padx=10)
        self.due_frame.pack(fill=tk.BOTH, side='left' )
        total_label = tk.Label(self.due_frame, text="Due", padx=10, pady=2, bg="#ddd")
        total_label.pack(side='left')
        self.due_entry = tk.Entry(self.due_frame, textvariable=self.due, width=7, font=5, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.due_entry.pack(side='left')
        self.due.trace("w", lambda name, index, mode, var=IntVar: CardController.cardCalculate(self))


        self.paid_frame = tk.Frame(self.card_label_frame, padx=10)
        self.paid_frame.pack(fill=tk.BOTH, side='left' )
        total_label = tk.Label(self.paid_frame, text="Paid", padx=10, pady=2, bg="#999")
        total_label.pack(side='left')
        self.total_entry = tk.Entry(self.paid_frame, textvariable=self.paid, width=10, font=13, border=0, highlightthickness=1,highlightbackground = "#ddd", state='readonly')
        self.total_entry.pack(side='left')

        self.refresh_frame = tk.Frame(self.card_label_frame, padx=20 )
        self.refresh_frame.pack(fill=tk.BOTH, side='left')
        add_to_cart_btn1 = tk.Button(self.refresh_frame, command=lambda:CardController.refreshCard(self), text="Refresh Card", padx=20, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn1.pack(side='left')

        auof_img = Image.open("./image/audio_of.png").resize((25, 18))
        auon_img = Image.open("./image/audio_on.png").resize((25, 18))
        self.au_of = ImageTk.PhotoImage(auof_img)
        self.au_on = ImageTk.PhotoImage(auon_img)
        self.volume_image = {"toggle": True}
        self.volume_frame = tk.Frame(self.card_label_frame, padx=3 )
        self.volume_frame.pack(fill=tk.BOTH, side='left')
        self.volume_button = tk.Button(self.volume_frame, image=self.au_on, command=lambda:CardController.cardSpeaker(self), cursor='hand2', padx=20, fg="black", font=("Arial", 8), border=0.1)
        self.volume_button.image = self.au_on
        self.volume_button.pack(side='left')

        # Billing option
        self.bill_label_frame = tk.LabelFrame(self.option_frame, text="Bill Options", pady=10, padx=10)
        self.bill_label_frame.pack(fill=tk.BOTH, expand=True, side='left')


        self.save_frame = tk.Frame(self.bill_label_frame, padx=40)
        self.save_frame.pack(fill=tk.BOTH, side='left' )
        add_to_cart_btn = tk.Button(self.save_frame, text="Save Bill", command=lambda :BillController.createBill(self), padx=20, bg="#A2C579", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn.pack(side='left')

        self.print_frame = tk.Frame(self.bill_label_frame, padx=20)
        self.print_frame.pack(fill=tk.BOTH, side='left' )
        add_to_cart_btn = tk.Button(self.print_frame, text="Print Bill", command=lambda: BillController.print(self), padx=30, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn.pack(side='left')

        self.logout_frame = tk.Frame(self.bill_label_frame, padx=40)
        self.logout_frame.pack(fill=tk.BOTH, side='left' )
        add_to_cart_btn = tk.Button(self.logout_frame, command=lambda : self.logout(), text="Logout", padx=20, bg="#E25E3E", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn.pack(side='left')
        
        
        
        self.shop_name = tk.Label(root, text='© 2025 - Softwar Developed by Md. Rafikul Islam (Rofik), Phone- 01737034338, Email- rofik.it.bd@gmail.com', font=("Times New Roman", 8))
        self.shop_name.pack(side=BOTTOM, anchor='s')
        
        
        SettingController.getDeshboardBackground(self)
                
                


    def viewDealer(self):
        self.root.destroy()
        dealerView(tk.Tk())

    def setting(self):
        self.root.destroy()
        settingView(tk.Tk())


    def viewProduct(self):
        self.root.destroy()
        productView(tk.Tk())


    def viewCategory(self):
        self.root.destroy()
        categoryView(tk.Tk())


    def viewCustomer(self):
        self.root.destroy()
        customerView(tk.Tk())

    def viewSales(self):
        self.root.destroy()
        salesView(tk.Tk())

    def viewReturn(self):
        self.root.destroy()
        returnView(tk.Tk())

    def thisCategory(self, event):
        cat = self.category_select.get()
        self.product_name_entry1.set('')
        self.quntaty_entry1.delete(0, tk.END)
        if cat:
            self.product_name_entry1.config(values=Product.onselect(cat))


    def defaultQuntaty(self, event):
        self.quntaty_entry1.delete(0, tk.END)
        self.quntaty_entry1.insert(0,'1')

    def clearBill(self):
        self.cardTotal.set(0)
        self.less.set(0)
        self.due.set(0)
        self.paid.set(0)
        self.name.set('')
        self.mobile.set('')
        self.email.set('')

    def logout(self):
        ans = messagebox.askokcancel("Confirm", "Are you sure to logout ?")
        if ans == True:
            self.root.quit()
            
    def thisBackground(self, event):
        bg = None
        color = self.background.get()
        if color=='Default':
            bg=("#eeeeee")
        else:
            bg=(color)
        SettingController.updateJsonFile(self,"backgroundColor",bg)
        SettingController.getDeshboardBackground(self)