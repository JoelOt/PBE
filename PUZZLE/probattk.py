import tkinter as tk
from tkinter import ttk
from tkinter import *

def __init__(self, window):
        self.finestra = window
        self.finestra.title('Lector NFC')
        
if __name__ == '__main__':  #basicament si s'executa com a main, ens desplega la finestra
    window = Tk() #crea una finestra
    #application = Product(window)  #es guarda la finestra
    window.mainloop()  #la desplega
    