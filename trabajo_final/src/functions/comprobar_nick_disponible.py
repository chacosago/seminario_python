import os
import PySimpleGUI as sg 
import json
from src.objects.excepciones import UsuarioNoDisponible

def comprobar (values) :
    """Itera sobre el archivo de usuarios y comprueba
    si el nick name en values["-NICKNAME-"] (diccionario 
    recibido por parámetro) está ya registrado o no.
    En caso de estar registrado levanta la excepción nameError.
    """
    color_fondo = "#45B39D"
    color_botones = "#3498DB"
    path_file = os.path.join(os.getcwd(), "src", "files", "" )  
    usuarios = open(path_file+"usuarios.json","r")
    lista_usuarios = json.load(usuarios)
    usuarios.close()
    for i in lista_usuarios :
        if i["Nick"] == values["-NICKNAME-"] :
            sg.popup("El nombre elegido no se encuentra disponible",title="Nombre no disponible",font=("Helvetica",15),
                background_color=color_fondo,button_color=color_botones)
            raise UsuarioNoDisponible