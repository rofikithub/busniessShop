import tkinter as tk
import tkinter.font as font
from tkinter import LEFT, ttk

def update_font(event=None):
    selected_font = font_combo.get()
    demo_label.config(font=(selected_font, 16))

root = tk.Tk()
root.title("Font Family Viewer")
root.geometry("400x300")

# সব ফন্ট আনা
fonts = sorted(font.families())

# Combobox এ ফন্ট নাম লোড
font_combo = ttk.Combobox(root, values=fonts, state="readonly")
font_combo.set("Select a font")
font_combo.pack(side=LEFT)

# ডেমো লেবেল
demo_label = tk.Label(root, text="Hello বন্ধু! 😃", font=("Arial", 16))
demo_label.pack(pady=20)

# ফন্ট পরিবর্তন হলে আপডেট
font_combo.bind("<<ComboboxSelected>>", update_font)

root.mainloop()


# Bahnschrift Condensed,