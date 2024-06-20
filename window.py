import gi
gi.require_version("Gtk","4.0")
from gi.repository import Gtk, GLib

QUIT = False

def quit_(window):
    print(window)
    global QUIT
    QUIT = True

class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ventana")
        self.connect("close-request", quit_)
        self.boton = Gtk.Button()
        self.boton.set_label("Hola")
        self.boton.connect("clicked", self.on_clicked_button)
        self.boton.connect("activate", self.on_activate_button)
        self.set_child(self.boton)
        self.show

    def on_activate_button(self,widget):
        print("activado")

    def on_clicked_button(self,widget):
        print("CLICK")

    
def main():
    Window()
    loop = GLib.MainContext().default()
    while not QUIT:
        loop.iteration(True)