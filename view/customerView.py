import tkinter as tk
from tkinter import *
from tkinter import ttk
from controller.JsonController import JsonController
from view import dashboardView
from controller.CustomerController import CustomerController


class customerView:
    def __init__(self, root):
        self.root = root
        root.title("Customer List")
        ww = 850
        wh = 600
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(50)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        self.root.iconbitmap(r'image\winico.ico')
        root.resizable(False, False)

        self.cID     = tk.IntVar()
        self.cName   = tk.StringVar()
        self.cMobile = tk.StringVar()
        self.cEmail  = tk.StringVar()
        
        self.bg = JsonController.bgColor(self)
        self.fg = JsonController.fgColor(self)

        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())


        frame = tk.Frame(root, padx=20, pady=20, relief=tk.RAISED, background=self.bg)
        frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        label_frame = tk.LabelFrame(frame, text="Customer add and update", padx=5, pady=5, background=self.bg, fg=self.fg)
        label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        # Update
        update_frame = tk.Frame(label_frame, padx=10, pady=10, background=self.bg)
        update_frame.pack(side=LEFT, expand=True)

        name_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        name_frame.pack(side=TOP)
        customer_name_label = tk.Label(name_frame, text="Name        ", background=self.bg, fg=self.fg)
        customer_name_label.pack(side=LEFT)
        self.customer_name_entry = tk.Entry(name_frame, textvariable=self.cName, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.customer_name_entry.pack(side=LEFT)


        mobile_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        mobile_frame.pack(side=TOP)
        mobile_label = tk.Label(mobile_frame, text="Mobile     ", background=self.bg, fg=self.fg)
        mobile_label.pack(side=LEFT)
        self.mobile_entry = tk.Entry(mobile_frame, textvariable=self.cMobile, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.mobile_entry.pack(side=LEFT)

        email_frame = tk.Frame(update_frame, padx=10, pady=10, background=self.bg)
        email_frame.pack(side=TOP)
        email_label = tk.Label(email_frame, text="Email       ", background=self.bg, fg=self.fg)
        email_label.pack(side=LEFT)
        self.email_entry = tk.Entry(email_frame, textvariable=self.cEmail, width=20, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground="#ddd")
        self.email_entry.pack(side=LEFT)


        save_frame = tk.Frame(update_frame, padx=20, pady=40, background=self.bg)
        save_frame.pack(fill=tk.BOTH, side=TOP)
        save_btn = tk.Button(save_frame, command=lambda :CustomerController.createCustomer(self), padx=20, text="Save", bg="#A2C579", fg="black", font=("Arial", 8), border=0.5, relief="flat", cursor='hand2')
        save_btn.pack(side=TOP)

        updates_frame = tk.Frame(update_frame, padx=20, background=self.bg)
        updates_frame.pack(fill=tk.BOTH, side=TOP)
        updates_btn = tk.Button(updates_frame, command=lambda : CustomerController.updateCustomer(self), padx=30, text="Update", bg="#B0A695", fg="black", font=("Arial", 8), border=0.5, relief="flat", cursor='hand2')
        updates_btn.pack(side=TOP)

        print_frame = tk.Frame(update_frame, padx=20, pady=40, background=self.bg)
        print_frame.pack(fill=tk.BOTH, side=TOP)
        print_btn = tk.Button(print_frame, command=lambda :CustomerController.print(self), padx=40, text="Print", bg="#ddd", fg="black", font=("Arial", 8), border=0.5, relief="flat", cursor='hand2')
        print_btn.pack(side=TOP)

        go_back_label = tk.Label(update_frame, text='Go back', borderwidth=0, relief="groove",bg="#176B87", fg="white", padx=50, cursor='hand2')
        go_back_label.pack(side=BOTTOM, anchor='s')
        go_back_label.bind("<Button-1>", backDeshboard)


        # List.....
        list_frame = tk.Frame(label_frame, padx=10, pady=10, bg=None)
        list_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(list_frame, selectmode='browse')
        self.tree.pack(side=LEFT, fill=BOTH)


        verscrlbar = ttk.Scrollbar(list_frame,orient="vertical",command=self.tree.yview)
        verscrlbar.pack(side=RIGHT, fill=BOTH, expand=True)
        self.tree.configure(xscrollcommand=verscrlbar.set)

        self.tree["columns"] = ("1", "2", "3", "4")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=60, anchor='w')
        self.tree.column("2", width=150, anchor='w')
        self.tree.column("3", width=90, anchor='w')
        self.tree.column("4", width=150, anchor='w')


        self.tree.heading("1", text="No")
        self.tree.heading("2", text="Name")
        self.tree.heading("3", text="Mobile")
        self.tree.heading("4", text="Email")
        self.tree.bind('<ButtonRelease-1>', self.selectCustomer)

        CustomerController.customerShow(self)

    def selectCustomer(self,event):
        items = self.tree.focus()
        item  = self.tree.item(items)
        if items:
            self.cID.set(item['values'][0])
            self.cName.set(item['values'][1])
            self.cMobile.set("0"+str(item['values'][2]))
            self.cEmail.set(item['values'][3])








