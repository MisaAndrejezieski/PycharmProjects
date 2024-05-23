import os
from tkinter import *

desligar= input("Quer desligar sue pc?")


if (desligar == "SIM" or "sim" or "S" or "s"):
    def desligar_computador():
        os.system("shutdown /s /t 1")
        desligar_computador()
else:
    print("Desistiu???")

janela = Tk()


janela.mainloop()
