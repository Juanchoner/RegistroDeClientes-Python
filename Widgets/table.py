'''
Widget para mostra a los usuarios en una tabla
'''

import tkinter
from tkinter import ttk

from Constants import style

class CostumerTable(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background="green")

        self.create_table()

    def create_table(self):
        names_column = ("Nombre", "Domicilio", "Escolaridad", "Teléfono", "Actividad", "Vencimiento")
        self.costumers_table = ttk.Treeview(self, columns = names_column)
        for column in names_column:
            self.costumers_table.heading(f'{column}', text=f'{column}')
        self.costumers_table['show'] = 'headings'
        for name in names_column:
            self.costumers_table.column(f'{name}', **style.STYLE_TABLE)
        self.costumers_table.grid(row=0, column=0, sticky=tkinter.NSEW)

        #Barra de desplazamiento vertical
        move_y = ttk.Scrollbar(self, orient = "vertical", command=self.costumers_table)
        move_y.grid(row=0, column=1, sticky=tkinter.NS)
        self.costumers_table.config(yscrollcommand = move_y.set)

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)
