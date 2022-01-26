'''
Estilos usuados en la apliación
'''

import tkinter

BACKGROUND = '#121212'
FONT = ('Arial', 16)
COLOR_LETTERS = "#ffffff"

#Título de la apliación
TITLE = {
    "font": ('Arial', 20, 'bold'),
    "bg": "#373e4a",
    "fg": COLOR_LETTERS
}

#Estilos de las etiquetas, cajas de texto y botones
STYLE_LABELS = {
    "font": FONT,
    "bg": BACKGROUND,
    "fg": COLOR_LETTERS
}

STYLE_ENTRYS = {
    "width" : 20,
    "font": FONT
}

STYLE_BUTTONS = {
    "font" : ('Arial', 10)
}

#Estilo de la tabla
STYLE_TABLE = {
    "width" : 180, 
    "anchor" : 'center', 
    "stretch" : 0, 
    "minwidth" : 100
}

#Manera en la que se colocaran las etiquetas y las cajas de texto
PACK_LABELS = {
    "side" : tkinter.TOP,
    "fill" : tkinter.X,
    "padx" : 2,
    "pady" : 2
}

PACK_ENTRYS = {
    "side" : tkinter.TOP,
    "fill" : tkinter.BOTH,
    "padx" : 2,
    "pady" : 2
}

GRID_BUTTONS = {
    "sticky" : tkinter.NSEW,
    "padx" : 5,
    "pady" : 5
}
