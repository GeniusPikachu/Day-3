from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Avatar Project").grid(column=1000, row=1000)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=10, row=1)
root.mainloop()