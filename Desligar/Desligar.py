import os  # Importa o módulo os que permite a interação com o sistema operacional
from tkinter import *  # Importa tudo da biblioteca tkinter para criar interfaces gráficas
from tkinter import ttk  # Importa ttk da biblioteca tkinter para usar widgets temáticos

# Feito por Misa

def Desligar():  # Define uma função chamada 'Desligar'
    os.system("shutdown /s /t 1")  # Executa o comando de desligamento do sistema operacional

root = Tk()  # Cria a janela principal
frm = ttk.Frame(root, padding=40)  # Cria um frame com padding de 40
frm.grid()  # Posiciona o frame na janela
ttk.Label(frm, text="Desligar").grid(column=0, row=0)  # Cria um rótulo 'Desligar' no frame
ttk.Button(frm, text="Sim", command=Desligar).grid(column=0, row=2)  # Cria um botão 'Sim' que, quando pressionado, executa a função 'Desligar'
ttk.Button(frm, text="Não", command=root.destroy).grid(column=0, row=4)  # Cria um botão 'Não' que, quando pressionado, fecha a janela
root.mainloop()  # Inicia o loop principal da janela
