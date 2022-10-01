import os
import random
import csv
import datetime

def load() :
    """Esta funcion retorna una lista con el resultado de aplicar la
    consulta que se determina segun un criterio basado en el dia/horario. La lista
    contiene los datos necesarios para obetener palabras/imagenes para
    el tablero.
    """
    maniana = (0, 12)
    dia = datetime.datetime.now().weekday()
    hora = datetime.datetime.now().hour
    es_maniana = hora in maniana
    resultado, generos_t = consultar(dia,es_maniana)
    return (resultado, generos_t)

def consultar(dia,es_maniana) : 
    """Genera un una lista de animes en base a dos géneros de animes que varías según
    el día, y dependiendo de si se está en la primer mited del día o en la segunda
    se seleccionarán para dicha lista los animés que tengan una puntuación por encima
    o por debajo debajo del promedio.
    """
    path_base = os.path.join(os.getcwd(), "src", "files", "animes.csv")
    with open(path_base, "r",encoding="utf8") as archivo:
        reader = csv.reader(archivo)
        encabezado = next(reader)
        generos = encabezado[encabezado.index("genre_action"):]
    with open(path_base, "r",encoding="utf8") as archivo:
        reader = csv.DictReader(archivo)
        genero_1_ind = dia * 4
        genero_elegido = random.randint(genero_1_ind,genero_1_ind+3) 
        while True :
            genero_elegido_2 = random.randint(genero_1_ind,genero_1_ind+3)    
            if genero_elegido != genero_elegido_2 :
                break  
        rdo_dia = list(filter(lambda x: float(x[generos[genero_elegido]]) == 1 or float(x[generos[genero_elegido_2]]) == 1 ,reader))
        # guardamos los nombres de los generos elegidos para mostrarlos en el tablero
        generos_t = (generos[genero_elegido][6:],generos[genero_elegido_2][6:])
    promedio = sum([float(item["rate"]) for item in rdo_dia]) / float(len(rdo_dia))
    return (list(filter(lambda x: float(x["rate"]) < promedio ,rdo_dia)),generos_t) if es_maniana else (list(filter(lambda x: float(x["rate"]) > promedio ,rdo_dia)),generos_t)
    