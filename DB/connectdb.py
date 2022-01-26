import sqlite3
from pathlib import Path

class DataAccessObject:
    def __init__(self):
        try:
            ruta = Path(__file__).parent.resolve()
            database = f'{ruta}\\clientes.db'
            self.con = sqlite3.connect(database)
        except:
            print(f'Error :( {ruta}\n {database}')

    def show_costumers_db(self):
        cur = self.con.cursor()
        information_costumers_db = '''SELECT clientes.nombre, clientes.domicilio, 
                                    escolaridades.escolaridad, clientes.telefono, actividades.nombre, clientes.vencimiento
                                    FROM clientes
                                    INNER JOIN escolaridades ON clientes.escolaridad = escolaridades.id_escolaridad
                                    INNER JOIN actividades ON clientes.actividad = actividades.id_actividad;'''
        cur.execute(information_costumers_db)
        datos = cur.fetchall()
        return datos

    def search_costumer_db(self, id_cliente):
        cur = self.con.cursor()
        search_costumer = f"""SELECT * FROM clientes
                            WHERE id_cliente = {id_cliente}"""
        cur.execute(search_costumer)
        costumer = cur.fetchall()
        return costumer
     
    def insert_costumer_db(self, nombre, domicilio, escolaridad, telefono, actividad, vencimiento):
        cur = self.con.cursor()
        insert_costumer = f"""INSERT INTO 'main'.'clientes'
                            ('nombre', 'domicilio', 'escolaridad', 'telefono', 'actividad', 'vencimiento')
                            VALUES ('{nombre}', '{domicilio}', {escolaridad}, '{telefono}', {actividad}, '{vencimiento}');"""
        cur.execute(insert_costumer)
        self.con.commit()

    def update_costumer_db(self, id_cliente, nombre, domicilio, escolaridad, telefono, actividad, vencimiento):
        cur = self.con.cursor()
        upadate_costumer = f"""UPDATE clientes
                            SET nombre='{nombre}', domicilio='{domicilio}', escolaridad='{escolaridad}',
                            telefono='{telefono}', actividad='{actividad}', vencimiento = '{vencimiento}'
                            WHERE id_cliente = {id_cliente};"""
        cur.execute(upadate_costumer)
        self.con.commit()

    def delete_costumer_db(self, id_cliente):
        cur = self.con.cursor()
        delete_costumer = f"""DELETE FROM clientes
                            WHERE id_cliente = '{id_cliente}'"""
        cur.execute(delete_costumer)
        self.con.commit()

    def show_schooling_db(self):
        cur = self.con.cursor()
        show_schooling = '''SELECT * FROM escolaridades'''
        cur.execute(show_schooling)
        schooling = cur.fetchall()
        return schooling

    def show_activites_db(self):
        cur = self.con.cursor()
        show_activites = '''SELECT * FROM actividades'''
        cur.execute(show_activites)
        activites = cur.fetchall()
        return activites
