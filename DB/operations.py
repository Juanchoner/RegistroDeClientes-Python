'''
Las operaciones que tiene la apliación.
'''
import tkinter
from DB.connectdb import DataAccessObject

class Operations:
    def __init__(self):
        self.operation = DataAccessObject()

    #Operaciones para la tabla
    def show_data_table(self, table):
        '''
        Mostrar los registros que se encuentran en la base de datos.
        Argunmentos
            -table: En que tabla se van a colocar los registros
        '''
        try:
            rows = self.operation.show_costumers_db()
        except:
            print('Ha ocurrido un problema...')
        table.delete(*table.get_children())
        for row in rows:
            table.insert('', tkinter.END, values=row)
        
    def get_cursor(self, table):
        cursor_row = table.focus()
        if len(cursor_row) > 0:
            content = table.item(cursor_row)
            client_data =  content['values']
            print(client_data[0], client_data[1], client_data[2], client_data[4], client_data[5])
        else:
            print("Creo que falta algo aquí...")
            return