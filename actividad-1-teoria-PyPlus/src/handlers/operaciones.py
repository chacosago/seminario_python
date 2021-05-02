import os
import csv
import json
import collections
import requests

# se que estas consultas se podrian implementar de manera mas simple, 
# pero lo hice antes de ver la clase del lunes 26/4. 
# Tambien se que deberia haber hecho mas de un archivo para mantener el criterio de la
# estructura de carpetas que arme, por tema de tiempo no lo rearmo. 

def iniciar_consulta(nombre_consulta,archivo_nom):
    """ La funcion recibe una funcion y un nombre de archivo como parametro y retorna una tupla
    con el encabezado y el resultado de aplicar la consulta correspondiente como lista.
    """
    path_datos = os.path.join(os.getcwd(), "src", "files", "datos", "" )
    archivo = open(path_datos+archivo_nom, "r")
    csvreader = csv.reader(archivo, delimiter=',')
    encabezado = next(csvreader)
    dataset_l = list(csvreader)

    resultado_t = (encabezado, nombre_consulta(encabezado, dataset_l))
    archivo.close()
    return resultado_t

def ted(encabezado, dataset_l):
    """ La funcion recibe como parámetro un encabezado y un dataset que es una lista de filas que
    tmb son listas y consulta en el dataset TED_Talk cuales son las charlas mas vistas de cada
    año y las retorna en una lista de listas.
    """
    index_rdate = encabezado.index("recording_date")
    index_view_count = encabezado.index("view_count")
    index_speaker_name = encabezado.index("speaker__name")

    mas_vista_por_anio_d = {}
    for fila in dataset_l:
        try:
            anio, _mes , _dia = fila[index_rdate].split("-")
            anio = int(anio)
        except:
            continue
        try:
            if int(fila[index_view_count]) > int(mas_vista_por_anio_d[anio][index_view_count]):
                mas_vista_por_anio_d[anio] = fila
        except KeyError:
            mas_vista_por_anio_d[anio] = fila

    return list(mas_vista_por_anio_d.values())

def anime(encabezado, dataset_l):
    """ La funcion recibe como parámetro un encabezado y un dataset que es una lista de filas que
    tmb son listas y consulta asi, en este dataset anime cuales son los 10 anime con mas puntaje del género
    más común  y las retorna en una lista de listas.
    """
    index_punteje = encabezado.index("rating")
    index_genero = encabezado.index("genre")
    generos_l1 = [f[index_genero].lower().replace(" ", "") for f in dataset_l]
    generos_l2 = []
    for i in generos_l1:
        generos_l2.extend((i.split(",")))

    conteo_generos = collections.Counter(generos_l2)
    conteo_generos.pop("")
    animes_genero_ganador = list(filter(lambda x: conteo_generos.most_common()[0][0] in x[index_genero].lower() , dataset_l))
    
    animes_ganador_puntaje = [n for n in animes_genero_ganador if n[index_punteje] != '']

    animes_max_puntaje = (sorted(animes_ganador_puntaje,key= lambda x: float(x[index_punteje]), reverse=True))
    animes_max_puntaje_l = animes_max_puntaje[:10]

    return animes_max_puntaje_l

def guardar_json(lista_guardar,nombre_archivo, encabezado):
    """ Esta funcion recibe una lista de listas, un str, y un encabezado y guarda lo guarda en un archivo
    json cuyo nombre es el str recibido por parametro en y las claves del dict cada elem del encabezado:
    /src/files/salidas/nombre_archivo.json  ¡Sobreescribe!.
    """
    path_salida = os.path.join(os.getcwd(), "src", "files", "salidas", "" )
    datos_estruct = []
    for fila in lista_guardar:
        diccionario = {}
        for elem,clave in zip(fila,encabezado):
            diccionario[clave] = elem 
        datos_estruct.append(diccionario)
    
    archivo_salida = open(path_salida + f"{nombre_archivo}.json", "w")
    json.dump(datos_estruct, archivo_salida, indent=4)
    archivo_salida.close()

def descargar_imagen(nombre, direccion):
    """esta funcion espera un str que va a ser el nombre del archivo a descargar y un str de la
    url de donde descargar la imagen. Guarda la imagen en /src/files/salidas/nombre.jpg
    """
    path_datos = os.path.join(os.getcwd(), "src", "files", "salidas", "" )
    imagen = requests.get(direccion)
    archivo = open(f"{path_datos+nombre}.jpg", "wb")
    archivo.write(imagen.content)
    archivo.close()

def descargar_todas_img(lista):
    """Esta funcion descarga todas las fotos de una lista que recibe como parametro
    con el formato: lista[i] = charla i; lista[i][0] = año de la charla y 
    lista[i][1] = lista con la fila del csv.
    """
    # l[1][11] = speaker__name
    # l[1][32] = url_imagen
    for l in lista:
        try:
            descargar_imagen(l[1][11],l[1][32])
        except:
            continue