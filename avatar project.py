from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=200)
frm.grid()
ttk.Label(frm, text="avatar!").grid(column=200, row=200)
ttk.Button(frm, text="exit", command=root.destroy).grid(column=100, row=100)
root.mainloop()