'''
Las operaciones que tiene la apliación.
'''


import tkinter
from DB.connectdb import DataAccessObject

class Operations:
    def __init__(self):
        self.operation = DataAccessObject()

    def transfrom_schooling(self):
        '''
        Invierte los grados academicos para que a la hora de un registro
        se mande el ID de la escolaridad
        '''
        try:
            row_schooling = self.operation.show_schooling_db()
        except:
            print('Hubo un error...')
        schooling = dict()
        for act in row_schooling:
            schooling.setdefault(act[1], act[0])
        return schooling

    def transform_activities(self):
        '''
        Invierte el nombre de la actividad con su ID para que a la hora de un registro
        se mande el ID de la actividad
        '''
        try:
            row_activity = self.operation.show_activites_db()
        except:
            print('Hubo un error...')
        activity = dict()
        for act in row_activity:
            activity.setdefault(f'{act[1]} ${act[2]}', act[0])

        return activity

    def show_schooling(self):
        '''
        Rellena el comobox de escolaridad con los datos que se
        encuentran en la base de datos.
        '''
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
        '''
        Rellena el comobox de actividades con los datos que se
        encuentran en la base de datos.
        '''
        try:
            row_activity = self.operation.show_activites_db()
        except:
            print('Hubo un error...')
        activity = []
        for act in row_activity:
            activity.append(f'{act[1]} ${act[2]}')
        activity_tuple = tuple(activity)
        return activity_tuple



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
        
    def create_refernce(self, table):
        '''
        Se crea una referencia para la tabla donde se muestra a los clientes, 
        con el fin de poder actualizar la tabla a la hora de ejecutar acciones.
        Argumantos:
            -table: La tabla a la que se le hace referencia
        '''
        self.referencia = table

    def refresh_table(self):
        '''
        Refresca la tabla para mostra los nuevos registros.
        '''
        self.show_data_table(self.referencia)

    def get_cursor(self, table):
        '''
        Al seleccionar a un cliente en la tabla este la manda a Entrys de 
        los formularios
        Argumentos:
            -table: De que tabla se están seleccionado al cliente
        '''
        cursor_row = table.focus()
        if len(cursor_row) > 0:
            content = table.item(cursor_row)
            client_data =  content['values']
            return client_data
        else:
            client_data = []
            return client_data

    def registration(self, data, school, activity):
        '''
        Valida la infromación que se mandará a la base de datos
        Arguentos:
            -data: Los datos que se encuentran en los StringVar
            -school: Escolaridad invertido 'grado':id
            -activity: Actividades invertidas 'actividad':id
        '''
        for key, value in data.items():
            if value.get() == '':
                return f'El campo {key} esta vacio...'
        if not len(data['telefono'].get()) == 10:
            return 'Verifique el formato del nuemro de telefono...'

        id_school = school.get(data['escolaridad'].get())


        id_activity = activity.get(data['actividad'].get())
        
        self.operation.insert_costumer_db(data['nombre'].get(), data['domicilio'].get(), id_school, 
        data['telefono'].get(), id_activity, data['vencimiento'].get())
        self.refresh_table()
        return f'Cliente registrado'
