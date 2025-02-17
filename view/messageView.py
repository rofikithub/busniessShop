import math
import tkinter as tk
from datetime import date, datetime, timedelta
import webbrowser
from datetime import date
from view.dashboardView import dashboardView
from view import loginView


class messageView:
    def __init__(self,root,data):
        self.root = root
        self.root.title('Notification')
        self.root.protocol('WM_DELETE_WINDOW', root.quit)
        self.root.geometry(f'400x300+500+100')
        self.root.resizable(False, False)
        self.root.iconbitmap(r'image\email.ico')
        
        self.version = "1.0.0"


        def updateVersion(event):
            webbrowser.open_new('https://rofikit.com/')
            self.root.destroy()
            loginView.loginView(tk.Tk())

        

        fram = tk.Frame(self.root)
        fram.pack(side='top', fill='both')

        sms_label = tk.Label(fram, text='Hello\n'+str(data["name"])+'\n Welcome to '+str(data["softwar"]), fg='#555', font=("Bahnschrift SemiBold Condensed", 12))
        sms_label.pack(side='top', fill='x', padx=20, pady=40, anchor='w')

        if data["status"] == '1':
            link_label = tk.Label(fram, text='Please wait until your payment is confirmed', fg='#555', cursor="hand2", font=("Bahnschrift SemiBold Condensed", 10))
            link_label.pack(side='top', anchor='center')

            
        if self.version != data["version"]:
            link_label = tk.Label(fram, text='New version '+str(data["version"])+' is available, Click for Download', fg='#555', cursor="hand2", font=("Bahnschrift SemiBold Condensed", 10))
            link_label.pack(side='top', anchor='center')
            link_label.bind("<Button-1>", updateVersion)
        
        if data["status"] == '3':
            link_label = tk.Label(fram, text='The package expired on '+str(data["end"]), fg='red', font=('Bahnschrift SemiBold Condensed', 9))
            link_label.pack(side='top', anchor='center')
        else:
            link_label = tk.Label(fram, text='The package will expire on '+str(data["end"]), fg='#777', font=('Bahnschrift SemiBold Condensed', 9))
            link_label.pack(side='top', anchor='center')
        
        e = date.fromisoformat(data["end"])
        end = datetime(e.year, e.month, e.day)
        end = end.timestamp()
        end = math.ceil(end)

        t = datetime.today()
        today = datetime(t.year, t.month, t.day)
        today = today.timestamp()
        today = math.ceil(today)

        if today > end:
            button = tk.Button(fram, text="Renew Payment", command=self.packageRenew, width=15, cursor="hand2", font=('Arial', 10), border=0.5)
            button.pack(side='top', fill='none', padx=10, pady=40, anchor='s')
        elif data["status"] == '3':
            button = tk.Button(fram, text="Renew Payment", command=self.packageRenew, width=15, cursor="hand2", font=('Arial', 10), border=0.5)
            button.pack(side='top', fill='none', padx=10, pady=40, anchor='s')
        elif data["status"] == '1':
            button = tk.Button(fram, text="View Invoice", command=self.viewInvoice, width=15, cursor="hand2", font=('Arial', 10), border=0.5)
            button.pack(side='top', fill='none', padx=10, pady=40, anchor='s')
        elif data["status"] == '2':
            button = tk.Button(fram, text="Dashboard", command=self.nextAction, width=15, cursor="hand2", font=('Arial', 10), border=0.5)
            button.pack(side='top', fill='none', padx=10, pady=40, anchor='s')
            
    def viewInvoice(self):
        webbrowser.open_new('https://rofikit.com/')
        self.root.destroy()
        loginView.loginView(tk.Tk())   
            
    def packageRenew(self):
        webbrowser.open_new('https://rofikit.com/')
        self.root.destroy()
        loginView.loginView(tk.Tk())

    def nextAction(self):
        self.root.destroy()
        dashboardView(tk.Tk())

