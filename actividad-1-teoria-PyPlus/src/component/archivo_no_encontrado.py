import PySimpleGUI as sg
from src.windows import archivo_no_encontrado


def start():
    """
    Lanza la ejecución de la ventana de Base no encontrada
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    
    window = archivo_no_encontrado.build()
    
    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-EXIT-"):
            break
            
    return window
