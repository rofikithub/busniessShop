from tkinter import messagebox
from model.Category import Category


class CategoryController:
    def __init__(self):
        pass
    def createCategory(self):
        name = self.cName.get()
        if name == "":
            messagebox.showwarning("Error", "Please enter a Category name ! ")
        else:
            if Category.chack(self,name):
                messagebox.showerror("Error", "Category already exists.")
            else:
                if Category.create(self, name):
                    messagebox.showinfo("Success", "Category saved successfully.")
                    CategoryController.clearData(self)
                    CategoryController.categoryShow(self)

    def update(self):
        id   = self.catID.get()
        name = self.cName.get()
        if id=="":
            messagebox.showerror("Error", "Something is wrong please try again.")
        elif name=="":
            messagebox.showerror("Error", "Please enter a Category name !")
        else:
            if Category.chack(self,name):
                messagebox.showerror("Error", "Category already exists.")
            else:
                if Category.update(self,[name,id]):
                    messagebox.showinfo("Success", "Category name update successfully!")
                    CategoryController.clearData(self)
                    CategoryController.categoryShow(self)
                else:
                    messagebox.showerror("Error", "Something is wrong please try again.")


    def categoryShow(self):
        lists = Category.all(self)
        if lists:
            self.treev.delete(*self.treev.get_children())
            for list in lists:
                self.treev.insert("", 'end', text=list[1],values=list)

    def clearData(self):
        self.catID.set('')
        self.cName.set('')