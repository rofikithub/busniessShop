import tkinter as tk
from tkinter import * # type: ignore
from tkinter import ttk
from PIL import ImageTk,Image
from unicodedata import category

from controller.CardController import CardController
from controller.CategoryController import CategoryController
from controller.SettingController import SettingController
from view import dashboardView
from controller.ProductController import ProductController
from model.Category import Category


class categoryView:
    def __init__(self, root):
        self.root = root
        root.title("Category")
        ww = 500
        wh = 450
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(100)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        root.resizable(False, False)

        self.catID = tk.IntVar()
        self.cName = tk.StringVar()
        
        self.bg = SettingController.bgColor(self)
        self.fg = SettingController.fgColor(self)

        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())


        frame = tk.Frame(root, padx=20, pady=20, relief=tk.RAISED, background=self.bg)
        frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        label_frame = tk.LabelFrame(frame, text="Category Details", padx=5, pady=5, background=self.bg, fg=self.fg)
        label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        # Update
        update_frame = tk.Frame(label_frame, padx=10, pady=10, background=self.bg)
        update_frame.pack(side=LEFT, expand=True)

        name_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        name_frame.pack(side=TOP)
        category_name_label = tk.Label(name_frame, text="Name        ", background=self.bg, fg=self.fg)
        category_name_label.pack(side=LEFT)
        self.category_name_entry = tk.Entry(name_frame, textvariable=self.cName, width=15, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.category_name_entry.pack(side=LEFT)

        save_frame = tk.Frame(update_frame, padx=40, pady=40, background=self.bg)
        save_frame.pack(fill=tk.BOTH, side=TOP)
        new_save_btn = tk.Button(save_frame, command=lambda :CategoryController.createCategory(self), padx=20, text="Save", bg="#A2C579", fg="black", font=("Arial", 8), border=0.5)
        new_save_btn.pack(side=TOP)

        btn_frame = tk.Frame(update_frame, padx=40, background=self.bg)
        btn_frame.pack(fill=tk.BOTH, side=TOP)
        product_save_btn = tk.Button(btn_frame, command=lambda :CategoryController.update(self), padx=30, text="Update", bg="#B0A695", fg="black", font=("Arial", 8), border=0.5)
        product_save_btn.pack(side=TOP)

        back_frame = tk.Frame(update_frame, padx=40, pady=40, background=self.bg)
        back_frame.pack(fill=tk.BOTH, side=BOTTOM)
        go_back_label = tk.Label(back_frame, text='Go back', borderwidth=0, bg="#176B87", fg="white", relief="groove", padx=40, cursor='hand2')
        go_back_label.pack(side=BOTTOM, anchor='s')
        go_back_label.bind("<Button-1>", backDeshboard)


        # List.....
        list_frame = tk.Frame(label_frame, padx=10, pady=10, bg=None)
        list_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.treev = ttk.Treeview(list_frame, selectmode='browse')
        self.treev.pack(side=LEFT, fill=BOTH)


        verscrlbar = ttk.Scrollbar(list_frame,orient="vertical",command=self.treev.yview)
        verscrlbar.pack(side=RIGHT, fill=BOTH, expand=True)
        self.treev.configure(xscrollcommand=verscrlbar.set)

        self.treev["columns"] = ("1", "2")
        self.treev['show'] = 'headings'
        self.treev.column("1", width=60, anchor='w')
        self.treev.column("2", width=90, anchor='w')


        self.treev.heading("1", text="No")
        self.treev.heading("2", text="Name")
        self.treev.bind('<ButtonRelease-1>', self.selectCategory)
        CategoryController.categoryShow(self)


    def selectCategory(self,event):
        items = self.treev.focus()
        item  = self.treev.item(items)
        if items:
            self.catID.set(item['values'][0])
            self.cName.set(item['values'][1])






