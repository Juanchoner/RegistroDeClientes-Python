'''
Las operaciones que tiene la apliación.
'''
import tkinter
from DB.connectdb import DataAccessObject

class Operations:
    def __init__(self):
        self.operation = DataAccessObject()

    def show_data_table(self, table):
        try:
            rows = self.operation.show_costumers_db()
        except:
            print('Ha ocurrido un problema...')
        table.delete(*table.get_children())
        for row in rows:
            table.insert('', tkinter.END, values=row)