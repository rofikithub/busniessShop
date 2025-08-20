import os
import tkinter as tk
from view.loginView import loginView
from view.dashboardView import dashboardView


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
        
        home_directory = os.path.expanduser( '~' )
        
        report = (home_directory+"\\AppData\\Local\\BMS\\report")
        if not os.path.exists(report):
            os.mkdir(report)
            
        qrpng = (home_directory+"\\AppData\\Local\\BMS\\qrpng")
        if not os.path.exists(qrpng):
            os.mkdir(qrpng)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop() 


# pip install -r libs.txt
