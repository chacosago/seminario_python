import PySimpleGUI as sg
from src.windows import layout_registarse
from src.functions import guardar_usuario, comprobar_nick_disponible
import os
from src.objects.excepciones import DatosInvalidos,UsuarioNoDisponible

def generar_registrarse():
    """Genera la ventana donde el usuario se registra    
    """      
    ventana_registrarse = layout_registarse.build()  
    while True :
        event,values = ventana_registrarse.read()
        if event in (sg.WINDOW_CLOSED,"-SALIR-") :
                break
        if event in ("\r","-SAVE-") : 
            try :
                path_file = os.path.join(os.getcwd(), "src", "files", "usuarios.json" )
                if os.path.exists(path_file) :
                    comprobar_nick_disponible.comprobar(values)           
                usuario = guardar_usuario.registrar_usuario(values)
            # Si el nickname está ocudado levantamos el error UsuarioNoDisponible y si uno de los datos 
            # ingresados  es inválido se levanta el error DatosInvalidos
            except (DatosInvalidos,UsuarioNoDisponible) :                    
                continue
            break
    ventana_registrarse.close()
    return usuario