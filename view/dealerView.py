import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

from controller.DealerController import DealerController
from controller.PurchaseController import PurchaseController
from controller.SettingController import SettingController
from model.Dealer import Dealer
from view import dashboardView
from controller.CustomerController import CustomerController
from model.Category import Category


class dealerView:
    def __init__(self, root):
        self.root = root
        root.title("Dealer Window")
        ww = 900
        wh = 650
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()-90
        c_x = int(sw / 2 - ww / 2)
        c_y = int(10)
        root.geometry(f'{ww}x{sh}+{c_x}+{c_y}')
        root.resizable(False, False)
        
        self.bg = SettingController.bgColor(self)

        self.did     = tk.IntVar()
        self.company = tk.StringVar()
        self.mobile  = tk.StringVar()
        self.srname  = tk.StringVar()

        self.pid      = tk.IntVar()
        self.dealer   = tk.StringVar()
        self.voucher  = tk.StringVar()
        self.purchase = tk.IntVar()
        self.payment  = tk.IntVar()
        self.newDue   = tk.IntVar()
        self.previous = tk.IntVar()
        self.totalDue = tk.IntVar()


        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())


        frame = tk.Frame(root, padx=20, pady=20, relief=tk.RAISED, background=self.bg)
        frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        label_frame = tk.LabelFrame(frame, text="Dealer Details", padx=5, pady=5, background=self.bg)
        label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)


        # Customer Details
        dealer_frame = tk.Frame(label_frame, pady=5, padx=20, background=self.bg)
        dealer_frame.pack(side='top', expand=True)

        company_label = tk.Label(dealer_frame, text="Company  ", padx=12, background=self.bg)
        company_label.pack(side='left')
        company_entry = tk.Entry(dealer_frame, textvariable=self.company, bd=0.5, width=20, border=0, font=('Arial', 10), highlightthickness=1,highlightbackground = "#ddd")
        company_entry.pack(side='left')

        mobile_label = tk.Label(dealer_frame, text="Mobile ", padx=10, background=self.bg)
        mobile_label.pack(side='left')
        mobile_entry = tk.Entry(dealer_frame, textvariable=self.mobile, bd=0.5, width=15, font=('Arial', 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        mobile_entry.pack(side='left')

        srname_label = tk.Label(dealer_frame, text="SR Name ", padx=10, background=self.bg)
        srname_label.pack(side='left')
        srname_entry = tk.Entry(dealer_frame, textvariable=self.srname, bd=0.5, width=20, font=('Arial', 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        srname_entry.pack(side='left')

        dealer_delete_frame = tk.Frame(dealer_frame, padx=5, background=self.bg)
        dealer_delete_frame.pack(side='left')
        dealer_delete_btn = tk.Button(dealer_delete_frame, command=lambda :DealerController.deleteDealer(self), text="Delete", padx=5, bg="#E25E3E", fg="black", font=("Arial", 8), border=0.5)
        dealer_delete_btn.pack(side='left')

        dealer_update_frame = tk.Frame(dealer_frame, background=self.bg)
        dealer_update_frame.pack(side='left')
        dealer_update_btn = tk.Button(dealer_update_frame, command=lambda :DealerController.updateDealer(self), text="Update", padx=5, bg="#B0A695", fg="black", font=("Arial", 8), border=0.5)
        dealer_update_btn.pack(side='left')

        dealer_save_frame = tk.Frame(dealer_frame, padx=5, background=self.bg)
        dealer_save_frame.pack(side='left')
        dealer_save_btn = tk.Button(dealer_save_frame, command=lambda :DealerController.createDealer(self), text="Save", padx=15, bg="#A2C579", fg="black", font=("Arial", 8), border=0.5)
        dealer_save_btn.pack(side='left')

        # Update
        option_frame = tk.Frame(label_frame, background=self.bg)
        option_frame.pack(side=TOP, expand=True)

        company_frame = tk.Frame(option_frame, padx=10, pady=10, background=self.bg)
        company_frame.pack(side=LEFT, expand=True)

        name_frame = tk.Frame(company_frame, padx=10, pady=7, background=self.bg)
        name_frame.pack(side=TOP)
        company_name_label = tk.Label(name_frame, text="Company       ", background=self.bg)
        company_name_label.pack(side=LEFT)
        self.company_name_entry = ttk.Combobox(name_frame, textvariable=self.dealer, values=Dealer.list(self), width=17, font=("Arial", 10))
        self.company_name_entry.pack(side=LEFT)
        self.company_name_entry.bind('<<ComboboxSelected>>', self.thisCompany)


        voucher_frame = tk.Frame(company_frame, padx=10, pady=7, background=self.bg)
        voucher_frame.pack(side=TOP)
        voucher_label = tk.Label(voucher_frame, text="Voucher No    ", background=self.bg)
        voucher_label.pack(side=LEFT)
        voucher_entry = tk.Entry(voucher_frame, textvariable=self.voucher, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        voucher_entry.pack(side=LEFT)

        purchase_frame = tk.Frame(company_frame, padx=10, pady=7, background=self.bg)
        purchase_frame.pack(side=TOP)
        purchase_label = tk.Label(purchase_frame, text="Purchase         ", background=self.bg)
        purchase_label.pack(side=LEFT)
        purchase_entry = tk.Entry(purchase_frame, textvariable=self.purchase, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        purchase_entry.pack(side=LEFT)

        payment_frame = tk.Frame(company_frame, padx=10, pady=7, background=self.bg)
        payment_frame.pack(side=TOP)
        payment_label = tk.Label(payment_frame, text="Payment          ", background=self.bg)
        payment_label.pack(side=LEFT)
        payment_entry = tk.Entry(payment_frame, textvariable=self.payment, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        payment_entry.pack(side=LEFT)
        self.payment.trace("w", lambda name, index, mode, vars=vars: PurchaseController.purchaseCalculate(self))

        newdue_frame = tk.Frame(company_frame, padx=10, pady=7, background=self.bg)
        newdue_frame.pack(side=TOP)
        newdue_label = tk.Label(newdue_frame, text="New Due         ", background=self.bg)
        newdue_label.pack(side=LEFT)
        newdue_entry = tk.Entry(newdue_frame, textvariable=self.newDue, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        newdue_entry.pack(side=LEFT)

        revious_frame = tk.Frame(company_frame, padx=10, pady=7, background=self.bg)
        revious_frame.pack(side=TOP)
        revious_label = tk.Label(revious_frame, text="Previous Due   ", background=self.bg)
        revious_label.pack(side=LEFT)
        revious_entry = tk.Entry(revious_frame, textvariable=self.previous, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        revious_entry.pack(side=LEFT)

        total_frame = tk.Frame(company_frame, padx=10, pady=7, background=self.bg)
        total_frame.pack(side=TOP)
        total_label = tk.Label(total_frame, text="Total Due        ", background=self.bg)
        total_label.pack(side=LEFT)
        total_entry = tk.Entry(total_frame, textvariable=self.totalDue, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        total_entry.pack(side=LEFT)

        delete_frame = tk.Frame(company_frame, padx=5, background=self.bg)
        delete_frame.pack(fill=tk.BOTH, side=LEFT)
        delete_btn = tk.Button(delete_frame, command=lambda: PurchaseController.deletePurchase(self), padx=8, text="Delete", bg="#E25E3E", fg="black", font=("Arial", 8), border=0.5)
        delete_btn.pack(side=TOP)

        print_frame = tk.Frame(company_frame, padx=5, background=self.bg)
        print_frame.pack(fill=tk.BOTH, side=LEFT)
        print_btn = tk.Button(print_frame, command=lambda: PurchaseController.print(self), padx=8, text="Print", bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        print_btn.pack(side=TOP)

        updates_frame = tk.Frame(company_frame, padx=5, background=self.bg)
        updates_frame.pack(fill=tk.BOTH, side=LEFT)
        updates_btn = tk.Button(updates_frame, command=lambda: PurchaseController.updatePurchase(self), padx=8, text="Update", bg="#B0A695", fg="black", font=("Arial", 8), border=0.5)
        updates_btn.pack(side=TOP)

        save_frame = tk.Frame(company_frame, padx=5, background=self.bg)
        save_frame.pack(fill=tk.BOTH, side=LEFT)
        save_btn = tk.Button(save_frame, command=lambda :PurchaseController.createPurchase(self), padx=11, text="Save", bg="#A2C579", fg="black", font=("Arial", 8), border=0.5)
        save_btn.pack(side=TOP)


        # List.....
        dlist_frame = tk.Frame(option_frame, padx=10, pady=10, bg=None)
        dlist_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.treed = ttk.Treeview(dlist_frame, selectmode='browse')
        self.treed.pack(side=LEFT, fill=BOTH)


        verscrlbard = ttk.Scrollbar(dlist_frame,orient="vertical",command=self.treed.yview)
        verscrlbard.pack(side=RIGHT, fill=BOTH, expand=True)
        self.treed.configure(xscrollcommand=verscrlbard.set)

        self.treed["columns"] = ("1", "2", "3", "4")
        self.treed['show'] = 'headings'
        self.treed.column("1", width=70, anchor='w')
        self.treed.column("2", width=150, anchor='w')
        self.treed.column("3", width=150, anchor='w')
        self.treed.column("4", width=150, anchor='w')


        self.treed.heading("1", text="No")
        self.treed.heading("2", text="Company")
        self.treed.heading("3", text="Mobile")
        self.treed.heading("4", text="SR Name")
        self.treed.bind('<ButtonRelease-1>', self.selectDealer)


        #Report
        plist_frame = tk.Frame(label_frame, padx=10, pady=10)
        plist_frame.pack(side=TOP, expand=True)

        self.treep = ttk.Treeview(plist_frame, selectmode='browse')
        self.treep.pack(side=LEFT, fill=BOTH)

        verscrlbarp = ttk.Scrollbar(plist_frame, orient="vertical", command=self.treep.yview)
        verscrlbarp.pack(side=RIGHT, fill=BOTH, expand=True)
        self.treep.configure(xscrollcommand=verscrlbarp.set)

        self.treep["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.treep['show'] = 'headings'
        self.treep.column("1", width=80, anchor='w')
        self.treep.column("2", width=80, anchor='w')
        self.treep.column("3", width=100, anchor='w')
        self.treep.column("4", width=80, anchor='w')
        self.treep.column("5", width=80, anchor='w')
        self.treep.column("6", width=80, anchor='w')
        self.treep.column("7", width=80, anchor='w')
        self.treep.column("8", width=100, anchor='w')
        self.treep.column("9", width=50, anchor='w')
        self.treep.column("10", width=50, anchor='w')

        self.treep.heading("1", text="No")
        self.treep.heading("2", text="Date")
        self.treep.heading("3", text="Voucher")
        self.treep.heading("4", text="Purchase")
        self.treep.heading("5", text="Payment")
        self.treep.heading("6", text="New Due")
        self.treep.heading("7", text="Previous Due")
        self.treep.heading("8", text="Total Due")
        self.treep.heading("9", text="CID")
        self.treep.heading("10", text="ID")
        self.treep.bind('<ButtonRelease-1>', self.selectPurchase)


        go_back_label = tk.Label(label_frame, text='Go back', borderwidth=0, relief="groove", padx=50, bg="#176B87", fg="white", cursor='hand2')
        go_back_label.pack(side=BOTTOM, anchor='s')
        go_back_label.bind("<Button-1>", backDeshboard)

        DealerController.dealerShow(self)

    def selectDealer(self,event):
        items = self.treed.focus()
        item  = self.treed.item(items)
        if items:
            self.did.set(item['values'][0])
            self.company.set(item['values'][1])
            self.dealer.set(item['values'][1])
            self.mobile.set('0'+str(item['values'][2]))
            self.srname.set(item['values'][3])
            PurchaseController.getprevious(self, item['values'][1])
            PurchaseController.purchaseShow(self,item['values'][0])


    def selectPurchase(self,event):
        items = self.treep.focus()
        item  = self.treep.item(items)
        if items:
            self.pid.set(item['values'][9])
            self.did.set(item['values'][8])
            self.voucher.set(item['values'][2])
            self.purchase.set(item['values'][3])
            self.payment.set(item['values'][4])
            self.newDue.set(item['values'][5])
            self.previous.set(item['values'][6])
            self.totalDue.set(item['values'][7])

    def thisCompany(self, event):
        ven = self.company_name_entry.get()
        self.pid.set('0')
        self.voucher.set("")
        self.purchase.set('0')
        self.payment.set('0')
        self.newDue.set('0')
        self.previous.set('0')
        self.totalDue.set('0')

        self.did.set(Dealer.getid(self,ven))
        PurchaseController.getprevious(self, ven)








