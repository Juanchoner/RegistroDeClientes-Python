'''
Ventana principal de la aplicación la cual contendra
las todas las ventanas.
'''
import tkinter
from Constants import style
from Screens.activities import Actividades
from Screens.registro import Registro

class Manager(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Clientes")
        container = tkinter.Frame(self)
        container.pack(
            side = tkinter.TOP,
            fill = tkinter.BOTH,
            expand = True
        )
        container.configure(background = style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        #Creamos un diccionario para guardar nuestras ventanas (frames)
        self.frames = {}
        
        for ventana in (Registro, Actividades):
            frame = ventana(container, self)
            self.frames[ventana] = frame
            frame.grid(row = 0, column = 0, sticky = tkinter.NSEW)
        self.show_frame(Registro)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()