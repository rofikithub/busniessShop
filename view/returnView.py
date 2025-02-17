import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from view import dashboardView
from controller.ReturnController import ReturnController


class returnView:
    def __init__(self, root):
        self.root = root
        root.title("Product Return")
        ww = 1200
        wh = 600
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(50)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        # root.resizable(False, False)


        self.sID   = tk.StringVar()
        
        self.voucher = tk.IntVar()
        self.proID   = tk.IntVar()
        self.proName = tk.StringVar()
        self.price   = tk.IntVar()
        self.oldQun  = tk.IntVar()
        self.proQun  = tk.IntVar()
        self.cid     = tk.IntVar()



        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())


        frame = tk.Frame(root, padx=20, pady=20, relief=tk.RAISED)
        frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        label_frame = tk.LabelFrame(frame, text="Product Return Details", padx=5, pady=5)
        label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        # Update
        update_frame = tk.Frame(label_frame, padx=10, pady=10, bg=None)
        update_frame.pack(side=LEFT, expand=True)

        name_frame = tk.Frame(update_frame, padx=10, pady=5, bg=None)
        name_frame.pack(side=TOP)
        product_name_label = tk.Label(name_frame, text="Bill Number    ", bg=None)
        product_name_label.pack(side=LEFT)
        self.product_name_entry = tk.Entry(name_frame, textvariable=self.sID, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.product_name_entry.pack(side=LEFT)
        self.sID.trace("w", lambda name, index, mode, vars=vars: ReturnController.showBill(self))


        quantity_frame = tk.Frame(update_frame, padx=10, pady=5)
        quantity_frame.pack(side=TOP)
        quantity_label = tk.Label(quantity_frame, text="Voucher          ")
        quantity_label.pack(side=LEFT)
        self.quantity_entry = tk.Entry(quantity_frame, textvariable=self.voucher, width=20, font=("Arial", 10), border=0, state=DISABLED, highlightthickness=1,highlightbackground="#ddd")
        self.quantity_entry.pack(side=LEFT)

        sell_frame = tk.Frame(update_frame, padx=10, pady=5)
        sell_frame.pack(side=TOP)
        sell_price_label = tk.Label(sell_frame, text="Product ID      ")
        sell_price_label.pack(side=LEFT)
        self.sell_price_entry = tk.Entry(sell_frame, textvariable=self.proID, width=20, font=("Arial", 10), border=0, state=DISABLED, highlightthickness=1,highlightbackground="#ddd")
        self.sell_price_entry.pack(side=LEFT)

        cost_frame = tk.Frame(update_frame, padx=10, pady=5)
        cost_frame.pack(side=TOP)
        cost_price_label = tk.Label(cost_frame, text="Product          ")
        cost_price_label.pack(side=LEFT)
        self.cost_price_entry = tk.Entry(cost_frame, textvariable=self.proName, width=20, font=("Arial", 10), border=0, state=DISABLED, highlightthickness=1,highlightbackground="#ddd")
        self.cost_price_entry.pack(side=LEFT)

        cost_frame = tk.Frame(update_frame, padx=10, pady=5)
        cost_frame.pack(side=TOP)
        cost_price_label = tk.Label(cost_frame, text="Price               ")
        cost_price_label.pack(side=LEFT)
        self.cost_price_entry = tk.Entry(cost_frame, textvariable=self.price, width=20, font=("Arial", 10), border=0, state=DISABLED, highlightthickness=1,highlightbackground="#ddd")
        self.cost_price_entry.pack(side=LEFT)

        cost_frame = tk.Frame(update_frame, padx=10, pady=5)
        cost_frame.pack(side=TOP)
        cost_price_label = tk.Label(cost_frame, text="Quantity        ")
        cost_price_label.pack(side=LEFT)
        self.cost_price_entry = tk.Entry(cost_frame, textvariable=self.proQun, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.cost_price_entry.pack(side=LEFT)


        btn_frame = tk.Frame(update_frame, padx=10, pady=60)
        btn_frame.pack(fill=tk.BOTH, side=TOP)
        new_product_save_btn = tk.Button(btn_frame, command= lambda: ReturnController.productReturn(self), padx=30, text="Update", bg="#B0A695", fg="black", font=("Arial", 8), border=0.5)
        new_product_save_btn.pack(side=TOP)


        go_back_label = tk.Label(update_frame, text='Go back', borderwidth=0, relief="groove",bg="#176B87", fg="white", padx=50, cursor='hand2')
        go_back_label.pack(side=BOTTOM, anchor='c')
        go_back_label.bind("<Button-1>", backDeshboard)


        # Sales.....
        sale_frame = tk.Frame(label_frame, padx=10, pady=10, bg=None)
        sale_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(sale_frame, selectmode='browse')
        self.tree.pack(side=LEFT, fill=BOTH)


        verscrlbar = ttk.Scrollbar(sale_frame,orient="vertical",command=self.tree.yview)
        verscrlbar.pack(side=RIGHT, fill=BOTH, expand=True)
        self.tree.configure(xscrollcommand=verscrlbar.set)

        self.tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=90, anchor='c')
        self.tree.column("2", width=120, anchor='w')
        self.tree.column("3", width=120, anchor='w')
        self.tree.column("4", width=60, anchor='c')
        self.tree.column("5", width=60, anchor='c')
        self.tree.column("6", width=60, anchor='c')
        self.tree.column("7", width=60, anchor='c')
        self.tree.column("8", width=60, anchor='c')
        self.tree.column("9", width=90, anchor='c')


        self.tree.heading("1", text="No")
        self.tree.heading("2", text="Customer Name")
        self.tree.heading("3", text="Total")
        self.tree.heading("4", text="Less")
        self.tree.heading("5", text="Due")
        self.tree.heading("6", text="Paid")
        self.tree.heading("7", text="Status")
        self.tree.heading("8", text="Profit")
        self.tree.heading("9", text="Date")
        # self.tree.bind('<ButtonRelease-1>', self.selectProduct)


        # List.....
        list_frame = tk.Frame(label_frame, padx=10, pady=10, bg=None)
        list_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.treel = ttk.Treeview(list_frame, selectmode='browse')
        self.treel.pack(side=LEFT, fill=BOTH)


        verscrlbar = ttk.Scrollbar(list_frame,orient="vertical",command=self.treel.yview)
        verscrlbar.pack(side=RIGHT, fill=BOTH, expand=True)
        self.treel.configure(xscrollcommand=verscrlbar.set)


        self.treel["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        self.treel['show'] = 'headings'
        self.treel.column("1", width=90, anchor='c')
        self.treel.column("2", width=200, anchor='c')
        self.treel.column("3", width=100, anchor='c')
        self.treel.column("4", width=90, anchor='c')
        self.treel.column("5", width=80, anchor='c')
        self.treel.column("6", width=80, anchor='c')
        self.treel.column("7", width=80, anchor='c')


        self.treel.heading("1", text="No")
        self.treel.heading("2", text="Product Name")
        self.treel.heading("3", text="Price")
        self.treel.heading("4", text="Quantity")
        self.treel.heading("5", text="CID")
        self.treel.heading("6", text="SID")
        self.treel.heading("7", text="PID")
        self.treel.bind('<ButtonRelease-1>', self.selectProduct)


    def selectProduct(self,event):
        items = self.treel.focus()
        item  = self.treel.item(items)
        if items:
            self.voucher.set(item['values'][0])
            self.proName.set(item['values'][1])
            self.proID.set(item['values'][6])
            self.oldQun.set(item['values'][3])
            self.proQun.set(item['values'][3])
            self.price.set(item['values'][2])








