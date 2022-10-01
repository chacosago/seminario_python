import os
import requests
from PIL import Image
from io import BytesIO
from src.functions.funcionalidades_tablero import limpiar_string

def descargar_todas(lista_animes):
    """Descarga todas las imágenes mediante la 
    repetida invocación de la funcion descargar imágen
    """
    for anime_d in lista_animes:
        descargar_imagen(anime_d["anime"],anime_d["anime_img"])

def descargar_imagen(nombre, direccion):    
    """Descarga una imágen de la dirección recibida por parámetro
    usando el nombre recibido como parámetro para nombrarla
    """
    path_images = os.path.join(os.getcwd(), "src", "files", "images", "")
    imagen = requests.get(direccion)
    nombre = limpiar_string(nombre)    
    if not os.path.exists(nombre) :   
        im = Image.open(BytesIO(imagen.content))
        im.save(path_images+nombre+".png")