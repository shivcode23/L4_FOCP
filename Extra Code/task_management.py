import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("Contact")

tk.Label(root,text="Name").grid(row=1,column=0,columnspan=4)
tk.Label(root,text="Address").grid(row=1,column=8,columnspan=4)


name=tk.Entry(root,width=16)
address=tk.Entry(root,width=16)

name.grid(row=1,column=4,columnspan=4)
address.grid(row=1,column=12,columnspan=4)

 # Create a Treeview widget to display contact details
tree = ttk.Treeview(root, columns=("Name", "Address"), show='headings')
tree.heading("Name", text="Name")
tree.column("Name",anchor=tk.CENTER)
tree.heading("Address", text="Address")
tree.column("Address",anchor=tk.CENTER)
tree.grid(row=4, column=0, columnspan=16)

data=[];
def saveData():
    nameEntry=name.get()
    addressEntry=address.get()
    data.append(f"name : {nameEntry}, address : {addressEntry}")
    tree.insert("", tk.END, values=(nameEntry, addressEntry))
    print(data)
   

tk.Button(root,text="Save",command=saveData).grid(row=2,column=0)

root.mainloop()