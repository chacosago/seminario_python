#La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
#es que dado una estructura que dice que celdas tienen minas y que celdas no las tienen, como
#la siguiente:
def mapa_valido(mapa_bombas):
    altura = len(mapa_bombas[0])
    es_invalido = False
    for columna in mapa_bombas:
        if not(len(columna) == altura):
            es_invalido = True
            break
    return not(es_invalido)

def inicializar_mapa_cercanias(mapa_cercanias):
    if mapa_valido(mapa_cercanias):
        for fila in range(len(mapa_cercanias)):
            mapa_cercanias[fila] = mapa_cercanias[fila].replace("-","0")

def imprimir_mapa(mapa_bombas):
    if mapa_valido(mapa_bombas):
        for i in mapa_bombas:
            print(f"{i}\n")

def conversion_a_matriz(mapa_bombas):
    if mapa_valido(mapa_bombas):
        for i in range(len(mapa_bombas)):
            mapa_bombas[i] = list(mapa_bombas[i])

def contar_bombas_alrededor(mapa_bombas,fila,columna):
    """ La funcion espera un mapa de bombas una fila y una columna
    y retorna la cantidad de minas alrededor de dicha celda
    """
    cant_filas = len(mapa_bombas)
    cant_columnas = len(mapa_bombas[0])
    cant_bombas = -1
    if mapa_valido(mapa_bombas) and (fila >= 1 and fila <= cant_filas) and (columna >= 1 and columna <= cant_columnas):
        aux = cant_filas
        aux2 = cant_columnas
        cant_bombas = 0
        fila_ant = fila - 2
        fila_post = fila
        col_ant = columna - 2
        col_post = columna + 1    
        # Caso celda interior
        if (not(fila == 1 or fila == aux)) and (not(columna == 1 or columna == aux2)):
            # Miro fila de arriba
            cant_bombas += mapa_bombas[fila_ant][col_ant:col_post].count("*")
            # Miro fila de abajo
            cant_bombas += mapa_bombas[fila_post][col_ant:col_post].count("*")
            #Miro misma fila:
            cant_bombas+= mapa_bombas[fila_ant+1][col_ant].count("*")
            cant_bombas+= mapa_bombas[fila_ant+1][col_post-1].count("*")
        elif fila == 1 and (columna != 1 and columna != cant_columnas):
        #caso celda en borde: Primer fila
            # Miro fila de abajo
            cant_bombas += mapa_bombas[fila_post][col_ant:col_post].count("*")
            #Miro misma fila:
                #Celda anterior
            cant_bombas+= mapa_bombas[fila_ant+1][col_ant].count("*")
                #Celda posterior 
            cant_bombas+= mapa_bombas[fila_ant+1][col_post-1].count("*")
        elif fila == cant_filas and (columna > 1 and columna < cant_columnas):
        #caso celda en borde: Ultima fila
            # Miro fila de arriba
            cant_bombas += mapa_bombas[fila_ant][col_ant:col_post].count("*")
            #Miro misma fila:
                #Celda anterior
            cant_bombas+= mapa_bombas[fila_ant+1][col_ant].count("*")
                #Celda posterior 
            cant_bombas+= mapa_bombas[fila_ant+1][col_post-1].count("*")
        elif columna == 1 and (fila > 1 and fila < cant_filas):
        #caso celda en borde: Primer columna
            # Miro fila de arriba
            cant_bombas += mapa_bombas[fila_ant][col_ant+1:col_post].count("*")
            # Miro fila de abajo
            cant_bombas += mapa_bombas[fila_post][col_ant+1:col_post].count("*")
            #Miro misma fila:
            cant_bombas+= mapa_bombas[fila_ant+1][col_post-1].count("*")
        elif columna == cant_columnas and (fila > 1 and fila < cant_filas):
        #caso celda en borde: Ultima columna
            # Miro fila de arriba
            cant_bombas += mapa_bombas[fila_ant][col_ant:col_post-1].count("*")
            # Miro fila de abajo
            cant_bombas += mapa_bombas[fila_post][col_ant:col_post-1].count("*")
            #Miro misma fila:
            cant_bombas+= mapa_bombas[fila_ant+1][col_ant].count("*")
        elif columna == 1 and fila ==1:
        #caso celda en borde: Primer celda
            #Miro misma fila:
            cant_bombas+= mapa_bombas[fila_ant+1][col_post-1].count("*")
            # Miro fila de abajo
            cant_bombas += mapa_bombas[fila_post][col_ant+1:col_post].count("*")
        elif columna == cant_columnas and fila ==1:
        #caso celda en borde: Primer fila Ultima columna
            #Miro misma fila:
                #Celda anterior
            cant_bombas+= mapa_bombas[fila_ant+1][col_ant].count("*")
            # Miro fila de abajo
            cant_bombas += mapa_bombas[fila_post][col_ant:col_post-1].count("*")
        
        elif columna == 1 and fila == cant_filas:
        #caso celda en borde: Ultima fila Primer columna
            #Miro misma fila:
            cant_bombas+= mapa_bombas[fila_ant+1][col_post-1].count("*")
            # Miro fila de arriba
            cant_bombas += mapa_bombas[fila_ant][col_ant+1:col_post].count("*")

        elif columna == cant_columnas and fila == cant_filas:
        #caso celda en borde: Ultima fila Ultima columna
            #Miro misma fila:
                #Celda anterior
            cant_bombas+= mapa_bombas[fila_ant+1][col_ant].count("*")
            # Miro fila de arriba
            cant_bombas += mapa_bombas[fila_ant][col_ant:col_post-1].count("*")

    return cant_bombas

def procesar_mapa(mapa_bombas,cant_filas,cant_columnas):
    if mapa_valido(mapa_bombas):
        for fila in range(cant_filas):
            for col in range(cant_columnas):         
                cantidad = contar_bombas_alrededor(mapa_bombas,fila+1,col+1)
                mapa_bombas[fila][col] = mapa_bombas[fila][col] if mapa_bombas[fila][col] == "*" else str(cantidad)
        return True
    else:
        return False


mapa_bombas = [
  '-*---*-',
  '--*----',
  '--**--*',
  '*---*--',
]
mapa_cercanias = [
  '1*3*1',
  '12*32',
  '1212*',
  '*1011',
]

cant_columnas = len(mapa_bombas[0])
cant_filas = len(mapa_bombas)
print(f"Tamaño del mapa fila x columna {cant_filas}x{cant_columnas}")
print(f"Mapa valido? {mapa_valido(mapa_bombas)}")

mapa_cercanias2 = mapa_bombas.copy()
inicializar_mapa_cercanias(mapa_cercanias2)
conversion_a_matriz(mapa_cercanias2)
#fila = 4
#col = 5
#print(f"Bombas alrededor de fila {fila} columna {col}: {contar_bombas_alrededor(mapa_bombas,fila,col)}")
###
procesar_mapa(mapa_cercanias2,cant_filas,cant_columnas)


n = 1
print("\nColumna:12345")
for i in mapa_bombas:
    print(f"fila {n}: {i}")
    n+= 1
n = 1
print("\nMapa de Cercanias")
print("Columna:12345")
for i in mapa_cercanias2:
    print(f"fila {n}: {''.join(i)}")
    n+= 1
