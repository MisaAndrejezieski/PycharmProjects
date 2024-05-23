import os
from tkinter import *
from tkinter import ttk

"""def Desligar():
    os.system("shutdown /s /t 1")"""

   

root = Tk()
frm = ttk.Frame(root, padding=40)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Sim", command=root.title).grid(column=0, row=2)
ttk.Button(frm, text="Não", command=root.destroy).grid(column=0, row=4)
root.mainloop()
