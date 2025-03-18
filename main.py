import tkinter as tk
import random


root = tk.Tk()
frame = tk.Frame(root, width=500, height=500)
rowstart = 4

class AddItem():
    """
    Adds items to gui
    
    class means its easier to delete i suppose.
    """
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.add_items()
        
    def add_items(self):
        global rowstart
        
        #label
        self.txt = tk.Label(root, text=f'{self.count}x {self.name}')
        self.txt.grid(row=rowstart, column=0, sticky='W', padx=5, pady=10)
        #removal button
        self.btt = tk.Button(root, text='Remove', command=self.remove)
        self.btt.grid(row=rowstart, column=1, sticky='W', padx=5, pady=10)
        rowstart += 1
        
    def remove(self):
        self.txt.destroy()
        self.btt.destroy()

def itemChk(name, count, e1, e2, f):
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    
    if count == "":
        count = 1
    if name == "":
        f.set('Item must be named!')
        return 
    else:
        f.set("")
        AddItem(name, count)

def add_fixed():
    """
    Function to add fixed gui items (same every time)
    
    adds title, item entry, and count entry.
    
    """
    #variables
    feedback = tk.StringVar()
    itemName = tk.StringVar()
    itemCount = tk.StringVar()

    
    #title
    tk.Label(root, text='Grocery list', font=('Arial', 20)).grid(row=0,columnspan=2, sticky='NW', padx = 15, pady= 5)
    
    #feedback label
    tk.Label(root, textvariable=feedback).grid(row=1, column=0, sticky='W', padx=15, pady=5,columnspan=2)
    
    #item entry
    tk.Label(root, text='Item:').grid(row=2, padx=10, sticky='W')
    e1 = tk.Entry(root, textvariable=itemName)
    e1.grid(row=2, column=1, sticky='W')
    #count entry
    tk.Label(root, text='Amount:').grid(row=3, column=0, padx=10, sticky='W')
    e2 = tk.Entry(root, textvariable=itemCount)
    e2.grid(row=3, column=1, sticky='W')
    
    #add button
    tk.Button(root, text='Add', command=lambda: itemChk(itemName.get(), itemCount.get(), e1, e2, feedback)).grid(row=2, column=2, sticky='W', padx=10)


    
    
add_fixed()
    
root.mainloop()
