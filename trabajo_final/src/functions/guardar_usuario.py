import json
import os
import PySimpleGUI as sg
from src.objects.excepciones import DatosInvalidos 

def validar_datos(values) :
    """Recibe un diccionario y verifica que los datos para las claves '-NICKNAME-',
    '-AGE-', '-GEN0-', '-GEN1-' y '-GEN2-' sean válidos, de no ser así, lanzará la 
    excepción TypeError.
    """
    color_fondo = "#45B39D"
    color_botones = "#3498DB"

    if values["-NICKNAME-"].isnumeric() or len(values["-NICKNAME-"]) < 3 or values["-NICKNAME-"][0] == " " :
        sg.popup("El nombre ingresado no es válido.",title="Datos inválidos",font=("Helvetica",15),
            background_color=color_fondo,button_color=color_botones)
        raise DatosInvalidos        
    if len(values["-NICKNAME-"]) > 14 :
        sg.popup("El nombre ingresado es demasiado largo.",title="Datos inválidos",font=("Helvetica",15),
            background_color=color_fondo,button_color=color_botones)
        raise DatosInvalidos        
    if not values["-AGE-"].isnumeric() or values["-AGE-"] == "" or  int(values["-AGE-"]) > 99:
        sg.popup("La edad ingresada no es válida.",title="Datos inválidos",font=("Helvetica",15),
            background_color=color_fondo,button_color=color_botones)
        raise DatosInvalidos   
    if not (values["-GEN0-"] or values["-GEN1-"] or values["-GEN2-"]) :  
        sg.popup("Debe seleccionar un género.",title="Datos inválidos",font=("Helvetica",15),
            background_color=color_fondo,button_color=color_botones)  
        raise DatosInvalidos

def registrar_usuario(values) :
    """Esta funcion guarda un usuario nuevo: lo agrega si no existe,
    lo modifica si existe y crea el archivo json si dicho archivo no existe"""
    validar_datos(values)
    path_file = os.path.join(os.getcwd(), "src", "files", "" )
    try :
        usuarios = open(path_file+"usuarios.json","r")
        lista_usuarios = json.load(usuarios)
        usuarios.close()
    except FileNotFoundError :   
        lista_usuarios = []
    dic = dict()
    dic["Nick"] = values["-NICKNAME-"]
    dic["Edad"] = values["-AGE-"]
    choices = [("Mujer","-GEN0-"),("Hombre","-GEN1-"),("Otro","-GEN2-")]
    for i in choices :
        if values[i[1]] : 
            dic["Género"] = i[0]

    config = dict()
    config["Ancho"] = 4
    config["Alto"] = 3
    config["Coincidencias"] = "2 coincidencias"
    config["Tiempo"] = 50
    config["Color_fondo"] = "#45B39D"
    config["Color_botones"] = "#3498DB"
    config["Tipo_coincidencias"] = "Imagen/Imagen"
    config["Mensaje_ganaste"] = "¡Felicidades!"
    config["Mensaje_perdiste"] = "¡Que lástima!"
    config["Ayuda"] = False
    dic["Configuracion"] = config

    lista_usuarios.append(dic)
    usuarios = open(path_file+"usuarios.json","w")
    json.dump(lista_usuarios,usuarios,indent=4)
    usuarios.close()
    return dic
    


