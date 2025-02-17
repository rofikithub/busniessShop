from tkinter import messagebox
from model.Category import Category
from model.Dealer import Dealer


class DealerController:
    def __init__(self):
        self.did     = self.did.get()
        self.company = self.company.get()
        self.mobile  = self.mobile.get()
        self.srname  = self.srname.get()

    def createDealer(self):
        company = self.company.get()
        mobile  = self.mobile.get()
        srname  = self.srname.get()
        if company == "":
            messagebox.showwarning("Error", "Please enter a company name ! ")
        elif mobile == "":
            messagebox.showwarning("Error", "Please enter a mobile number ! ")
        elif srname == "":
            messagebox.showwarning("Error", "Please enter name of SR ! ")
        else:
            if Dealer.chack(self,[company, mobile]):
                messagebox.showerror("Error", "Company already exists.")
            else:
                if Dealer.create(self, [company, mobile, srname]):
                    messagebox.showinfo("Success", "Company name saved successfully.")
                    DealerController.clearData(self)
                    DealerController.dealerShow(self)

    def updateDealer(self):
        did     = self.did.get()
        company = self.company.get()
        mobile  = self.mobile.get()
        srname  = self.srname.get()
        if did=="":
            messagebox.showerror("Error", "Something is wrong please try again.")
        elif company == "":
            messagebox.showwarning("Error", "Please enter a company name ! ")
        elif mobile == "":
            messagebox.showwarning("Error", "Please enter a mobile number ! ")
        elif srname == "":
            messagebox.showwarning("Error", "Please enter name of SR ! ")
        else:
            if Dealer.chack(self,[company, mobile]):
                Dealer.updatesr(self, [srname, did])
                DealerController.clearData(self)
                DealerController.dealerShow(self)
                messagebox.showinfo("Success", "SR name update successfully!")
            else:
                if Dealer.update(self,[company, mobile, srname, did]):
                    DealerController.clearData(self)
                    DealerController.dealerShow(self)
                    messagebox.showinfo("Success", "Company update successfully!")
                else:
                    messagebox.showerror("Error", "Something is wrong please try again.")


    def dealerShow(self):
        lists = Dealer.all(self)
        if lists:
            self.treed.delete(*self.treed.get_children())
            for list in lists:
                self.treed.insert("", 'end', text=list[1],values=list)

    def clearData(self):
        self.did.set('')
        self.company.set('')
        self.mobile.set('')
        self.srname.set('')

    def deleteDealer(self):
        id = self.did.get()
        if id > 0:
            ans = messagebox.askokcancel("Confirm", "Are you sure to delete company?")
            if ans == True:
                if Dealer.chackDelete(self,[id]):
                    messagebox.showerror("Error", "Enable to delete company name.")
                else:
                    if Dealer.delete(self,id):
                        DealerController.clearData(self)
                        DealerController.dealerShow(self)
                        messagebox.showinfo("Confirmation", "Voucher has been deleted")
        else:
            messagebox.showwarning("Warning", "Please select a company name ! ")