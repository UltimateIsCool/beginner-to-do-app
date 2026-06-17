from tkinter import *
from tkinter import ttk

tasks = []

def insertData():
    name = nameEntry.get()
    pri = priEntry.get()
    category = categoryEntry.get()
    tasks.append([name, pri, category, "pending"])
    refreshTreeView()
    clearInput()
    
def updateData():
    item = toDoTreeView.focus()
    if item:
        index = int(item) - 1
        tasks[index] = [nameEntry.get(), priEntry.get(), categoryEntry.get(), tasks[index][3]]
        refreshTreeView()
        clearInput()
    
def deleteWork():
    item = toDoTreeView.focus()
    if item:
        index = int(item) - 1
        tasks.pop(index)
        refreshTreeView()
        clearInput()
        
def sendToUpdate():
    item = toDoTreeView.focus()
    if item:
        index = int(item) - 1
        task = tasks[index]
        nameEntry.insert(0, task[0])
        priEntry.insert(0, task[1])
        categoryEntry.insert(0, task[2])

def setWorkDone():
    item = toDoTreeView.focus()
    if item:
        index = int(item) - 1
        tasks[index][3] = "Done"
        refreshTreeView()

def refreshTreeView():
    toDoTreeView.delete(*toDoTreeView.get_children())
    for i, task in enumerate(tasks):
        toDoTreeView.insert("", "end", iid=i+1, text="", values=task)

def clearInput():
    nameEntry.delete(0, END)
    priEntry.delete(0, END)
    categoryEntry.delete(0, END)

root = Tk()
root.geometry("1000x500")
root.title("TO DO")

root.rowconfigure(0, weight=100)
root.columnconfigure(0, weight=40)
root.columnconfigure(1, weight=60)

insertBox = LabelFrame(root, text="insert info")
insertBox.grid(row=0, column=0, sticky="nsew")
insertBox.grid_propagate(False)

showBox = LabelFrame(root, text="info")
showBox.grid(row=0, column=1, sticky="nsew")
showBox.grid_propagate(False)

nameLabel = Label(insertBox, text="name :")
priLabel = Label(insertBox, text="priority :")
categoryLabel = Label(insertBox, text="category :")

nameEntry = Entry(insertBox)
priEntry = Entry(insertBox)
categoryEntry = Entry(insertBox)

nameLabel.pack(pady=10)
nameEntry.pack(pady=10, ipadx=10, ipady=10)

priLabel.pack(pady=10)
priEntry.pack(pady=10, ipadx=10, ipady=10)

categoryLabel.pack(pady=10)
categoryEntry.pack(pady=10, ipadx=10, ipady=10)

insertButton = Button(insertBox, text="insert", command=insertData)
updateButton = Button(insertBox, text="update", command=updateData)

insertButton.pack(pady=10, ipadx=10, ipady=10, side="bottom")
updateButton.pack(pady=10, ipadx=10, ipady=10, side="bottom")

headers = ["name", "pri", "category", "status"]

toDoTreeView = ttk.Treeview(showBox, columns=headers, show="headings")

toDoTreeView.column("#0", width=0, stretch=NO)
toDoTreeView.column("name", width=110)
toDoTreeView.column("pri", width=70)
toDoTreeView.column("category", width=120)
toDoTreeView.column("status", width=70)

toDoTreeView.heading("name", text="name")
toDoTreeView.heading("pri", text="pri")
toDoTreeView.heading("category", text="category")
toDoTreeView.heading("status", text="status")

toDoTreeView.pack(side="top")


operationBox = LabelFrame(showBox, text="operations")

operationBox.rowconfigure(0, weight=100)
operationBox.columnconfigure(0, weight=30)
operationBox.columnconfigure(1, weight=30)
operationBox.columnconfigure(2, weight=30)
operationBox.pack(side="bottom", fill="x")

operationDeletetButton = Button(operationBox, text="delete", command=deleteWork)
operationDoneButton = Button(operationBox, text="done", command=setWorkDone)
operationUpdateButton = Button(operationBox, text="update", command=sendToUpdate)

operationDeletetButton.grid(row=0, column=0)
operationDoneButton.grid(row=0, column=1)
operationUpdateButton.grid(row=0, column=2)

root.mainloop()