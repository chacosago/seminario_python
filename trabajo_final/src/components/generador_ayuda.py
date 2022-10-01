import PySimpleGUI as sg
from src.windows import layout_ayuda

def generar_ventana_ayuda(color_fondo,color_botones):    
    """Genera la ventana  de ayuda donde se muestra de que trata el juego
    y como se calcula el puntaje.
    Tiene el bucle que da funcionalidad a la ventana y espera eventos.
    No retorna nada.
    """    
    ventana_ayuda = layout_ayuda.build(color_fondo,color_botones)
    while True :
        event,_values = ventana_ayuda.read()
        if event in (sg.WINDOW_CLOSED,"-VOLVER-") :
            break
    ventana_ayuda.close()