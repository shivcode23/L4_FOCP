import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root=tk.Tk()
root.title("Contact")

tk.Label(root,text="Name").grid(row=1,column=0,columnspan=4)
tk.Label(root,text="Address").grid(row=1,column=8,columnspan=4)


name=tk.Entry(root,width=16)
address=tk.Entry(root,width=16)

name.grid(row=1,column=4,columnspan=4)
address.grid(row=1,column=12,columnspan=4)

 # Create a Treeview widget to display contact details
tree = ttk.Treeview(root, columns=("Name", "Address","Action"), show='headings')
tree.heading("Name", text="Name")
tree.column("Name",anchor=tk.CENTER)
tree.heading("Address", text="Address")
tree.column("Address",anchor=tk.CENTER)
tree.grid(row=4, column=0, columnspan=22)
tree.heading("Action",text="Action")
tree.column("Action",anchor=tk.CENTER,width=100)

# def find_duplicate(name,address):
#     for item_id in tree.get_children():
#         values=tree.item(item_id,"values")
#         if values[0] == name and values[1] == address:
#             return item_id
#         else:
#             return None

def checkDuplicate(name,address):
    for item_id in tree.get_children():
        values=tree.item(item_id,"values")
        print("-------------",name,address)
        print("-------------",values[0], values[1])
        if name == values[0] and address == values[1]:
            return item_id
        else:
            return None

buttonAction=""
def setEditButtonAction():
    global buttonAction
    buttonAction="Edit"

def setSaveButtonAction():
    global buttonAction
    buttonAction="Save"

def editAction(item_id):
    if messagebox.askyesno("Edit Data","Are u sure to edit data?"):
        item=tree.item(item_id)
        nameTree=item['values'][0]
        addressTree=item['values'][1]

        address.delete(0,tk.END)
        name.delete(0,tk.END)

        name.insert(tk.END,nameTree)
        address.insert(tk.END,addressTree)
        
        setEditButtonAction()

        print(name,address,buttonAction)

def deleteAction(item_id):
    if messagebox.askyesno("Delete  Data", "Are you sure to delete?"):
        tree.delete(item_id)

def onRowClick(event):
    global item_id
    item_id=tree.identify_row(event.y)
    col=tree.identify_column(event.x)
    print(event)

    if col == "#3":
        action=""
        if(event.x < 442):
            editAction(item_id)
        else:
            deleteAction(item_id)
        # ation = tree.item(item_id,'values')[2]
        print(action)

tree.bind("<Button-1>", onRowClick)

data=[];
def saveData():
    print(buttonAction)
    nameEntry=name.get()
    addressEntry=address.get()

    isUpdate=buttonAction == "Edit"
   
    if isUpdate:
        tree.item(item_id,values=(nameEntry,addressEntry, "Edit | Delete"))
        messagebox.showinfo("Update","Data updated Successfully")
    else:  
        item_id_check = checkDuplicate(nameEntry,addressEntry)
        print(item_id_check)
        if item_id_check:
            messagebox.showinfo("Duplicate Data!","Data you have entered is already in table")
            return
        else:
            data.append(f"name : {nameEntry}, address : {addressEntry}")
            tree.insert("", tk.END, values=(nameEntry, addressEntry,"Edit  |  Delete"))
            print(data) 

    setSaveButtonAction()
    address.delete(0,tk.END)
    name.delete(0,tk.END)
    

   

tk.Button(root,text="Save / Update",command=saveData).grid(row=1,column=16)

root.mainloop()