import tkinter as tk
from tkinter import *
from tkinter import ttk
from types import LambdaType
from PIL import ImageTk,Image
from tkinter import messagebox
import PIL
from tkinter_webcam import webcam
from importlib.metadata import files
from PIL import Image as PIM, ImageTk

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
        # root.configure(background='#9AA6B2')

        # Title Bar
        dashboard_frame = tk.Frame(root)
        dashboard_frame.pack(side='top', expand=True)
        label = tk.Label(dashboard_frame, text="Bill Management System", font=("Times New Roman", 20))
        label.pack()
        
        shop_name = tk.Label(dashboard_frame, text="ESHOP ONLINE MARCATE CENTER", font=("Times New Roman", 8))
        shop_name.pack()


        # Customer Details
        customer_frame = tk.Frame(root, pady=5, padx=20)
        customer_frame.pack(fill=tk.BOTH,side='top', expand=True)
        customer_label_frame = tk.LabelFrame(customer_frame, text="Customer Details", pady=10, padx=10)
        customer_label_frame.pack(fill=tk.BOTH, side='left', expand=True)

        bill_number_label = tk.Label(customer_label_frame, text="Bill Number:", pady=10, padx=20)
        bill_number_label.pack(side='left')
        self.bill_number_entry = tk.Entry(customer_label_frame, textvariable=self.billNo, bd=0.5, width=15, border=0, font=('Ubuntu', 13), highlightthickness=1,highlightbackground = "#ddd")
        self.bill_number_entry.pack(side='left')
        bill_number_search = tk.Button(customer_label_frame, command=lambda : BillController.searchBill(self),text="Search", padx=20, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        bill_number_search.pack(side='left')

        mobile_number_label = tk.Label(customer_label_frame, text="Mobile Number:", pady=10, padx=20)
        mobile_number_label.pack(side='left')
        self.mobile_number_entry = tk.Entry(customer_label_frame, textvariable=self.mobile, bd=0.5, width=15, font=12, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.mobile_number_entry.pack(side='left')
        self.mobile.trace("w", lambda name, index, mode, var=self.mobile: BillController.searchName(self))

        customer_name_label = tk.Label(customer_label_frame, text="Customer Name", pady=10, padx=20)
        customer_name_label.pack(side='left')
        self.customer_name_entry = tk.Entry(customer_label_frame, textvariable=self.name, bd=0.5, width=20, font=12, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.customer_name_entry.pack(side='left')


        email_address_label = tk.Label(customer_label_frame, text="Email Address:", pady=10, padx=20)
        email_address_label.pack(side='left')
        self.email_address_entry = tk.Entry(customer_label_frame, textvariable=self.email, bd=0.5, width=20, font=12, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.email_address_entry.pack(side='left')
        #self.email_address_entry.insert(0, "rofik@gmail.com")


        # Product and billing Frame
        details_frame = tk.Frame(root, pady=5, padx=20)
        details_frame.pack(fill=tk.BOTH, side='top', expand=True)

        # Select by category
        details_label_frame = tk.LabelFrame(details_frame, text="Select product by category", pady=20, padx=20)
        details_label_frame.pack(fill=tk.BOTH, side='left', expand=True)


        category_frame = tk.Frame(details_label_frame)
        category_frame.pack(fill=tk.BOTH, side='top' )
        category_label = tk.Label(category_frame, text="Product Category", padx=20, pady=10)
        category_label.pack(side='left')
        self.category_select = ttk.Combobox(category_frame, state="readonly",values=Category().list(), width=30)
        self.category_select.pack(side='left')
        self.category_select.bind('<<ComboboxSelected>>', self.thisCategory)

        product_frame = tk.Frame(details_label_frame)
        product_frame.pack(fill=tk.BOTH, side='top' )
        product_name_label1 = tk.Label(product_frame, text="Product Name     ", padx=20, pady=10)
        product_name_label1.pack(side='left')
        self.product_name_entry1 = ttk.Combobox(product_frame, state="readonly", values=[], width=30)
        self.product_name_entry1.pack(side='left')
        self.product_name_entry1.bind('<<ComboboxSelected>>', self.defaultQuntaty)

        quntaty_frame = tk.Frame(details_label_frame)
        quntaty_frame.pack(fill=tk.BOTH, side='top' )
        quntaty_label1 = tk.Label(quntaty_frame, text="Product Quantity  ", padx=20, pady=10)
        quntaty_label1.pack(side='left')
        self.quntaty_entry1 = tk.Entry(quntaty_frame, textvariable=self.qun, width=22, font=12, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.quntaty_entry1.pack(side='left')


        add_card_frame = tk.Frame(details_label_frame)
        add_card_frame.pack(fill=tk.BOTH, side='top', pady=20 )
        add_to_cart_btn1 = tk.Button(add_card_frame, command=lambda:CardController.addToCard(self), text="Add to card", padx=20, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn1.pack(side='bottom')


        # add_card_frame = tk.Frame(details_label_frame)
        # add_card_frame.pack(fill=tk.BOTH, side='top', pady=20 )
        # add_to_cart_btn1 = tk.Button(add_card_frame, command=lambda:CardController.camera(self), text="Camera", padx=20, bg="#444", fg="white", font=("Arial", 8), border=0.5)
        # add_to_cart_btn1.pack(side='bottom')

        # Select by nane
        label_frame = tk.LabelFrame(details_frame, text="Select product by name", padx=10, pady=10)
        label_frame.pack(fill=tk.BOTH, side='left' )

        name_label_frame = tk.Frame(label_frame)
        name_label_frame.pack(fill=tk.BOTH, side=TOP, expand=True)

        def on_configure(event):
            canvas.configure ( scrollregion=canvas.bbox ( 'all' ) )
        
        canvas = tk.Canvas ( name_label_frame, bg="white")
        canvas.pack ( side="left", fill="both")

        scrollbar = tk.Scrollbar ( name_label_frame, orient="vertical", command=canvas.yview, bg="white")
        scrollbar.pack ( side="right", fill="y" )

        canvas.configure ( yscrollcommand=scrollbar.set )
        canvas.bind ( '<Configure>', on_configure )

        frame_inside_canvas = tk.Frame ( canvas , bg="white")
        canvas.create_window ( (0, 0), window=frame_inside_canvas, anchor='nw' )

        products = Product().all()
        if products :
            self.checkbox_values = []
            self.checkbox_vars = []
            self.entries = {}
            for product in products:
                var = tk.IntVar()
                self.checkbox_vars.append(var)
                self.checkbox_values.append(product[1])
                name_frame = tk.Frame(frame_inside_canvas, bg="white")
                name_frame.pack(side='top', fill=tk.BOTH, expand=False)
                product_checkbutton = tk.Checkbutton(name_frame, text=product[1], variable=var, height=1, bg="white")
                product_checkbutton.pack(side='left', anchor=tk.NW, expand=True)
                self.product_name_entry = tk.Entry(name_frame, width=20, border=0, highlightthickness=1,highlightbackground = "#ddd")
                self.product_name_entry.pack(side='left')
                self.entries[product[1]] = self.product_name_entry

        canvas.update_idletasks ()
        # Set the canvas scroll region
        canvas.config ( scrollregion=canvas.bbox ( "all" ) )

        add_card_frame = tk.Frame(label_frame, pady=5)
        add_card_frame.pack(side=TOP, anchor='s')
        add_to_cart_btn1 = tk.Button(add_card_frame, command=lambda:CardController.getQuntaty(self), text="Add to card", padx=20, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn1.pack()

        # Bill Area
        bill_frame = tk.LabelFrame(details_frame, text="Bill Area", padx=10, pady=5, width=50, height=50)
        bill_frame.pack(fill=tk.BOTH, side='top', expand=True)

        self.bill_box = tk.Text(bill_frame, fg="black", font=("Arial", 9))
        self.bill_box.pack(side='left')

        self.bill_box.delete('1.0', tk.END)
        shop = SettingController.showShop(self)
        if shop:
            self.bill_box.insert(tk.END, '\t\t\t'+str(shop[0])+'\n')
            self.bill_box.insert(tk.END, '\t\t\t        '+str(shop[1])+'\n')
            self.bill_box.insert(tk.END, '\t\t\t           Mobile : - '+str(shop[2])+'\n')
        self.billDetails


        # Option Frame
        option_frame = tk.Frame(root, pady=5, padx=20)
        option_frame.pack(fill=tk.BOTH, expand=True, side='top')

        # Card option
        card_label_frame = tk.LabelFrame(option_frame, text="Card Options", pady=10, padx=10)
        card_label_frame.pack(fill=tk.BOTH, expand=True, side='left')


        total_frame = tk.Frame(card_label_frame, padx=10)
        total_frame.pack(fill=tk.BOTH, side='left')
        total_label = tk.Label(total_frame, text="Total", padx=15, pady=2, bg="#999")
        total_label.pack(side='left')
        self.total_entry = tk.Entry(total_frame, textvariable=self.cardTotal, width=10, font=13, border=0, highlightthickness=1,highlightbackground = "#ddd", state='readonly')
        self.total_entry.pack(side='left')

        total_frame = tk.Frame(card_label_frame, padx=10)
        total_frame.pack(fill=tk.BOTH, side='left' )
        total_label = tk.Label(total_frame, text="Less", padx=10, pady=2, bg="#ddd")
        total_label.pack(side='left')
        self.less_entry = tk.Entry(total_frame, textvariable=self.less, width=7, font=5, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.less_entry.pack(side='left')
        self.less.trace("w", lambda name, index, mode, var=IntVar: CardController.cardCalculate(self))

        total_frame = tk.Frame(card_label_frame, padx=10)
        total_frame.pack(fill=tk.BOTH, side='left' )
        total_label = tk.Label(total_frame, text="Due", padx=10, pady=2, bg="#ddd")
        total_label.pack(side='left')
        self.due_entry = tk.Entry(total_frame, textvariable=self.due, width=7, font=5, border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.due_entry.pack(side='left')
        self.due.trace("w", lambda name, index, mode, var=IntVar: CardController.cardCalculate(self))


        total_frame = tk.Frame(card_label_frame, padx=10)
        total_frame.pack(fill=tk.BOTH, side='left' )
        total_label = tk.Label(total_frame, text="Paid", padx=10, pady=2, bg="#999")
        total_label.pack(side='left')
        self.total_entry = tk.Entry(total_frame, textvariable=self.paid, width=10, font=13, border=0, highlightthickness=1,highlightbackground = "#ddd", state='readonly')
        self.total_entry.pack(side='left')

        add_card_frame = tk.Frame(card_label_frame, padx=20 )
        add_card_frame.pack(fill=tk.BOTH, side='left')
        add_to_cart_btn1 = tk.Button(add_card_frame, command=lambda:CardController.refreshCard(self), text="Refresh Card", padx=20, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn1.pack(side='left')

        off_img = Image.open("./image/volume_off.png").resize((20, 15))
        on_img = Image.open("./image/volume_on.png").resize((20, 15))
        self.v_off_img = ImageTk.PhotoImage(off_img)
        self.v_on_img = ImageTk.PhotoImage(on_img)
        self.volume_image = {"toggle": True}
        volume_frame = tk.Frame(card_label_frame, padx=3 )
        volume_frame.pack(fill=tk.BOTH, side='left')
        self.volume_button = tk.Button(volume_frame, image=self.v_off_img, command=lambda:CardController.cardSpeaker(self), cursor='hand2', padx=20, fg="black", font=("Arial", 8), border=0.1)
        self.volume_button.image = self.v_off_img
        self.volume_button.pack(side='left')

        # Billing option
        bill_label_frame = tk.LabelFrame(option_frame, text="Bill Options", pady=10, padx=10)
        bill_label_frame.pack(fill=tk.BOTH, expand=True, side='left')


        frame = tk.Frame(bill_label_frame, padx=40)
        frame.pack(fill=tk.BOTH, side='left' )
        add_to_cart_btn = tk.Button(frame, text="Save Bill", command=lambda :BillController.createBill(self), padx=20, bg="#A2C579", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn.pack(side='left')

        frame = tk.Frame(bill_label_frame, padx=20)
        frame.pack(fill=tk.BOTH, side='left' )
        add_to_cart_btn = tk.Button(frame, text="Print Bill", command=lambda: BillController.print(self), padx=30, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn.pack(side='left')

        frame = tk.Frame(bill_label_frame, padx=40)
        frame.pack(fill=tk.BOTH, side='left' )
        add_to_cart_btn = tk.Button(frame, command=lambda : self.logout(), text="Logout", padx=20, bg="#E25E3E", fg="black", font=("Arial", 8), border=0.5)
        add_to_cart_btn.pack(side='left')
        
        
        
        shop_name = tk.Label(root, text='© 2025 - Softwar Developed by Md. Rafikul Islam (Rofik), Phone- 01737034338, Email- rofik.it.bd@gmail.com', font=("Times New Roman", 7))
        shop_name.pack(side=BOTTOM, anchor='s')
        

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
