import random, os

def validar(matches,images) :
    """Recibe una lista de tuplas y una lista de posiciones
    y retorna un valor de verdad que indica si las tuplas en la posición
    0 son iguales (Si las cartas en esas posiciones coinciden o no)
    """
    j = images[matches[0]]
    coinciden = True 
    for i in matches :
        if images[i][0] != j[0] :
            coinciden = False
            break
    return coinciden

def calcular_coincidencias(cantidad_cartas) :
    """Recibe por parámetro la cantidad de cartas del tablero
    y calcula en base a dicha cantidad las coincidencias compatibles
    para el tamaño dado.
    """
    coincidencias = list()
    if cantidad_cartas % 2 == 0 :
        coincidencias.append("2 coicidencias")
    if cantidad_cartas % 3 == 0 :
        coincidencias.append("3 coicidencias")
    if cantidad_cartas % 5 == 0 :
        coincidencias.append("5 coicidencias")
    return tuple(coincidencias)

def calcular_puntajes(cant_cartas,tiempo_usado,penzalizacion_ayuda) :
    """Recibe por parámetro la cantidad de cartas del tablero, el tiempo 
    empleado en terminar la partida y un coeficiente de penalizacion calculado en 
    base a la cantidad de ayudas usadas, y calcula el puntaje obtenido en la partida
    haciendo uso de estos datos.
    """
    return str( round ((cant_cartas ** 3 / tiempo_usado) * penzalizacion_ayuda ) ) 

def ajustar_texto(nombre) :
    """ Le da a la palabra un formato que permite que se ajuste mejor al boton/carta.
    Como la cantidad de chars que entran en cada línea del botón es 14, nos aseguramos
    de que ninguna línea tenga más de 14 chars y haya como máximo 5 líneas. Así se puede
    visualizar bien la palabra.
    """
    nombre2 = limpiar_string(nombre)
    aux = nombre2.split(" ")
    # genera una lista con tantos con str vacios como palabras haya en el str recibido
    texto_l = ["" for i in range(len(aux))]
    i = 0

    # este for genera una lista de str donde cada uno puede tener a lo sumo 14 chars.
    # cada elemento de la lista será una línea del str resultante
    for palabra in aux :
        # si la palabra tiene mas de 14 chars, 
        if len(palabra) > 14 :
            # si el nombre del anime esta compuesto por mas de una palabra
            if len(texto_l) > 1 :
                texto_l[i] = palabra[:14]
                i+= 1
                texto_l[i] = palabra[14:]
            # si el nombre del anime esta compuesto por una sola palabra
            else :
                texto_l[i] = palabra[:14]
                texto_l.append(palabra[14:])
        # si la palabra es menor o igual a 14 chars
        else :
            # Concateno palabras mientras que el str sea menor o igual a 14 chars
            if (len(palabra + texto_l[i]) + 1 <= 14) :
                texto_l[i] += palabra + " "
            # si la palabra no entra en texto[i], la ubico en la siguiente posición
            else :
                if len(texto_l) > 1 :
                    i+= 1
                    texto_l[i] += palabra + " "
                else :
                    texto_l[0] = palabra

    # nos quedamos con los elementos que no son "" (de la creacion con list comprehension)
    texto_l = texto_l[:i+1]

    # Si hay mas de 5 lineas, nos quedamos solo con las 1ras 5
    # y concatenamos "..." al final de la 5ta linea
    if len(texto_l) > 5 and  texto_l[4] != "" :
        texto_l = texto_l[:5]
        texto_l[4] = texto_l[4][:11] + "..."
    
    return '\n'.join(texto_l)

def limpiar_string(un_string) :
    """Recibe un string y lo retorna sin
    algunos caracteres específicos que no
    admitidos como nombre de archivo.
    """
    otro_string = un_string
    for i in un_string :
        if i in "\/?:*><|\"" :  
            otro_string = otro_string.replace(i,"")
    return otro_string

def generar_lista(rdo,cant_coincidencias) :
    """Recibe una lista con cada línea del archivo de animes en forma de lista
    (lista de listas) y retorna una lista de tuplas donde cada una contiene path de la imágen
    nombre y un string que indica si esta debe ser usada como imágen o como texto, generada con 
    algún criterio y cuyo tamaño es cant_coincidencias (valor recibido por parámetro).
    """
    path_file = os.path.join(os.getcwd(), "src", "files", "images", "" )
    lista = []
    for i in rdo :
        for j in range(cant_coincidencias-1) :
            lista.append((path_file + limpiar_string(i["anime"]) + ".png", i["anime"], "imagen"))
        lista.append((path_file + limpiar_string(i["anime"]) + ".png", i["anime"], "palabra"))
    random.shuffle(lista)
    return lista