# Con la información de los archivos de texto que se encuentran disponibles en el curso:
# nombres_1
# nombres_2
# Nota: Trabaje con los datos en variables de tipo string

# 1. Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
# 2. Genere dos variables con la lista de notas que se incluyen en los archivos: eval1.txt y eval2.txt
# e imprima con formato los nombres de los estudiantes con las correspondientes nota y la suma de ambas
# como se ve en la imagen:

from texto_en_palabras import texto_en_palabras
from texto_en_palabras import texto_en_enteros
nombres_str = """'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
"""

nombres_1 = """'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
 """

nombres_2 = """'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
 'Tomás',
 'Ulises',
 'Yanina'
 """

eval1_str = """
 81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74,
 """

eval2_str = """
 30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10,
 """

# Preparo los datos en listas:
nombres_lista = texto_en_palabras(nombres_str.lower())
nombres_1_lista = texto_en_palabras(nombres_1.lower())
nombres_2_lista = texto_en_palabras(nombres_2.lower())
eval1_int = texto_en_enteros(eval1_str)
eval2_int = texto_en_enteros(eval2_str)

""" digitos = string.digits
codigos = [ord(n) for n in digitos]

cuadrados = [num**2 for num in range(10) if num % 2 == 0] """

# Inciso 1:
nombres_unicos = set(nombres_1_lista + nombres_2_lista) 
nombres_repetidos = [n for n in nombres_unicos if (n in nombres_1_lista) and (n in nombres_2_lista)]

print(len(nombres_unicos), len(nombres_1_lista), len(nombres_2_lista), len(eval1_int), len(eval2_int))

print(f"nombres1:\n{nombres_1_lista}\n\nnombres2:\n{nombres_2_lista}\n")
print(f"Nombres repetidos {len(nombres_repetidos)}:\n{nombres_repetidos}")

# Inciso 2:

t0= "Tabla de alumnos"
t1 = "Nombre"
t2 = "Eval1"
t3 = "Eval2"
t4 = "Total"
print(f"\n{t0:*^45}\n")
print(f" # {t1:<15}{t2:^10}{t3:^10}{t4:^10}")

for i in range(len(nombres_lista)):
    print(f"{i:2d} {nombres_lista[i].capitalize():<15}{eval1_int[i]:^10}{eval2_int[i]:^10}{eval1_int[i]+eval2_int[i]:^10}")

