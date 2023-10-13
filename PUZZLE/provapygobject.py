import puzzle1
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button = Gtk.Button(label="Click Here")  #crear el botó
        self.button.connect("clicked", self.on_button_clicked)  #acció del botó
        self.add(self.button)  #afegir-lo a la window

    def on_button_clicked(self, widget):
        print(l1.llegir())
        print("Hello World")


l1 = puzzle1.Lector_NFC()
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()