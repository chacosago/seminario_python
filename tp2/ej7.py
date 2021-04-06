# Copiar el contenido de los archvios en variables de tipo string y realizar.
# 1. generar una estructura con los nombres de los estudiantes y la suma de ambas.
# 2. Calcular el promedio de las notas totales e informar quiénes obtuvieron menos que el promedio notas. 


import procesar_palabras

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

nombres_lista = procesar_palabras.texto_en_palabras(nombres_str.lower())

eval1_int = procesar_palabras.texto_en_enteros(eval1_str)
eval2_int = procesar_palabras.texto_en_enteros(eval2_str)

# Inciso 1:
#forma 1, armando manualmente las tuplas:
nombres_y_suma_eval = []
for estudiante in nombres_lista:
    nombres_y_suma_eval.append((estudiante, eval1_int[nombres_lista.index(estudiante)] 
    + eval2_int[nombres_lista.index(estudiante)]))

#forma 2, usando la estructura ZIP:
nombres_y_suma_eval2 = []
for nota1, nota2, nombre in zip(eval1_int,eval2_int,nombres_lista):
    nombres_y_suma_eval2.append((nombre,sum([nota1,nota2])))

print(f"forma 1:\n{nombres_y_suma_eval}\n\nforma 2:\n{nombres_y_suma_eval2}")


# Inciso 2:
suma_total = 0
for estudiante in nombres_y_suma_eval2:
    suma_total+= estudiante[1]

promedio = int((suma_total / len(nombres_lista)) / 2)
print(f"\nEl promedio es: {promedio}\n")

#
for estudiante in nombres_y_suma_eval2:
    if int(estudiante[1] / 2) < promedio:
        print(f"El estudiante {estudiante[0]} obtuvo {estudiante[1] / 2} que es menor al promedio\n")