'''
Widget para el formulario de registro de clientes
'''

import tkinter
from Constants import style

class FormRegister(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)

        self.create_form()

    def create_form(self):
        tkinter.Label(self, text = 'Nombre:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Domicilio:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Escolaridad:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Teléfono:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Actividad:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Vencimiento:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        buttons = tkinter.Frame(self)
        buttons.pack( side = tkinter.TOP, fill = tkinter.BOTH, expand = True)
        buttons.configure(background = style.BACKGROUND)
        tkinter.Button(buttons, text="Registrar", **style.STYLE_BUTTONS).grid(row=0, column=0, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Limpiar", **style.STYLE_BUTTONS).grid(row=0, column=1, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Actualizar", **style.STYLE_BUTTONS).grid(row=1, column=0, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Eliminar", **style.STYLE_BUTTONS).grid(row=1, column=1, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Actualizar tabla", **style.STYLE_BUTTONS).grid(row=2, columnspan=2, **style.GRID_BUTTONS)

        
        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(1, weight=1)
            