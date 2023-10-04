from tkinter import ttk
from tkinter import *

class Puzzle2:
    def __init__(self, window):
        self.finestra = window
        self.finestra.title('Lector NFC')

        frame = LabelFrame(self.finestra, text = 'Llegeixi targeta NFC').grid(row= 0, column= 0)
        
        ttk.Button(frame, text= 'Prem per llegir una targeta NFC').grid(row= 0, column = 1)
    

if __name__ == '__main__':  #basicament si s'executa com a main, ens desplega la finestra
    window = Tk() #crea una finestra
    #application = Product(window)  #es guarda la finestra
    window.mainloop()  #la desplega
    