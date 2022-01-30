'''
Las operaciones que tiene la apliación.
'''

import tkinter
from DB.connectdb import DataAccessObject

class Operations:
    def __init__(self):
        self.operation = DataAccessObject()

    #Llenar comobox de escoloridad
    def show_schooling(self):
        try:
            row_schooling = self.operation.show_schooling_db()
        except:
            print('Hubo un error...')
        schooling = []
        for act in row_schooling:
            schooling.append(act[1])
        schooling_tuple = tuple(schooling)
        return schooling_tuple

    def show_activities(self):
        try:
            row_activity = self.operation.show_activites_db()
        except:
            print('Hubo un error...')
        activity = []
        for act in row_activity:
            activity.append(f'{act[1]} ${act[2]}')
        activity_tuple = tuple(activity)
        return activity_tuple


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
            print(client_data[0], client_data[1], client_data[2], client_data[3], client_data[4], client_data[5])
        else:
            print("Creo que falta algo aquí...")
            return