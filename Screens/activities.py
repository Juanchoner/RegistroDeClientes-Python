'''
Pantalla de actividades
'''
from tkinter import Frame
from Constants import style

class Actividades(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller