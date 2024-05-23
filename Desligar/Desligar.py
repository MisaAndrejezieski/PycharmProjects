import os
from tkinter import *
from tkinter import ttk

def Desligar():
    os.system("shutdown /s /t 1")

   

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Sim", command=Desligar()).grid(column=1, row=0)
ttk.Button(frm, text="Não", command=root.destroy).grid(column=1, row=0)
root.mainloop()
