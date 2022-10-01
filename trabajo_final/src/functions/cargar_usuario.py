import json
import os

def load(nickname) :
    """Busca y retorna el usuario con el nombre
    recibido por parámetro
    """
    path_file = os.path.join(os.getcwd(), "src", "files", "usuarios.json" )
    usuarios = open(path_file,"r")
    lista_usuarios = json.load(usuarios)
    for i in lista_usuarios :
        if i["Nick"] == nickname :
            usuario = i
            break
    usuarios.close()
    return usuario