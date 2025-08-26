import os
import io
import shutil
from tkinter import filedialog, messagebox
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive.file']
HOME_DIRECTORY = os.path.expanduser( '~' )
DIRECTORY= (HOME_DIRECTORY+"\\AppData\\Local\\BMS")
TOKEN_FILE= (HOME_DIRECTORY+"\\AppData\\Local\\BMS\\token.json")
SYSTEM_PATH = (HOME_DIRECTORY+"\\AppData\\Local\\BMS\\system.json")
DATABASE_PATH = (HOME_DIRECTORY+"\\AppData\\Local\\BMS\\bms_database.db")
CLIENT_SECRET_FILE = (HOME_DIRECTORY+"\\AppData\\Local\\BMS\\client_secrets.json")

class DriveController:
    def __init__(self):
        file = None

    def getFile(self,fnam):
        if fnam=="db":
          return DATABASE_PATH
        elif fnam=="system":
          return SYSTEM_PATH
        elif fnam=="drive":
            return CLIENT_SECRET_FILE
        elif fnam=="token":
          return CLIENT_SECRET_FILE
        else:
            return False
      
    def get_credentials():
        creds = None
        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                creds = flow.run_local_server(port=0)

            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())

        return creds

    def get_drive_service(self):
        creds = DriveController.get_credentials()
        service = build('drive', 'v3', credentials=creds)
        return service

    # ---------------- Upload in Google Drive ----------------
    def upload_file(self,fnam):
        file_path = DriveController.getFile(self,fnam)
        if file_path:
            service = DriveController.get_drive_service(self)
            file_metadata = {'name': os.path.basename(file_path)}
            media = MediaFileUpload(file_path, resumable=True)
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            if file.get('id'):
                messagebox.showinfo("Success", f"File uploaded successfully in your google drive!")

    # ---------------- Download from Goole Drive ----------------
    def download_file(self,file_id, save_as):
        service = DriveController.get_drive_service()
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO(save_as, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        fh.close()
        
        
    # ---------------- Upload file in softwer system ----------------
    # def file_upload(self):
    #     file_path = filedialog.askopenfilename(title="Select File", filetypes=[("DB/JSON","*.db *.json")])
    #     if file_path:
            
    #         try:
    #             dest_path = os.path.join(DIRECTORY, os.path.basename(file_path))
    #             shutil.copy(file_path, dest_path)

    #             messagebox.showinfo("Success", f"File uploaded successfully!")
    #         except Exception as e:
    #             messagebox.showerror("Error", str(e))
                
    def uploadClient(self):
        file_path = self.client.get()
        if file_path:
            os.makedirs(DIRECTORY, exist_ok=True)
            new_name = "client_secrets.json"
            
            try:
                dest_path = os.path.join(DIRECTORY, new_name)
                shutil.copy(file_path, dest_path)
                messagebox.showinfo("Success", f"client_secrets.json File uploaded successfully!")
                self.client.set("")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                
    def uploadDatabase(self):
        file_path = self.database.get()
        if file_path:
            os.makedirs(DIRECTORY, exist_ok=True)
            new_name = "bms_database.db"
            
            try:
                dest_path = os.path.join(DIRECTORY, new_name)
                shutil.copy(file_path, dest_path)
                messagebox.showinfo("Success", f"Backup Database File uploaded successfully!")
                self.client.set("")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                
                
    def uploadSystemJson(self):
        file_path = self.system.get()
        if file_path:
            os.makedirs(DIRECTORY, exist_ok=True)
            new_name = "system.json"
            
            try:
                dest_path = os.path.join(DIRECTORY, new_name)
                shutil.copy(file_path, dest_path)
                messagebox.showinfo("Success", f"System Json File uploaded successfully!")
                self.system.set("")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                
                