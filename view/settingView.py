import json
import tkinter as tk
from tkinter import TOP, LEFT, ttk, BOTH
from tkinter import colorchooser
from PIL import ImageTk, Image
from PIL.ImageChops import screen
from model.Category import Category
from view import dashboardView
from controller.SettingController import SettingController


class settingView:

    def __init__(self, root):
        
        self.root = root
        root.title("Setting")
        ww = 800
        wh = 600
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(50)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        root.resizable(False, False)

        self.sname   = tk.StringVar()
        self.address = tk.StringVar()
        self.mobile  = tk.StringVar()

        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())
            
        def choose_background():
            color_code = colorchooser.askcolor(title ="Choose color")
            with open("./system.json", "r") as file:
                data = json.load(file)
                data["backgroundColor"]= color_code[1]
            with open("./system.json", "w") as file:
                json.dump(data, file, indent=1)

        satting_frame = tk.Frame(root, padx=40, pady=10)
        satting_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        setting_label_frame = tk.LabelFrame(satting_frame, text="Shop information", padx=5, pady=5)
        setting_label_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        name_frame = tk.Frame(setting_label_frame, padx=10, pady=5)
        name_frame.pack(side=TOP)
        shop_name_label = tk.Label(name_frame, text="Shop Name        ")
        shop_name_label.pack(side=LEFT)
        self.shop_name_entry = tk.Entry(name_frame, textvariable=self.sname, width=40, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_name_entry.pack(side=LEFT)


        name_frame = tk.Frame(setting_label_frame, padx=10, pady=5)
        name_frame.pack(side=TOP)
        shop_name_label = tk.Label(name_frame, text="Shop Address     ")
        shop_name_label.pack(side=LEFT)
        self.shop_address_entry = tk.Entry(name_frame, textvariable=self.address, width=40, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_address_entry.pack(side=LEFT)

        name_frame = tk.Frame(setting_label_frame, padx=10, pady=5)
        name_frame.pack(side=TOP)
        shop_name_label = tk.Label(name_frame, text="Mobile Number ")
        shop_name_label.pack(side=LEFT)
        self.shop_mobile_entry = tk.Entry(name_frame, textvariable=self.mobile, width=40, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_mobile_entry.pack(side=LEFT)


        btn_frame = tk.Frame(setting_label_frame, padx=10, pady=5)
        btn_frame.pack(fill=tk.BOTH, side=TOP)
        new_product_save_btn = tk.Button(btn_frame, text="Save", command= lambda: SettingController.createShop(self), padx=30, bg="#A2C579", fg="black", border=0.5)
        new_product_save_btn.pack(side=TOP)

        SettingController.showUpdate(self)


        self.bg_color_frame = tk.LabelFrame(satting_frame, text="Windows Background Color", padx=5, pady=5)
        self.bg_color_frame.pack(fill=tk.BOTH, expand=True, side=TOP)
        
        bill_number_label = tk.Label(self.bg_color_frame, text="Select Background Color", pady=2, padx=20)
        bill_number_label.pack(side='left')
        bill_number_search = tk.Button(self.bg_color_frame,text="Search", command=choose_background, padx=20, bg="#ddd", fg="black", font=("Arial", 9), border=0.5)
        bill_number_search.pack(side='left')
        
        go_back_label = tk.Label(satting_frame, text='Go back', borderwidth=0, relief="groove", bg="#176B87", fg="white", padx=20, cursor='hand2')
        go_back_label.pack(side='bottom')
        go_back_label.bind("<Button-1>", backDeshboard)
        
        