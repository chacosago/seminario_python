""" import csv

archi = open('burbujasEscolares.csv','r')

archi_reader = csv.reader(archi, delimiter = ',')
next(archi_reader)

for datos in archi_reader:
    if datos[2] == '4to':
        print (datos[1])    """ 


# Sea a continuación el contenido del archivo burbujasEscolares.csv y un código que manipula esos datos:
# Si ejecuto este código, NO se imprime los nombres de todos los/las docentes de 4to grado. 
# Explicá cuál es el error y proponé una solución para que el código imprima todos los/as docentes de 4to grado.

import csv

archi = open('burbujasEscolares.csv','r')

archi_reader = csv.reader(archi, delimiter = ',')

#next(archi_reader)

for datos in archi_reader:
    if datos[2] == '4to':
        print (datos[1])    

# cierro archivo
archi.close()