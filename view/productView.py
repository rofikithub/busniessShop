import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from view import dashboardView
from controller.ProductController import ProductController
from model.Category import Category


class productView:
    def __init__(self, root):
        self.root = root
        root.title("Product")
        ww = 890
        wh = 600
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(50)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        root.resizable(False, False)

        self.proID   = tk.IntVar()
        self.proName = tk.StringVar()
        self.catName = tk.StringVar()
        self.proQun  = tk.IntVar()
        self.sPrice  = tk.IntVar()
        self.cPrice  = tk.IntVar()


        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())


        frame = tk.Frame(root, padx=20, pady=20, relief=tk.RAISED)
        frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        label_frame = tk.LabelFrame(frame, text="Product Details", padx=5, pady=5)
        label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        # Update
        update_frame = tk.Frame(label_frame, padx=10, pady=10, bg=None)
        update_frame.pack(side=LEFT, expand=True)

        name_frame = tk.Frame(update_frame, padx=10, pady=10, bg=None)
        name_frame.pack(side=TOP)
        product_name_label = tk.Label(name_frame, text="Name        ", bg=None)
        product_name_label.pack(side=LEFT)
        self.product_name_entry = tk.Entry(name_frame, textvariable=self.proName, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.product_name_entry.pack(side=LEFT)

        category_frame = tk.Frame(update_frame, padx=10, pady=10)
        category_frame.pack(side=TOP)
        category_label = tk.Label(category_frame, text="Category  ")
        category_label.pack(side=LEFT)
        self.category_entry = ttk.Combobox(category_frame, textvariable=self.catName, state="readonly", values=Category().list(), width=20)
        self.category_entry.pack(side=LEFT)

        quantity_frame = tk.Frame(update_frame, padx=10, pady=10)
        quantity_frame.pack(side=TOP)
        quantity_label = tk.Label(quantity_frame, text="Quantity   ")
        quantity_label.pack(side=LEFT)
        self.quantity_entry = tk.Entry(quantity_frame, textvariable=self.proQun, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.quantity_entry.pack(side=LEFT)

        sell_frame = tk.Frame(update_frame, padx=10, pady=10)
        sell_frame.pack(side=TOP)
        sell_price_label = tk.Label(sell_frame, text="Sell Price   ")
        sell_price_label.pack(side=LEFT)
        self.sell_price_entry = tk.Entry(sell_frame, textvariable=self.sPrice, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.sell_price_entry.pack(side=LEFT)

        cost_frame = tk.Frame(update_frame, padx=10, pady=10)
        cost_frame.pack(side=TOP)
        cost_price_label = tk.Label(cost_frame, text="Cost Price  ")
        cost_price_label.pack(side=LEFT)
        self.cost_price_entry = tk.Entry(cost_frame, textvariable=self.cPrice, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.cost_price_entry.pack(side=LEFT)

        save_frame = tk.Frame(update_frame, padx=10, pady=40)
        save_frame.pack(fill=tk.BOTH, side=TOP)
        product_save_btn = tk.Button(save_frame, command=lambda : ProductController.createProduct(self), padx=20, text="Save", bg="#A2C579", fg="black", font=("Arial", 8), border=0.5)
        product_save_btn.pack(side=TOP)

        btn_frame = tk.Frame(update_frame, padx=10)
        btn_frame.pack(fill=tk.BOTH, side=TOP)
        new_product_save_btn = tk.Button(btn_frame, command=lambda : ProductController.update(self), padx=30, text="Update", bg="#B0A695", fg="black", font=("Arial", 8), border=0.5)
        new_product_save_btn.pack(side=TOP)

        save_frame = tk.Frame(update_frame, padx=10, pady=20)
        save_frame.pack(fill=tk.BOTH, side=TOP)
        save_btn = tk.Button(save_frame, command=lambda : ProductController.print(self),text="Print", padx=40, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        save_btn.pack(side=TOP)


        qr_frame = tk.Frame(update_frame, padx=10, pady=30)
        qr_frame.pack(fill=tk.BOTH, side=TOP)
        qr_btn = tk.Button(qr_frame, command=lambda : ProductController.printqr(self),text="Print QR Code", padx=40, bg="#ddd", fg="black", font=("Arial", 8), border=0.5)
        qr_btn.pack(side=TOP)

        go_back_label = tk.Label(update_frame, text='Go back', borderwidth=0, relief="groove", padx=50, bg="#176B87", fg="white", cursor='hand2')
        go_back_label.pack(side=BOTTOM, anchor='c')
        go_back_label.bind("<Button-1>", backDeshboard)


        # List.....
        list_frame = tk.Frame(label_frame, padx=10, pady=10, bg=None)
        list_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(list_frame, selectmode='browse')
        self.tree.pack(side=LEFT, fill=BOTH)


        verscrlbar = ttk.Scrollbar(list_frame,orient="vertical",command=self.tree.yview)
        verscrlbar.pack(side=RIGHT, fill=BOTH, expand=True)
        self.tree.configure(xscrollcommand=verscrlbar.set)

        self.tree["columns"] = ("1", "2", "3", "4", "5", "6")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=60, anchor='c')
        self.tree.column("2", width=90, anchor='w')
        self.tree.column("3", width=90, anchor='w')
        self.tree.column("4", width=90, anchor='c')
        self.tree.column("5", width=90, anchor='c')
        self.tree.column("6", width=90, anchor='c')


        self.tree.heading("1", text="No")
        self.tree.heading("2", text="Name")
        self.tree.heading("3", text="Category")
        self.tree.heading("4", text="Quantity")
        self.tree.heading("5", text="Sall Price")
        self.tree.heading("6", text="Cost Price")
        self.tree.bind('<ButtonRelease-1>', self.selectProduct)

        ProductController.productShow(self)

    def selectProduct(self,event):
        items = self.tree.focus()
        item  = self.tree.item(items)
        if items:
            self.proID.set(item['values'][0])
            self.proName.set(item['values'][1])
            self.catName.set(item['values'][2])
            self.proQun.set(item['values'][3])
            self.sPrice.set(item['values'][4])
            self.cPrice.set(item['values'][5])








