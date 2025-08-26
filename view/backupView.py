import tkinter as tk
from tkinter import filedialog, messagebox
from controller.DriveController import DriveController


class BMSDriveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMS Google Drive Manager")
        self.create_widgets()

    def create_widgets(self):
        # Upload Section
        self.lbl_upload = tk.Label(self.root, text="Upload Database to Google Drive", font=("Arial", 12))
        self.lbl_upload.pack(pady=5)

        self.btn_upload = tk.Button(self.root, text="Upload File", command=DriveController.upload_file(self,"db"), width=40)
        self.btn_upload.pack(pady=5)

        # Download Section
        self.lbl_download = tk.Label(self.root, text="Download Database by File ID", font=("Arial", 12))
        self.lbl_download.pack(pady=10)

        self.entry_fileid = tk.Entry(self.root, width=50)
        self.entry_fileid.pack(pady=5)

        self.btn_download = tk.Button(self.root, text="Download File", command=self.download_file, width=40)
        self.btn_download.pack(pady=5)

    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Select Database", filetypes=[("DB/JSON","*.db *.json")])
        if file_path:
            try:
                file_id = self.drive.upload_file(file_path)
                messagebox.showinfo("Success", f"Uploaded!\nFile ID: {file_id}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def download_file(self):
        file_id = self.entry_fileid.get().strip()
        if not file_id:
            messagebox.showwarning("Warning", "Enter File ID")
            return
        save_path = filedialog.asksaveasfilename(title="Save As", defaultextension=".db", filetypes=[("DB/JSON","*.db *.json")])
        if save_path:
            try:
                self.drive.download_file(file_id, save_path)
                messagebox.showinfo("Success", f"Downloaded to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = BMSDriveApp(root)
    root.mainloop()
