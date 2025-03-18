import tkinter as tk
import random


root = tk.Tk()
frame = tk.Frame(root, width=500, height=500)
rowstart = 3


def add_fixed():
    """
    Function to add fixed gui items (same every time)
    
    adds title, item entry, and count entry.
    
    """
    #variables
    itemName = tk.StringVar()
    itemCount = tk.IntVar()
    itemCount.set("")
    
    
    #title
    tk.Label(root, text='Grocery list', font=('Arial', 20)).grid(row=0,columnspan=2, sticky='NW', padx = 15, pady= 5)
    
    #item entry
    tk.Label(root, text='Item:').grid(row=1, padx=10, sticky='W')
    tk.Entry(root, textvariable=itemName).grid(row=1, column=1, sticky='W')
    #count entry
    tk.Label(root, text='Amount:').grid(row=2, column=0, padx=10, sticky='W')
    tk.Entry(root, textvariable=itemCount).grid(row=2, column=1, sticky='W')
    
    #add button
    tk.Button(root, text='Add') ).grid(row=1, column=2, sticky='W', padx=10)


    
    
add_fixed()
    
root.mainloop()
