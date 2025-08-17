import tkinter as tk
from tkinter import * # type: ignore
from tkinter import ttk
from PIL import ImageTk,Image
from tkcalendar import DateEntry

from controller.CardController import CardController
from controller.CategoryController import CategoryController
from controller.SalesController import SalesController
from controller.SettingController import SettingController
from view import dashboardView
from view.returnView import returnView
from controller.ProductController import ProductController
from model.Category import Category


class salesView:
    def __init__(self, root):
        self.root = root
        root.title("Sales")
        ww = 1100
        wh = 600
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(50)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        root.resizable(False, False)

        self.sID      = tk.StringVar()
        self.cName    = tk.StringVar()
        self.total    = tk.IntVar()
        self.less     = tk.IntVar()
        self.due      = tk.IntVar()
        self.paid     = tk.IntVar()
        self.status   = tk.IntVar()
        self.taka     = tk.IntVar()

        self.bg = SettingController.bgColor(self)
        self.fg = SettingController.fgColor(self)
        
        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())


        frame = tk.Frame(root, padx=20, pady=20, relief=tk.RAISED, background=self.bg)
        frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        label_frame = tk.LabelFrame(frame, text="Sale Details", padx=5, pady=5, background=self.bg, fg=self.fg)
        label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        # Update
        update_frame = tk.Frame(label_frame, padx=10, pady=10, background=self.bg)
        update_frame.pack(side=LEFT, expand=True)

        name_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        name_frame.pack(side=TOP)
        category_name_label = tk.Label(name_frame, text="Bill   ", background=self.bg, fg=self.fg)
        category_name_label.pack(side=LEFT)
        paid_due_entry = tk.Entry(name_frame, textvariable=self.sID, width=10, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        paid_due_entry.pack(side=LEFT)
        self.sID.trace("w", lambda name, index, mode, vars=vars: SalesController.salesSaearch(self))

        name_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        name_frame.pack(side=TOP)
        category_name_label = tk.Label(name_frame, text="Due   ", background=self.bg, fg=self.fg)
        category_name_label.pack(side=LEFT)
        paid_due_entry = tk.Entry(name_frame, textvariable=self.due, width=10, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd", state='readonly')
        paid_due_entry.pack(side=LEFT)

        name_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        name_frame.pack(side=TOP)
        category_name_label = tk.Label(name_frame, text="Paid   ", background=self.bg, fg=self.fg)
        category_name_label.pack(side=LEFT)
        self.paid_due_entry = tk.Entry(name_frame, textvariable=self.taka, width=10, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.paid_due_entry.pack(side=LEFT)

        options_frame = tk.Frame(update_frame, padx=20, pady=20, background=self.bg)
        options_frame.pack(fill=tk.BOTH, side=TOP)

        btn_frame = tk.Frame(options_frame, padx=10, pady=10, background=self.bg)
        btn_frame.pack(fill=tk.BOTH, side=LEFT)
        product_save_btn = tk.Button(btn_frame, command=lambda : self.viewReturn(), padx=5, text="Product Return", bg="#E25E3E", fg="black", font=("Arial", 8), border=0.5)
        product_save_btn.pack(side=LEFT)

        btn_frame = tk.Frame(options_frame, padx=10, pady=10, background=self.bg)
        btn_frame.pack(fill=tk.BOTH, side=LEFT)
        product_save_btn = tk.Button(btn_frame, command=lambda : SalesController.duePaid(self), padx=20, text="Paid", bg="#A2C579", fg="black", font=("Arial", 8), border=0.5)
        product_save_btn.pack(side=LEFT)

        from_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        from_frame.pack(side=TOP)
        from_label = tk.Label(from_frame, text="From   ",background=self.bg, fg=self.fg)
        from_label.pack(side=LEFT)
        self.from_entry = DateEntry(from_frame,locale='en_US', date_pattern='YYYY-mm-dd', width=10, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.from_entry.pack(side=LEFT)

        to_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        to_frame.pack(side=TOP)
        to_label = tk.Label(to_frame, text="To     ", background=self.bg, fg=self.fg)
        to_label.pack(side=LEFT)
        self.to_entry = DateEntry(to_frame, locale='en_US', date_pattern='YYYY-mm-dd', width=10, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.to_entry.pack(side=LEFT)

        print_frame = tk.Frame(update_frame, padx=20, pady=10, background=self.bg)
        print_frame.pack(fill=tk.BOTH, side=TOP)
        print_btn = tk.Button(print_frame, command=lambda : SalesController.print(self,2), padx=20, text="Print", font=("Arial", 8), border=0.5)
        print_btn.pack(side=TOP)

        list_frame = tk.Frame(update_frame, padx=20, pady=10, background=self.bg)
        list_frame.pack(fill=tk.BOTH, side=TOP)
        list_btn = tk.Button(list_frame, command=lambda : SalesController.print(self,0), padx=30, text="All list print", font=("Arial", 8), border=0.5)
        list_btn.pack(side=TOP)

        due_frame = tk.Frame(update_frame, padx=20, pady=10, background=self.bg)
        due_frame.pack(fill=tk.BOTH, side=TOP)
        due_btn = tk.Button(due_frame, command=lambda : SalesController.print(self,1), padx=40, text="All due print", font=("Arial", 8), border=0.5)
        due_btn.pack(side=TOP)

        back_frame = tk.Frame(update_frame, padx=20, pady=30, background=self.bg)
        back_frame.pack(fill=tk.BOTH, side=BOTTOM)
        go_back_label = tk.Label(back_frame, text='Go back', borderwidth=0, relief="groove", bg="#176B87", fg="white", padx=50, cursor='hand2')
        go_back_label.pack(side=BOTTOM, anchor='s')
        go_back_label.bind("<Button-1>", backDeshboard)


        # List.....
        list_frame = tk.Frame(label_frame, padx=10, pady=10)
        list_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(list_frame, selectmode='browse')
        self.tree.pack(side=LEFT, fill=BOTH)


        verscrlbar = ttk.Scrollbar(list_frame,orient="vertical",command=self.tree.yview)
        verscrlbar.pack(side=RIGHT, fill=BOTH, expand=True)
        self.tree.configure(xscrollcommand=verscrlbar.set)

        self.tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=70, anchor='w')
        self.tree.column("2", width=150, anchor='w')
        self.tree.column("3", width=80, anchor='w')
        self.tree.column("4", width=70, anchor='w')
        self.tree.column("5", width=70, anchor='w')
        self.tree.column("6", width=70, anchor='w')
        self.tree.column("7", width=70, anchor='w')
        self.tree.column("8", width=80, anchor='w')
        self.tree.column("9", width=80, anchor='w')


        self.tree.heading("1", text="No")
        self.tree.heading("2", text="Name")
        self.tree.heading("3", text="Total")
        self.tree.heading("4", text="Less")
        self.tree.heading("5", text="Due")
        self.tree.heading("6", text="Paid")
        self.tree.heading("7", text="Profit")
        self.tree.heading("8", text="Status")
        self.tree.heading("9", text="Date")
        self.tree.bind('<ButtonRelease-1>', self.selectCategory)
        SalesController.salesShow(self)


    def selectCategory(self,event):
        items = self.tree.focus()
        item  = self.tree.item(items)
        if items:
            self.sID      .set(item['values'][0])
            self.cName    .set(item['values'][1])
            self.total    .set(item['values'][2])
            self.less     .set(item['values'][3])
            self.due      .set(item['values'][4])
            self.paid     .set(item['values'][5])

            if item['values'][7]=="Paid":
                self.status.set(0)
            elif item['values'][7]=="Due":
                self.status.set(1)

    def viewReturn(self):
        self.root.destroy()
        returnView(tk.Tk())


