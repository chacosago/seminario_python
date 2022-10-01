import PySimpleGUI as sg
from src.windows import layout_login
from src.components import generador_menu, generador_registrarse, generador_ayuda
from src.functions import cargar_usuario

def generar_login():
    """Genera la ventana de login, donde el usuario
    puede elegir entre iniciar sesión , registrarse
    o ver la ventana de ayuda.
    """
    color_fondo = "#45B39D"
    color_botones = "#3498DB"
    ventana_login = layout_login.build()
    dimensiones = ventana_login.get_screen_size()
    if dimensiones[0] < 1920 or dimensiones[1] < 1080 :
        ventana_login["-ADVERTENCIA-"].update("Algunos tamaños de tablero no se\nvisualizarán correctamente en\ntu monitor.")
    while True :
        event,values = ventana_login.read()
        if event in (sg.WINDOW_CLOSED,"-EXIT-") :
                break
        if event in ("\r","-ENTER-")  :            
            #validacion del nick name debería retornar al usuario  
            try:
                ventana_login.hide()
                usuario = cargar_usuario.load(values["-NICK-"])
                generador_menu.generar_menu(usuario)
                ventana_login["-NICK-"].update("")
                ventana_login.un_hide()
            except (UnboundLocalError, FileNotFoundError) :
                ventana_login.un_hide()   
                sg.popup("Este nombre de usuario no está registrado.",title="Error al iniciar sesión",background_color=color_fondo,
                    font=("Helvetica",15), button_color=color_botones)      
        if event == "-REGISTER-" :
            try:
                ventana_login.hide()   
                ventana_login["-NICK-"].update("")             
                usuario = generador_registrarse.generar_registrarse()
                generador_menu.generar_menu(usuario)          
                ventana_login.un_hide()
            except UnboundLocalError :
                ventana_login.un_hide()  
        if event == "-HELP-" :
            ventana_login.hide()
            generador_ayuda.generar_ventana_ayuda(color_fondo,color_botones)            
            ventana_login.un_hide()

    ventana_login.close()
