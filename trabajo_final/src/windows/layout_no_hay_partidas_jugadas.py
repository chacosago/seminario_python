import PySimpleGUI as sg

def build(nombre_ventana,color_fondo) :
    layout_sin_valores = [
        [sg.Text("Aun no se han jugado partidas",background_color=color_fondo,font=("Helvetica",20))]
    ]
    return sg.Window(nombre_ventana,layout_sin_valores,background_color=color_fondo,margins=(200,200))