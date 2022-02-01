'''
Widget para el formulario de registro de clientes
'''


import tkinter
from tkinter import ttk, messagebox
import tkcalendar
from Constants import style

class FormRegister(tkinter.Frame):
    def __init__(self, parent, operation_db, entrys):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.operations = operation_db
        self.data_entrys = entrys


        self.schooling_invert = self.operations.transfrom_schooling()
        self.activities_invert = self.operations.transform_activities()
        self.create_form()

    def clear_entrys(self):
        self.data_entrys["nombre"].set('')
        self.data_entrys["domicilio"].set('')
        self.data_entrys["escolaridad"].set('')
        self.data_entrys["telefono"].set('')
        self.data_entrys["actividad"].set('')
        self.data_entrys["vencimiento"].set('')
        self.operations.refresh_table()

    def customer_registration(self):
        message = self.operations.registration(self.data_entrys, self.schooling_invert, self.activities_invert)
        messagebox.showwarning("Nota:", message)
        if message == "Cliente registrado":
            self.clear_entrys()

    def create_form(self):
        tkinter.Label(self, text = 'Nombre:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, textvariable=self.data_entrys["nombre"], **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Domicilio:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, textvariable=self.data_entrys["domicilio"], **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Escolaridad:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        self.cb_escolaridad = ttk.Combobox(self, textvariable=self.data_entrys["escolaridad"], state="readonly", **style.STYLE_ENTRYS)
        self.cb_escolaridad['values'] = self.operations.show_schooling()
        self.cb_escolaridad.pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Teléfono:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        tkinter.Entry(self, textvariable=self.data_entrys["telefono"], **style.STYLE_ENTRYS).pack(**style.PACK_ENTRYS)

        tkinter.Label(self, text = 'Actividad:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        self.cb_actividad = ttk.Combobox(self, textvariable=self.data_entrys["actividad"], state='readonly', **style.STYLE_ENTRYS)
        self.cb_actividad['values'] = self.operations.show_activities()
        self.cb_actividad.pack(**style.PACK_ENTRYS)
    
        tkinter.Label(self, text = 'Vencimiento:', anchor="w", **style.STYLE_LABELS).pack(
            **style.PACK_LABELS
        )
        self.calendar = tkcalendar.DateEntry(self, textvariable=self.data_entrys["vencimiento"], date_pattern='dd/mm/y').pack(**style.PACK_ENTRYS)

        buttons = tkinter.Frame(self)
        buttons.pack( side = tkinter.TOP, fill = tkinter.BOTH, expand = True)
        buttons.configure(background = style.BACKGROUND)
        tkinter.Button(buttons, text="Registrar", command=self.customer_registration, **style.STYLE_BUTTONS).grid(row=0, column=0, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Cancelar", command=self.clear_entrys, **style.STYLE_BUTTONS).grid(row=0, column=1, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Actualizar", **style.STYLE_BUTTONS).grid(row=1, column=0, **style.GRID_BUTTONS)
        tkinter.Button(buttons, text="Eliminar", **style.STYLE_BUTTONS).grid(row=1, column=1, **style.GRID_BUTTONS)



        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(1, weight=1)
            