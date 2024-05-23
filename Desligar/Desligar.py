import os
from tkinter import *


def Desligar():
    desligar= input("Quer desligar sue pc?")
    if (desligar == "SIM" or "sim" or "S" or "s"):
        def desligar_computador():
            os.system("shutdown /s /t 1")
            desligar_computador()
    else:
            print("Desistiu???")

janela = Tk()
janela.geometry("400x400")
janela.title("Desligando o computador...")

texto_orientacao = Label(janela, text="Desligar")
texto_orientacao.grid(column=20, row=0)

butao = Button(janela, text="Sim")
butao.grid(column=22, row=0)
butao2 = Button(janela, text="Não")
butao2.grid(column=26, row=0)

janela.mainloop()
