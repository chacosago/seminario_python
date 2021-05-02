import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú
    """
    layout = [
        [sg.Button('Charlas TED', size=(50, 2), key="-TED-")],
        [sg.Button('Animes', size=(50, 2), key="-ANIME-")],
        [sg.Button('Salir', size=(50, 2), key="-EXIT-")]
    ]

    board = sg.Window('Actividad 1 x PythonPlus - Teoría').Layout(layout)

    return board