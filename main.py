import os, time
import tkinter as tk
from PIL.ImageChops import screen
from view.loginView import loginView
from view.dashboardView import dashboardView
from controller.VoiceController import VoiceController


from reportlab.graphics.barcode import code128
from reportlab.graphics.barcode import code93
from reportlab.graphics.barcode import code39
from reportlab.graphics.barcode import usps
from reportlab.graphics.barcode import usps4s
from reportlab.graphics.barcode import ecc200datamatrix


class App:
    def __init__(self, root):
        loginView(root)
        #dashboardView(root)
        
        folder = "report"
        if not os.path.exists(folder):
            os.mkdir(folder)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop() 
    
# pip install -r libs.txt
