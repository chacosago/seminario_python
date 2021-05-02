import PySimpleGUI as sg
from src.windows import menu
from src.handlers import operaciones
from src.component import archivo_no_encontrado

def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = menu.build()
    
    while True:
        event, _values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit", "-EXIT-"):
            break

        if event == "-TED-":
            try:
                enc, rdo = operaciones.iniciar_consulta(operaciones.ted,"TED_Talk.csv")
            except FileNotFoundError:
                archivo_no_encontrado.start()
                continue

            operaciones.descargar_todas_img(rdo)
            operaciones.guardar_json(rdo,"consulta-ted",enc)
            
        if event == "-ANIME-":

            enc, rdo = operaciones.iniciar_consulta(operaciones.anime,"anime.csv")
            operaciones.guardar_json(rdo,"consulta-anime",enc)

    return window
