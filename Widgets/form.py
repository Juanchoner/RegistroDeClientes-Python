'''
Widget para el formulario de registro de clientes
'''

import tkinter
from tkinter import ttk
import tkcalendar
from Constants import style

class FormRegister(tkinter.Frame):
    def __init__(self, parent, operation_db):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.operations = operation_db

        #Variables de los entrys datos en los etrys
        self.nombre = tkinter.StringVar()
        self.domicilio = tkinter.StringVar()
        self.escolaridad = tkinter.StringVar()
        self.telefono = tkinter.StringVar()
        self.actividad = tkinter.StringVar()
        self.vencimiento = tkinter.StringVar()

        self.create_form()

    def clear_entrys(self):
        self.nombre.set('')
        self.domicilio.set('')
        self.telefono.set('')
        self.escolaridad.set('')
        self.actividad.set('')
        self.vencimiento.set('')

    def create_form(self):
        tkinter.Label(self, text = 'Nombre:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, textvariable=self.nombre, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Domicilio:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, textvariable=self.domicilio, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Escolaridad:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        self.cb_escolaridad = ttk.Combobox(self, state="readonly", **style.STYLE_ENTRYS)
        self.cb_escolaridad['values'] = self.operations.show_schooling()
        self.cb_escolaridad.pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Teléfono:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, textvariable=self.telefono, **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Actividad:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        self.cb_actividad = ttk.Combobox(self, state='readonly', **style.STYLE_ENTRYS)
        self.cb_actividad['values'] = self.operations.show_activities()
        self.cb_actividad.pack(**style.PACK_ENTRYS)
    
        tkinter.Label(self, text = 'Vencimiento:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        self.calendar = tkcalendar.DateEntry(self, date_pattern='dd/mm/y').pack(**style.PACK_ENTRYS)

        buttons = tkinter.Frame(self)
        buttons.pack( side = tkinter.TOP, fill = tkinter.BOTH, expand = True)
        buttons.configure(background = style.BACKGROUND)
        tkinter.Button(buttons, text="Registrar", **style.STYLE_BUTTONS).grid(row=0, column=0, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Limpiar", command=self.clear_entrys, **style.STYLE_BUTTONS).grid(row=0, column=1, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Actualizar", **style.STYLE_BUTTONS).grid(row=1, column=0, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Eliminar", **style.STYLE_BUTTONS).grid(row=1, column=1, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Actualizar tabla", **style.STYLE_BUTTONS).grid(row=2, columnspan=2, **style.GRID_BUTTONS)

        
        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(1, weight=1)
            