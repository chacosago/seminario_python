import PySimpleGUI as sg
from src.windows import layout_menu
from src.components import generador_estadisticas, generador_puntajes, generar_tablero, generar_configuracion, generador_ayuda

def generar_menu(usuario) :
    """Genera la ventana de menú
    """
    ventana_menu = layout_menu.build(usuario) 
    while True :
        event,_values = ventana_menu.read()
        if event == sg.WINDOW_CLOSED :
            exit()
        if event == "-SALIR-" :
            break     
        if event == "-PLAY-" :
            ventana_menu.hide()
            generar_tablero.generar_tablero(usuario)
            ventana_menu.un_hide()   
        if event == "-CONFIG-" :
            #ventana_menu.hide()
            ventana_menu.close()
            generar_configuracion.generar_configuracion(usuario)       
            ventana_menu = layout_menu.build(usuario)
            #ventana_menu.un_hide() 
        if event == "-PUNTAJES-" :
            ventana_menu.hide()
            generador_puntajes.generar_ventana_puntajes(usuario)
            ventana_menu.un_hide()          
        if event == "-STATS-" :
            ventana_menu.hide()
            generador_estadisticas.generar_ventana_estadisticas(usuario)            
            ventana_menu.un_hide() 
        if event == "-HELPMENU-" :
            ventana_menu.hide()
            generador_ayuda.generar_ventana_ayuda(usuario["Configuracion"]["Color_fondo"],usuario["Configuracion"]["Color_botones"])            
            ventana_menu.un_hide()
    ventana_menu.close()
