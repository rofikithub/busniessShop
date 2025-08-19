import json
import tkinter as tk
import webbrowser
from controller.JsonController import JsonController
from controller.LoginController import LoginController


class loginView:
    def __init__(self, root):
        
        self.bg = JsonController.bgColor(self)
        self.fg = JsonController.fgColor(self)
        
        self.root = root
        self.root.title('Login')
        self.root.protocol('WM_DELETE_WINDOW', root.quit)
        self.root.geometry(f'400x360+500+100')
        self.root.resizable(False, False)
        self.root.iconbitmap(r'image\winico.ico')
        self.root.configure(background=self.bg)


        def goLink(event):
                webbrowser.open_new('https://rofikit.com/registration')
        
        self.canvas = tk.Frame(self.root, background=self.bg)
        self.canvas.pack(fill='both', anchor='center', padx=20, pady=20)
        
        frame = tk.Frame(self.canvas, background=self.bg)
        frame.pack(side='top')
        
        title_frame = tk.Frame(frame, background=self.bg)
        title_frame.pack(side='top')
        title_label = tk.Label(title_frame, text="Softwer Login", font=('Bahnschrift SemiBold Condensed', 18), background=self.bg, fg=self.fg)
        title_label.pack(fill='both', pady=20)
        
        mobile_frame = tk.Frame(frame, background=self.bg)
        mobile_frame.pack(side='top', pady=10)
        mobile_label = tk.Label(mobile_frame, text='Mobile No', width=12, font=('Bahnschrift SemiBold Condensed',13), background=self.bg, fg=self.fg)
        mobile_label.pack(side='left', anchor='w')
        self.mobile_entry = tk.Entry(mobile_frame, width=25)
        self.mobile_entry.pack(side='left',ipady=2)
        
        password_frame = tk.Frame(frame, background=self.bg)
        password_frame.pack(side='top', pady=10)
        password_label = tk.Label(password_frame, text='Password', width=12, font=('Bahnschrift SemiBold Condensed',13), background=self.bg, fg=self.fg)
        password_label.pack(side='left', anchor='w')
        self.password_entry = tk.Entry(password_frame, show="*", width=25)
        self.password_entry.pack(side='left',ipady=2)
        
        button_frame = tk.Frame(frame, background=self.bg)
        button_frame.pack(side='top', fill='both', anchor='center', pady=35)
        login_button = tk.Button(button_frame, text='Login', command=lambda:LoginController.loginAction(self), width=15, cursor="hand2", font=('Bahnschrift SemiBold Condensed', 10), border=0.5)
        login_button.pack(anchor='center')
        
        link_frame = tk.Frame(frame, background=self.bg)
        link_frame.pack(side='top', fill='both', anchor='s', pady=20)
        link_label = tk.Label(link_frame, text='Create a new account', cursor="hand2", background=self.bg, fg=self.fg)
        link_label.pack(side='bottom',anchor='s')
        link_label.bind("<Button-1>", goLink)

        self.mobile_entry.insert(0,"01737034338")
        self.password_entry.insert(0,"180825")

