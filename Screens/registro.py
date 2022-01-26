'''
Pantalla de registro de clientes
'''

from tkinter import Frame
import tkinter
from Constants import style
from Widgets.form import FormRegister
from Widgets.table import CostumerTable

class Registro(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(
                self, 
                text = 'Clientes',
                justify = tkinter.CENTER,
                **style.TITLE).pack(
                    side = tkinter.TOP,
                    fill = tkinter.BOTH,
                    padx = 10,
                    pady = 5
                )

        operations_frame = tkinter.Frame(self)
        operations_frame.configure(background = style.BACKGROUND)
        operations_frame.pack(
            side = tkinter.TOP,
            fill = tkinter.BOTH,
            expand = True,
            padx = 10,
            pady = 5
        )

        FormRegister(operations_frame).grid(row = 0, column=0, sticky=tkinter.NSEW, padx=2, pady=2)
        CostumerTable(operations_frame).grid(row = 0, column=1, sticky=tkinter.NSEW, padx=2, pady=2)

        operations_frame.grid_columnconfigure(0, weight=1)
        operations_frame.grid_columnconfigure(1, weight=5)
        operations_frame.grid_rowconfigure(0, weight=1)