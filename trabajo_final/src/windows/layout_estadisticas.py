import PySimpleGUI as sg
import os

path_images = os.path.join(os.getcwd(), "src", "images", "" )

def build (color_fondo,color_botones,opciones) :    
                layout = [[sg.Text('Elija el gráfico:',background_color=color_fondo),sg.InputCombo(opciones,key = "-OP-",
                        size=(40,6),enable_events=True,readonly=True,default_value="Ninguno",background_color=color_botones,)],
                [sg.Canvas(key='-CANVAS-')],
                [sg.Button('Salir',key="-SALIR-")]]
                return sg.Window("Estadisticas",layout,background_color=color_fondo,button_color=color_botones,finalize=True,
                         element_justification='center', font='Helvetica 20',size=(900,600),margins=(50,50))

    
