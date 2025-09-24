import os
import io
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import requests
from view import dashboardView

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
        
    def checkNet(self):
        url = "http://www.google.com"
        timeout = 50
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.ConnectionError:
            return False
        except requests.Timeout:
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
                self.root.destroy()
                dashboardView.dashboardView(tk.Tk())
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
                self.root.destroy()
                dashboardView.dashboardView(tk.Tk())
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
                self.root.destroy()
                dashboardView.dashboardView(tk.Tk())
            except Exception as e:
                messagebox.showerror("Error", str(e))
              
                
    def deleteDrive(self,service,fileName):
        query = (f"name='{fileName}' and trashed=false")
        response = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
        items = response.get('files', [])
        for item in items:
            service.files().delete(fileId=item['id']).execute()
        
          
    def uploaDrive(self):
        if DriveController.checkNet(self):
            if os.path.exists(CLIENT_SECRET_FILE):
                service = DriveController.get_drive_service(self)
                DriveController.deleteDrive(self,service,"bms_database.db")
                file_metadata = {'name': os.path.basename(DATABASE_PATH)}
                media = MediaFileUpload(DATABASE_PATH, resumable=True)
                db = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                if db.get('id'):
                    DriveController.deleteDrive(self,service,"client_secrets.json")
                    file_metadata = {'name': os.path.basename(CLIENT_SECRET_FILE)}
                    media = MediaFileUpload(CLIENT_SECRET_FILE, resumable=True)
                    cs = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                    if cs.get('id'):
                        DriveController.deleteDrive(self,service,"system.json")
                        file_metadata = {'name': os.path.basename(SYSTEM_PATH)}
                        media = MediaFileUpload(SYSTEM_PATH, resumable=True)
                        ss = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                        if ss.get('id'): 
                            messagebox.showinfo("Success", f"Back files upload successfully in Your Google Drive!")
            else:
                # https://console.cloud.google.com/
                messagebox.showwarning("Drive Api","Not Found client_secrets.json File!")
        else:
            messagebox.showwarning("No Internet","Chack your internet connection!")
            
            
   