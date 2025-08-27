import os
import tkinter as tk
from tkinter import BOTTOM, TOP, LEFT, ttk, BOTH
from tkinter import filedialog
import webbrowser
from controller.DriveController import DriveController
from controller.JsonController import JsonController
from view import dashboardView
from controller.SettingController import SettingController


class settingView:

    def __init__(self, root):
        
        self.bg = JsonController.bgColor(self)
        self.fg = JsonController.fgColor(self)
        
        self.root = root
        root.title("Configaretion Satting")
        ww = 850
        wh = 600
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(50)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        root.resizable(False, False)
        self.root.iconbitmap(os.path.join(os.getcwd(), "image", "winico.ico"))
        self.root.configure(background=self.bg)

        self.snam     = tk.StringVar()
        self.sadd     = tk.StringVar()
        self.snum     = tk.StringVar()
        self.userMail = tk.StringVar()
        self.userPass = tk.StringVar()
        self.token    = tk.StringVar()
        self.client   = tk.StringVar()
        self.database = tk.StringVar()
        self.system = tk.StringVar()
        
        SettingController.showShop(self)
        self.userMail.set(JsonController.getJson(self,'userMail'))
        self.userPass.set(JsonController.getJson(self,'userPass'))
        self.token.set(JsonController.getJson(self,'greenwebToken'))

        def backupDatabase(event):
            self.database.set(filedialog.askopenfilename(title="Select File", filetypes=[("DB","*.db")]))

        def clientSecrets(event):
            self.client.set(filedialog.askopenfilename(title="Select File", filetypes=[("JSON","*.json")]))

        def systemJson(event):
            self.system.set(filedialog.askopenfilename(title="Select File", filetypes=[("JSON","*.json")]))

        def backDeshboard(event):
            self.root.destroy()
            dashboardView.dashboardView(tk.Tk())
                
        def thisBackground(event):
            bg = None
            color = self.background_box.get()
            if color=='Default':
                bg=("#eeeeee")
            else:
                bg=(color)
            JsonController.updateJson(self,"backgroundColor",bg,0)
            SettingController.getSettingBackground(self)

        
        def goGmail(event):
                webbrowser.open_new('https://myaccount.google.com/apppasswords')
        def goGreenweb(event):
                webbrowser.open_new('https://sms.greenweb.com.bd/index.php?ref=gen_token.php')   
                
        def on_mouse_wheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        def on_mouse_wheel_mac(event):
            if event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")   
                
        
        self.satting_frame = tk.Frame(root, padx=10, pady=10, background=self.bg)
        self.satting_frame.pack(side=TOP, fill=tk.BOTH, expand = True)
        
        
        # ===== Scrollable Frame Setup =====
        canvas = tk.Canvas(self.satting_frame, background=self.bg)
        scrollbar = ttk.Scrollbar(self.satting_frame, orient="vertical", command=canvas.yview)
        self.scroll_frame = tk.Frame(canvas, padx=10, pady=10, background=self.bg)

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.configure(highlightthickness=0, highlightbackground = "#F9F9F9")
        
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)
        canvas.bind_all("<Button-4>", on_mouse_wheel_mac)
        canvas.bind_all("<Button-5>", on_mouse_wheel_mac)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # >>> Shop information <<<
        self.info_frame = tk.Frame(self.scroll_frame, padx=10, pady=10, background=self.bg)
        self.info_frame.pack(side=TOP, fill=tk.BOTH, expand = True)
        
        self.setting_label_frame = tk.LabelFrame(self.info_frame, text="Shop information", padx=5, pady=5, background=self.bg, fg=self.fg)
        self.setting_label_frame.pack(side=TOP, fill=tk.BOTH, expand = True)

        self.name_frame = tk.Frame(self.setting_label_frame, padx=10, pady=5, background=self.bg)
        self.name_frame.pack(side=TOP)
        self.shop_name_label = tk.Label(self.name_frame, text="Shop Name        ", background=self.bg, fg=self.fg)
        self.shop_name_label.pack(side=LEFT)
        self.shop_name_entry = tk.Entry(self.name_frame, textvariable=self.snam, width=40, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_name_entry.pack(side=LEFT)


        self.address_frame = tk.Frame(self.setting_label_frame, padx=10, pady=5, background=self.bg)
        self.address_frame.pack(side=TOP)
        self.address_label = tk.Label(self.address_frame, text="Shop Address     ", background=self.bg, fg=self.fg)
        self.address_label.pack(side=LEFT)
        self.shop_address_entry = tk.Entry(self.address_frame, textvariable=self.sadd, width=40, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_address_entry.pack(side=LEFT)

        self.number_frame = tk.Frame(self.setting_label_frame, padx=10, pady=5, background=self.bg)
        self.number_frame.pack(side=TOP)
        self.numbe_label = tk.Label(self.number_frame, text="Mobile Number ", background=self.bg, fg=self.fg)
        self.numbe_label.pack(side=LEFT)
        self.shop_mobile_entry = tk.Entry(self.number_frame, textvariable=self.snum, width=40, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.shop_mobile_entry.pack(side=LEFT)


        self.update_btn_frame = tk.Frame(self.setting_label_frame, padx=5, pady=10, background=self.bg)
        self.update_btn_frame.pack(fill=tk.BOTH, side=TOP)
        self.save_btn = tk.Button(self.update_btn_frame, text="Save", command= lambda: SettingController.createShop(self), padx=30, bg="#A2C579", fg="black", border=0, relief="flat", cursor='hand2')
        self.save_btn.pack(side=TOP)

        # >>> Windows Background <<<
        self.bg_frame = tk.Frame(self.scroll_frame, padx=10, pady=10, background=self.bg)
        self.bg_frame.pack(side=TOP, fill=tk.BOTH, expand = True)
        
        self.bg_LabelFrame = tk.LabelFrame(self.bg_frame, text="Windows Background", padx=5, pady=5, background=self.bg, fg=self.fg)
        self.bg_LabelFrame.pack(side=TOP, fill=tk.BOTH, expand = True)
        
        self.background_frame = tk.Frame(self.bg_LabelFrame, padx=10, pady=5, background=self.bg)
        self.background_frame.pack(side=TOP)
        self.background_label = tk.Label(self.background_frame, text="Select Color", pady=10, padx=20, background=self.bg, fg=self.fg)
        self.background_label.pack(side='left')

        self.background_box = ttk.Combobox(self.background_frame, values=['Default','White', 'Red', 'Black', 'Green','Yellow'], state="readonly", width=25, background='white')
        self.background_box.pack(side='left')
        self.background_box.bind('<<ComboboxSelected>>', thisBackground)  

        if self.bg:
            if self.bg=="#eeeeee":
                self.background_box.set("Default")
            else:
                self.background_box.set(self.bg)
        else:
            self.background_box.set(".. Windows Color ..")
            
            
        # >>> Gmail Configuration <<<
        self.gmail_frame = tk.Frame(self.scroll_frame, padx=10, pady=10, background=self.bg)
        self.gmail_frame.pack(side=TOP, fill=tk.BOTH, expand = True)
        
        self.mail_LabelFrame = tk.LabelFrame(self.gmail_frame, text="Gmail Configuration", padx=25, pady=10, background=self.bg, fg=self.fg)
        self.mail_LabelFrame.pack(side=TOP, fill=tk.BOTH, expand = True)
        
        self.mailinfo_frame = tk.Frame(self.mail_LabelFrame, background=self.bg)
        self.mailinfo_frame.pack(side=TOP)
        
        self.mailAdd_frame = tk.Frame(self.mailinfo_frame, padx=5, pady=5, background=self.bg)
        self.mailAdd_frame.pack(side=LEFT)
        self.usermail_label = tk.Label(self.mailAdd_frame, text="Gmail Address  ", pady=10, padx=10, background=self.bg, fg=self.fg)
        self.usermail_label.pack(side='left')
        self.usermail_entry = tk.Entry(self.mailAdd_frame, textvariable=self.userMail, width=25, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.usermail_entry.pack(side=LEFT)
        
        self.mailPass_frame = tk.Frame(self.mailinfo_frame, padx=5, pady=5, background=self.bg)
        self.mailPass_frame.pack(side=LEFT)
        self.mailPass_label = tk.Label(self.mailPass_frame, text="App Password  ", pady=10, padx=10, background=self.bg, fg=self.fg)
        self.mailPass_label.pack(side='left')
        self.mailPass_entry = tk.Entry(self.mailPass_frame, textvariable=self.userPass, width=25, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.mailPass_entry.pack(side=LEFT)
        
        self.mailSave_frame = tk.Frame(self.mailinfo_frame, padx=5, pady=5, background=self.bg)
        self.mailSave_frame.pack(side=LEFT)
        self.mail_Save_btn = tk.Button(self.mailSave_frame, command=lambda:JsonController.updateConfiguration(self), text="Save", padx=30, bg="#A2C579", fg="black", border=0, relief="flat", cursor='hand2')
        self.mail_Save_btn.pack(side=LEFT)
        
        self.passNote_frame = tk.Frame(self.mail_LabelFrame, background=self.bg)
        self.passNote_frame.pack(side=BOTTOM, anchor='s')
        self.passwordApp_label1 = tk.Label(self.passNote_frame, text="Login google account in your browser. Go to this link", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.passwordApp_label1.pack(side=LEFT)
        self.passwordApp_label2 = tk.Label(self.passNote_frame, text="https://myaccount.google.com", font=("Arial", 8,"underline"), cursor='hand2', background=self.bg, fg=self.fg)
        self.passwordApp_label2.pack(side=LEFT)
        self.passwordApp_label2.bind("<Button-1>", goGmail)
        self.passwordApp_label3 = tk.Label(self.passNote_frame, text=".To create a new app specific password.", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.passwordApp_label3.pack(side=LEFT)
            
            
        # >>> SMS Configuration of Greenweb <<<   
        self.massage_frame = tk.Frame(self.scroll_frame, padx=10, pady=10, background=self.bg)
        self.massage_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.sms_LabelFrame = tk.LabelFrame(self.massage_frame, text="SMS Configuration of Greenweb", padx=20, pady=10, background=self.bg, fg=self.fg)
        self.sms_LabelFrame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.sms_frame = tk.Frame(self.sms_LabelFrame, background=self.bg)
        self.sms_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.token_frame = tk.Frame(self.sms_frame, padx=5, pady=5, background=self.bg)
        self.token_frame.pack(side=TOP)
        self.token_label = tk.Label(self.token_frame, text="Api_Key or Token  ", pady=15, padx=5, background=self.bg, fg=self.fg)
        self.token_label.pack(side=LEFT)
        self.token_entry = tk.Entry(self.token_frame, textvariable=self.token, width=69, font=("Arial", 10), border=0, highlightthickness=1,highlightbackground = "#ddd")
        self.token_entry.pack(side=LEFT)
        self.stoken_frame = tk.Frame(self.token_frame, padx=10, pady=5, background=self.bg)
        self.stoken_frame.pack(side=LEFT)
        self.stoken_btn = tk.Button(self.stoken_frame, command=lambda:JsonController.updateToken(self), text="Save Token", padx=15, bg="#A2C579", fg="black", border=0, relief="flat", cursor='hand2')
        self.stoken_btn.pack(side=LEFT)
        
        self.greenweb_frame = tk.Frame(self.sms_frame, background=self.bg)
        self.greenweb_frame.pack(side=BOTTOM, anchor='s')
        self.smsnote_label1 = tk.Label(self.greenweb_frame, text="Create a account for buy sms service. Go to this link", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.smsnote_label1.pack(side=LEFT)
        self.smsnote_label2 = tk.Label(self.greenweb_frame, text="https://sms.greenweb.com.bd", font=("Arial", 8,"underline"), cursor='hand2', background=self.bg, fg=self.fg)
        self.smsnote_label2.pack(side=LEFT)
        self.smsnote_label2.bind("<Button-1>", goGreenweb)
        self.smsnote_label3 = tk.Label(self.greenweb_frame, text=".To create a new api token.", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.smsnote_label3.pack(side=LEFT)  
         
            
        # >>> Google Drive Configuration <<<   
        self.drive_frame = tk.Frame(self.scroll_frame, padx=10, pady=10, background=self.bg)
        self.drive_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.drive_LabelFrame = tk.LabelFrame(self.drive_frame, text="Google Drive Configuration File", padx=20, pady=10, background=self.bg, fg=self.fg)
        self.drive_LabelFrame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.driver_frame = tk.Frame(self.drive_LabelFrame, background=self.bg)
        self.driver_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.gdrive_frame = tk.Frame(self.driver_frame, padx=5, pady=5, background=self.bg)
        self.gdrive_frame.pack(side=TOP)
        self.gdrive_label = tk.Label(self.gdrive_frame, text="Browse client_secrets.json File",  padx=15, pady=2, font=("Arial", 8), background="#999999", cursor='hand2')
        self.gdrive_label.pack(side=LEFT)
        self.gdrive_label.bind("<Button-1>", clientSecrets)
        self.gdrive_entry = tk.Entry(self.gdrive_frame, textvariable=self.client, width=45, font=5, border=0, highlightthickness=1,highlightbackground = "#ddd", state='readonly')
        self.gdrive_entry.pack(side=LEFT)
        self.driveg_frame = tk.Frame(self.gdrive_frame, padx=10, pady=5, background=self.bg)
        self.driveg_frame.pack(side=LEFT)
        self.driveg_btn = tk.Button(self.driveg_frame, command=lambda:DriveController.uploadClient(self), text="Upload", padx=30, bg="#A2C579", fg="black", border=0, relief="flat", cursor='hand2')
        self.driveg_btn.pack(side=LEFT)
        
        self.drivenot_frame = tk.Frame(self.driver_frame, background=self.bg)
        self.drivenot_frame.pack(side=BOTTOM, anchor='s')
        self.gdnote_label1 = tk.Label(self.drivenot_frame, text="Create a account for buy sms service. Go to this link", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.gdnote_label1.pack(side=LEFT)
        self.gdnote_label2 = tk.Label(self.drivenot_frame, text="https://sms.greenweb.com.bd", font=("Arial", 8,"underline"), cursor='hand2', background=self.bg, fg=self.fg)
        self.gdnote_label2.pack(side=LEFT)
        self.gdnote_label2.bind("<Button-1>", goGreenweb)
        self.gdnote_label3 = tk.Label(self.drivenot_frame, text=".To create a new api token.", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.gdnote_label3.pack(side=LEFT)  

       
        # >>> Database Backup File Upload <<<   
        self.dbfile_frame = tk.Frame(self.scroll_frame, padx=10, pady=10, background=self.bg)
        self.dbfile_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.dbfile_LabelFrame = tk.LabelFrame(self.dbfile_frame, text="Database Backup File Upload", padx=20, pady=10, background=self.bg, fg=self.fg)
        self.dbfile_LabelFrame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.database_frame = tk.Frame(self.dbfile_LabelFrame, background=self.bg)
        self.database_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.dbf_frame = tk.Frame(self.database_frame, padx=5, pady=5, background=self.bg)
        self.dbf_frame.pack(side=TOP)
        self.dbf_label = tk.Label(self.dbf_frame, text="Browse bms_database.db File",  padx=15, pady=2, font=("Arial", 8), background="#999999", cursor='hand2')
        self.dbf_label.pack(side=LEFT)
        self.dbf_label.bind("<Button-1>", backupDatabase)
        self.dbf_entry = tk.Entry(self.dbf_frame, textvariable=self.database, width=45, font=5, border=0, highlightthickness=1,highlightbackground = "#ddd", state='readonly')
        self.dbf_entry.pack(side=LEFT)
        self.bdfile_frame = tk.Frame(self.dbf_frame, padx=10, pady=5, background=self.bg)
        self.bdfile_frame.pack(side=LEFT)
        self.dbfile_btn = tk.Button(self.bdfile_frame, command=lambda:DriveController.uploadDatabase(self), text="Upload", padx=30, bg="#A2C579", fg="black", border=0, relief="flat", cursor='hand2')
        self.dbfile_btn.pack(side=LEFT)
        
        self.dbnote_frame = tk.Frame(self.database_frame, background=self.bg)
        self.dbnote_frame.pack(side=BOTTOM, anchor='s')
        self.dbnote_label1 = tk.Label(self.dbnote_frame, text="Create a account for buy sms service. Go to this link", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.dbnote_label1.pack(side=LEFT)
        self.dbnote_label2 = tk.Label(self.dbnote_frame, text="https://sms.greenweb.com.bd", font=("Arial", 8,"underline"), cursor='hand2', background=self.bg, fg=self.fg)
        self.dbnote_label2.pack(side=LEFT)
        self.dbnote_label2.bind("<Button-1>", goGreenweb)
        self.dbnote_label3 = tk.Label(self.dbnote_frame, text=".To create a new api token.", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.dbnote_label3.pack(side=LEFT)  

       
        # >>> Upload System Json File <<<   
        self.sjson_frame = tk.Frame(self.scroll_frame, padx=10, pady=10, background=self.bg)
        self.sjson_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.sjson_LabelFrame = tk.LabelFrame(self.sjson_frame, text="Softwere System File Upload", padx=20, pady=10, background=self.bg, fg=self.fg)
        self.sjson_LabelFrame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.system_frame = tk.Frame(self.sjson_LabelFrame, background=self.bg)
        self.system_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.sjfile_frame = tk.Frame(self.system_frame, padx=5, pady=5, background=self.bg)
        self.sjfile_frame.pack(side=TOP)
        self.sjfile_label = tk.Label(self.sjfile_frame, text="Browse system.json File",  padx=15, pady=2, font=("Arial", 8), background="#999999", cursor='hand2')
        self.sjfile_label.pack(side=LEFT)
        self.sjfile_label.bind("<Button-1>", systemJson)
        self.sjfile_entry = tk.Entry(self.sjfile_frame, textvariable=self.system, width=49, font=5, border=0, highlightthickness=1,highlightbackground = "#ddd", state='readonly')
        self.sjfile_entry.pack(side=LEFT)
        self.sjsonf_frame = tk.Frame(self.sjfile_frame, padx=10, pady=5, background=self.bg)
        self.sjsonf_frame.pack(side=LEFT)
        self.sjfile_btn = tk.Button(self.sjsonf_frame, command=lambda:DriveController.uploadSystemJson(self), text="Upload", padx=30, bg="#A2C579", fg="black", border=0, relief="flat", cursor='hand2')
        self.sjfile_btn.pack(side=LEFT)
        
        self.sysnot_frame = tk.Frame(self.system_frame, background=self.bg)
        self.sysnot_frame.pack(side=BOTTOM, anchor='s')
        self.sysnote_label1 = tk.Label(self.sysnot_frame, text="Create a account for buy sms service. Go to this link", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.sysnote_label1.pack(side=LEFT)
        self.sysnote_label2 = tk.Label(self.sysnot_frame, text="https://sms.greenweb.com.bd", font=("Arial", 8,"underline"), cursor='hand2', background=self.bg, fg=self.fg)
        self.sysnote_label2.pack(side=LEFT)
        self.sysnote_label2.bind("<Button-1>", goGreenweb)
        self.sysnote_label3 = tk.Label(self.sysnot_frame, text=".To create a new api token.", font=("Arial", 8), background=self.bg, fg=self.fg)
        self.sysnote_label3.pack(side=LEFT)  
            
            
        self.back_frame = tk.Frame(root, padx=10, pady=10, background=self.bg)
        self.back_frame.pack(side=BOTTOM)
        go_back_label = tk.Label(self.back_frame, text='Go back', borderwidth=0, relief="groove", bg="#176B87", fg="white", padx=20, cursor='hand2')
        go_back_label.pack(side=BOTTOM, anchor='s')
        go_back_label.bind("<Button-1>", backDeshboard)
        
        