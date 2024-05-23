import os
from tkinter import *
from tkinter import ttk

"""def Desligar():
    desligar= input("Quer desligar sue pc?")
    if (desligar == "SIM" or "sim" or "S" or "s"):
        def desligar_computador():
            os.system("shutdown /s /t 1")
            desligar_computador()
    else:
            print("Desistiu???")"""

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Sim", command=root.destroy).grid(column=1, row=0)
root.mainloop()
