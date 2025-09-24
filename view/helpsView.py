import json
import os
import tkinter as tk
from tkinter import BOTTOM, TOP, LEFT, ttk, BOTH
from tkinter import colorchooser
import webbrowser
from controller.JsonController import JsonController
from view import dashboardView
from controller.SettingController import SettingController


class helpsView:

    def __init__(self, root):
        
        self.root = root
        root.title("Help Window")
        ww = 800
        wh = 600
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        c_x = int(sw / 2 - ww / 2)
        c_y = int(50)
        root.geometry(f'{ww}x{wh}+{c_x}+{c_y}')
        root.resizable(False, False)
        self.root.iconbitmap(os.path.join(os.getcwd(), "image", "winico.ico"))

        def on_mouse_wheel(event):
            # Windows Linux
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        def on_mouse_wheel_mac(event):
            # macOS
            if event.num == 4:   # Scroll Up
                canvas.yview_scroll(-1, "units")
            elif event.num == 5: # Scroll Down
                canvas.yview_scroll(1, "units")          
                
        def thisBackground(event):
            bg = None
            color = self.background_box.get()
            if color=='Default':
                bg=("#eeeeee")
            else:
                bg=(color)
            JsonController.updateJson(self,"backgroundColor",bg,0)
            SettingController.getSettingBackground(self)

        self.bg = JsonController.bgColor(self)
        self.fg = JsonController.fgColor(self)
        
        def goGmail(event):
                webbrowser.open_new('https://myaccount.google.com/apppasswords')
        def goGreenweb(event):
                webbrowser.open_new('https://sms.greenweb.com.bd/index.php?ref=gen_token.php')   

        
        self.help_frame = tk.Frame(root, padx=30, pady=20, background=self.bg)
        self.help_frame.pack(side=TOP,fill=tk.BOTH, expand=True)
        
        
        # ===== Scrollable Frame Setup =====
        canvas = tk.Canvas(self.help_frame, background=self.bg)
        scrollbar = ttk.Scrollbar(self.help_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, padx=30, pady=10, background=self.bg)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.configure(highlightthickness=0, highlightbackground = "#F9F9F9")
        
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)
        canvas.bind_all("<Button-4>", on_mouse_wheel_mac)
        canvas.bind_all("<Button-5>", on_mouse_wheel_mac)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ===== Help Topics with Sections =====
        help_data = {
            "লগইন নির্দেশনা": [
                "ইউজারনেম এবং পাসওয়ার্ড দিয়ে লগইন করুন।",
                "ভুল পাসওয়ার্ড দিলে সতর্কবার্তা দেখানো হবে।"
            ],
            "ডিলার ম্যানেজমেন্ট": [
                "Dealer মেনু ব্যবহার করুন।",
                "Save বাটনে ক্লিক করে নতুন ডিলার যোগ করুন।",
                "তথ্য আপডেট করতে ডিলারের লিষ্টে ক্লিক করে Update বাটন চাপুন।",
                "ডিলারের তথ্য ডিলিট করতে লিষ্টে ক্লিক করে Delete বাটন চাপুন।"
            ],
            "প্রোডাক্ট ক্যাটেগরি": [
                "প্রোডাক্ট শ্রেণীবিন্যাস করতে ক্যাটেগরি যোগ করুন।",
                "প্রতিটি প্রোডাক্টকে অবশ্যই একটি ক্যাটেগরির সাথে যুক্ত করুন।",
                "ক্যাটেগরি দিয়ে রিপোর্ট এবং সার্চ সহজ হবে।"
            ],
            "প্রোডাক্ট ম্যানেজমেন্ট": [
                "নতুন প্রোডাক্ট যোগ করতে Product মেনু ব্যবহার করুন।",
                "প্রোডাক্টের ক্যাটেগরি, নাম, ক্রয় ও বিক্রয় মূল্য সঠিকভাবে দিন।",
                "স্টক ম্যানেজমেন্টের জন্য প্রোডাক্ট আপডেট রাখুন।",
                "QR কোড প্রিন্ট করার জন্য প্রোডাক্ট সিলেক্ট করে Print QR Code বাটন চাপুন।"
            ],
            "কাস্টমার ম্যানেজমেন্ট": [
                "Customer মেনু ব্যবহার করুন।",
                "Save বাটনে ক্লিক করে নতুন কাস্টমার যোগ করুন।",
                "কাস্টমারের তথ্য আপডেট করতে Update বাটন চাপুন।"
            ],
            "রিপোর্ট সেকশন": [
                "রিপোর্ট দেখতে Sale মেনু ব্যবহার করুন।",
                "তারিখ অনুযায়ী রিপোর্ট ফিল্টার করা যায়।",
                "রিপোর্ট প্রিন্ট করার জন্য All list print বাটন ব্যবহার করুন।",
                "বকেয়া রিপোর্ট প্রিন্ট করার জন্য All Due print বাটন ব্যবহার করুন।"
            ],
            "প্রোডাক্ট ফেরত": [
                "কাস্টমার থেকে ফেরত আসা প্রোডাক্ট 'Return' মডিউলে এন্ট্রি করুন।",
                "স্টক এডজাস্টমেন্ট স্বয়ংক্রিয়ভাবে আপডেট হবে।"
            ],
            "প্রতিষ্ঠানের তথ্য": [
                "প্রতিষ্ঠানের তথ্য যোগ করতে Setting মেনু ব্যবহার করুন।",
                "কোম্পানির নাম, ঠিকানা এবং মোবাইল 'Shop Information' এ সেট করুন।",
                "ব্যাকআপ লোকেশন সেট করে রাখুন।"
            ],
            " জিমেইল কনফিগার": [
                "আপনার কাস্টমারকে ইমেইল পাঠানোর জন্য জিমেইল কনফিগার করুন।",
                "আপনার ইমেইল এবং App Password আপডেট রাখুন।"
            ],
            "SMS API Key": [
                "SMS সার্ভিস প্রোভাইডারের API Key 'SMS Config' এ যুক্ত করুন।",
                "কাস্টমারকে ইনভয়েস/নোটিফিকেশন পাঠাতে এটি ব্যবহার হবে।",
                "API Key সুরক্ষিত রাখুন।"
            ],
            "Google Drive কনফিগার": [
                "https://console.cloud.google.com লিঙ্ক থেকে নতুন একটি প্রোজেট তৈরি করুন",
                "Search বার থেকে Google Drive API সার্চ করে তা Enable করুন।",
                "সাইট মেনু OAuth consent screen থেকে Create OAuth client এ ক্লিক করুন।",
                "Application type এ Desktop app সিলেক্ট করে Create বাটন ক্লিক করলে Download JSON পাওয়া যাবে।",
                "সাইট মেনু Audience থেকে Test users আপনার লগইন করা Gmail Address যুক্ত করুন।",
                "সব শেষে Download করা client_secrets.json ফাইল টি সেটিং - এ আপলোড করুন।"
            ],
            "মোবাইল ফোন কনফিগার": [
                "QR কোড স্ক্যান করার জন্য মোবাইলে iVCam Webcam অ্যাপ Install করুন।",
                "কম্পিউটারে iVCam Webcam কম্পিউটার Softwer ডাউলোড করে Install করুন।",
                "কম্পিউটার এবং মোবাইল একই ইন্টারন্টে রেখে iVCam Webcam কানেক্ট করুন।"
            ]
            
        }

        for section, points in help_data.items():
            # Section Heading
            heading = tk.Label(scroll_frame, text=section, font=("Helvetica", 12, "bold"), anchor="w", background=self.bg, fg=self.fg)
            heading.pack(fill="x", padx=10, pady=(10, 3))

            # Section Details
            for p in points:
                lbl = tk.Label(scroll_frame, text="• " + p, anchor="w", justify="left", wraplength=600, background=self.bg, fg=self.fg)
                lbl.pack(fill="x", padx=20, pady=2)
            
        