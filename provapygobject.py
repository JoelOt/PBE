import puzzle1
from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
    
    

    def __init__(self):
        Gtk.Window.__init__(self, title= "Lector NFC")
        uid = None
        self.verticalBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.verticalBox)
        
        self.col1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.verticalBox.pack_start(self.col1, True, True, 0)
        self.col2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.verticalBox.pack_start(self.col2, True, True, 0)
        
        
        self.msg = Gtk.Label("Lector NFC")
        self.msg.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("green"))
        self.col1.pack_start(self.msg, True, True, 0)
        
        self.llegir = Gtk.Button(label="Prem per llegir")  #crear el botó
        self.llegir.connect("clicked", self.lector)  #acció del botó
        self.col2.pack_start(self.llegir, True, True, 0)
        
        
        self.neteja = Gtk.Button(label="neteja")
        self.neteja.connect("clicked", self.netejar)
        self.col2.pack_start(self.neteja, True, True, 0)
        
    def lector(self, widget):
        uid = l1.llegir()   
        print(uid)
        self.msg.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("red"))

    def netejar(self, widget):
        uid = None
        self.msg.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("green"))

#main:
l1 = puzzle1.Lector_NFC()
win = MyWindow()
win.connect("destroy", Gtk.main_quit)

win.show_all()
Gtk.main()


