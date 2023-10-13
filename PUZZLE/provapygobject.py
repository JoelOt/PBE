import puzzle1
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    
    idd = None

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        
        
        self.llegir = Gtk.Button(label="Prem per llegir")  #crear el botó
        self.llegir.connect("clicked", self.lector)  #acció del botó
        self.add(self.llegir)  #afegir-lo a la window
        
        self.neteja = Gtk.Button(label="neteja")
        self.neteja.connect("clicked", self.netejar)
        self.add(self.neteja)
        
    def lector(self, widget):
        idd = l1.llegir()
        print(idd)
        #print("Hello World")

    def netejar(self, widget):
        idd = None


#main:        
l1 = puzzle1.Lector_NFC()
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()