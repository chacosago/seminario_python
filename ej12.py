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

""" def sumar_misma_fila(mapa_bombas,fila):
    if mapa_valido(mapa_bombas):
        for celda in mapa_bombas[fila]:
            if  """


mapa_bombas = [
  '-*-*-',
  '--*--',
  '----*',
  '*----',
]
mapa_cercanias = [
  '1*3*1',
  '12*32',
  '1212*',
  '*1011',
]

print(mapa_bombas, mapa_cercanias)
cant_columnas = len(mapa_bombas)
cant_filas = len(mapa_bombas[0])
print(f"Tamaño del mapa fila x columna {cant_filas}x{cant_columnas}")
print(f"Mapa valido? {mapa_valido(mapa_bombas)}")

mapa_cercanias2 = mapa_bombas.copy()
print(f"Mapa de cercanias:\n")
imprimir_mapa(mapa_cercanias2)


inicializar_mapa_cercanias(mapa_cercanias2)
print(f"Mapa de cercanias inicializado:\n")
imprimir_mapa(mapa_cercanias2)

conversion_a_matriz(mapa_cercanias2)
###
