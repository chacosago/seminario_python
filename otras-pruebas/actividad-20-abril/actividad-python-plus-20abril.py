#url - "image_url") de los 10 juegos más votados (num_votes).

import csv
import collections

archivo_csv = open("/home/hcastorp/Drive/Facultad/Informatica/Python/TP/actividad-20-abril/bgg_db_1806.csv", "r")
csvreader = csv.reader(archivo_csv, delimiter=',')
# salteo y guardo el encabezado:
encabezado = next(csvreader)
index_max_player = encabezado.index('max_players')
index_category = encabezado.index('category')

juegos_listados = []
juegos_listados = list((filter(lambda x : int(x[index_max_player]) < 3 and 'card game' in x[index_category].lower(), csvreader)))

c = 0
for i in juegos_listados:
    c+=1
    print(f"{c:3d} Nombre: {i[3]:<70} Max jugadores: {i[index_max_player]:<3} Categoria")

# 2)




archivo_csv.close()