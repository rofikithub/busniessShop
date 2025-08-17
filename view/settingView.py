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
                
        def thisBackground(event):
            bg = None
            color = self.background_box.get()
            if color=='Default':
                bg=("#eeeeee")
            else:
                bg=(color)
            SettingController.updateJsonFile(self,"backgroundColor",bg)
            SettingController.getSettingBackground(self)

        self.bg = SettingController.bgColor(self)
        self.fg = SettingController.fgColor(self)
        
        # Shop Details Update
        self.satting_frame = tk.Frame(root, padx=20, pady=20, background=self.bg)
        self.satting_frame.pack(fill=tk.BOTH, expand=True, side=TOP)

        self.setting_label_frame = tk.LabelFrame(self.satting_frame, text="Shop information", padx=10, pady=10, background=self.bg, fg=self.fg)
        self.setting_label_frame.pack(fill=tk.BOTH, side=TOP)

        self.name_frame = tk.Frame(self.setting_label_frame, padx=10, pady=5, background=self.bg)
        self.name_frame.pack(side=TOP)
        self.shop_name_label = tk.Label(self.name_frame, text="Shop Name        ", background=self.bg, fg=self.fg)
        self.shop_name_label.pack(side=LEFT)
        self.shop_name_entry = tk.Entry(self.name_frame, textvariable=self.sname, width=40, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_name_entry.pack(side=LEFT)


        self.address_frame = tk.Frame(self.setting_label_frame, padx=10, pady=5, background=self.bg)
        self.address_frame.pack(side=TOP)
        self.address_label = tk.Label(self.address_frame, text="Shop Address     ", background=self.bg, fg=self.fg)
        self.address_label.pack(side=LEFT)
        self.shop_address_entry = tk.Entry(self.address_frame, textvariable=self.address, width=40, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_address_entry.pack(side=LEFT)

        self.number_frame = tk.Frame(self.setting_label_frame, padx=10, pady=5, background=self.bg)
        self.number_frame.pack(side=TOP)
        self.numbe_label = tk.Label(self.number_frame, text="Mobile Number ", background=self.bg, fg=self.fg)
        self.numbe_label.pack(side=LEFT)
        self.shop_mobile_entry = tk.Entry(self.number_frame, textvariable=self.mobile, width=40, font=("Arial", 9), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_mobile_entry.pack(side=LEFT)


        self.update_btn_frame = tk.Frame(self.setting_label_frame, padx=5, pady=10, background=self.bg)
        self.update_btn_frame.pack(fill=tk.BOTH, side=TOP)
        self.save_btn = tk.Button(self.update_btn_frame, text="Save", command= lambda: SettingController.createShop(self), padx=30, bg="#A2C579", fg="black", border=0.5)
        self.save_btn.pack(side=TOP)

        SettingController.showUpdate(self)


        self.bg_LabelFrame = tk.LabelFrame(self.satting_frame, text="Windows Background", padx=10, pady=10, background=self.bg, fg=self.fg)
        self.bg_LabelFrame.pack(fill=tk.BOTH, side=TOP)
        
        self.background_frame = tk.Frame(self.bg_LabelFrame, padx=10, pady=5, background=self.bg)
        self.background_frame.pack(side=TOP)
        self.background_label = tk.Label(self.background_frame, text="Select Color", pady=10, padx=20, background=self.bg, fg=self.fg)
        self.background_label.pack(side='left')

        self.background_box = ttk.Combobox(self.background_frame, values=['Default','White', 'Red', 'Black', 'Green','Yellow'], state="readonly", width=17, background='white')
        self.background_box.pack(side='left')
        self.background_box.bind('<<ComboboxSelected>>', thisBackground)  

        if self.bg:
            if self.bg=="#eeeeee":
                self.background_box.set("Default")
            else:
                self.background_box.set(self.bg)
        else:
            self.background_box.set(".. Windows Color ..")
            
        go_back_label = tk.Label(self.satting_frame, text='Go back', borderwidth=0, relief="groove", bg="#176B87", fg="white", padx=20, cursor='hand2')
        go_back_label.pack(side='bottom')
        go_back_label.bind("<Button-1>", backDeshboard)
        
        