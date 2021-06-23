import csv

ruta = "/home/hcastorp/Drive/Facultad/Informatica/Python/TP/otras-pruebas/actividad-20-abril/bgg_db_1806.csv"

archivo_csv = open(ruta, "r")
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
    print(f"{c:3d} Nombre: {i[3]:<70} Max jugadores: {i[index_max_player]:<3}")

# 2) hecho
archivo_csv = open(ruta, "r")
csvreader = csv.reader(archivo_csv, delimiter=',')
# salteo y guardo el encabezado:
encabezado = next(csvreader)

index_max_num_votes = encabezado.index('num_votes')
index_image_url = encabezado.index('image_url')

juegos_listados2 = sorted(csvreader,key = lambda col : int(col[index_max_num_votes]), reverse = True)

c = 0
for i in juegos_listados2[:10]:
    c+=1
    print(f"{c:3d} Votos:{i[index_max_num_votes]:<7} Nombre: {i[3]} Imagen: {i[index_image_url]}")

archivo_csv.close()