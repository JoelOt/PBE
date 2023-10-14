import threading
import puzzle1
from gi.repository import Gtk, Gdk, GObject
import time

class MyWindow(Gtk.Window):
    
    

    def __init__(self):
        super().__init__()
        Gtk.Window.__init__(self, title= "Puzzle 2 :)")  

        self.verticalBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.verticalBox)
        
        self.col1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.verticalBox.pack_start(self.col1, True, True, 0)
        self.col2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.verticalBox.pack_start(self.col2, True, True, 0)
        
        
        self.msg = Gtk.Label("Esperant tarjeta NFC...")
        self.col1.pack_start(self.msg, True, True, 0)
        
        
        self.clear = Gtk.Button(label="clear")
        self.clear.connect("clicked", self.netejarPremut)
        self.col2.pack_start(self.clear, True, True, 0)
    
    def netejarPremut(self, widjet):
        thread2 = threading.Thread(target= self.metodeThread)
        thread2.start()
        
    def metodeThread(self):
        GObject.idle_add(self.update_ui)
        uid = l1.llegir()
        print(uid)
        GObject.idle_add(self.update_ui2, uid)
        
    def update_ui(self): 
        self.msg.set_text("Esperant targeta NFC...")
        self.msg.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("green"))
    
    def update_ui2(self, uid):
        self.msg.set_text(uid)
        self.msg.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("red"))
        


#main:
lock = threading.Lock()
l1 = puzzle1.Lector_NFC()
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
thread1 = threading.Thread(target= win.metodeThread)
thread1.start()
Gtk.main()