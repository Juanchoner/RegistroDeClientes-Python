'''
Widget para mostra a los usuarios en una tabla
'''

import tkinter
from tkinter import ttk
from Constants import style

class CostumerTable(tkinter.Frame):
    def __init__(self, parent, operations_db, entrys):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.operations = operations_db
        self.send_data = entrys


        self.create_table()
        self.operations.show_data_table(self.costumers_table)
        self.operations.create_refernce(self.costumers_table)

    def take_data(self, ev):
        data = self.operations.get_cursor(self.costumers_table)
        if not data:
            self.send_data["id"].set('')
            self.send_data["nombre"].set('')
            self.send_data["domicilio"].set('')
            self.send_data["escolaridad"].set('')
            self.send_data["telefono"].set('')
            self.send_data["actividad"].set('')
            self.send_data["vencimiento"].set('')
        else:
            self.send_data["id"].set(data[0])
            self.send_data["nombre"].set(data[1])
            self.send_data["domicilio"].set(data[2])
            self.send_data["escolaridad"].set(data[3])
            self.send_data["telefono"].set(data[4])
            self.send_data["actividad"].set(data[5])
            self.send_data["vencimiento"].set(data[6])

    def create_table(self):
        names_column = ("ID", "Nombre", "Domicilio", "Escolaridad", "Teléfono", "Actividad", "Vencimiento")
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

        self.costumers_table.bind("<ButtonRelease-1>", self.take_data)

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)
