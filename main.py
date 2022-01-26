'''
Aplicacion de escritorio la cual, es un CRUD para clientes con widgets de formulario y
tabla (vista de clientes registrados).
'''

from manager import Manager

if __name__ == "__main__":
    app = Manager()
    app.geometry('1330x600+0+0')
    app.mainloop()