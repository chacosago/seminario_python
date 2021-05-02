import PySimpleGUI as sg

def build():
    """
    Construye la ventana de alerta base no encontrada
    """
    layout = [
        [sg.Text('Error - Base No encontrada - descarguela/descomprima y reintente')],
        [sg.Button('Salir', size=(50, 2), key="-EXIT-")]
    ]

    board = sg.Window('Error - Base No encontrada').Layout(layout)

    return board