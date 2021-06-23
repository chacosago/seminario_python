#Información de cada equipo: entrenador, integrantes
equipos = {
            "A": ['Jose', ['Carla', 'Helena', 'Rocío', 'Carmen']],
            "B": ['Josefa', ['Justina', 'Clara', 'Amalia', 'Ana', 'Melani']],
            "C": ['Rosana', ['Laura', 'Eugenia',  'Ana']]
            }
            
# def agrego_integrante(equipos, equipo):
#     try:
#         nombre = input('Ingresá nombre del /de la nueva/o integrante:  ')
#         equipos[equipo][1].append(nombre)
#     except ValueError:
#         print ('Usp.. se produjo un error con el equipo!')
        
# def mostrando_equipo(equipos, equipo):
#     return equipos[equipo][1]
        
# #Gestionando los equipos
# try:
#     resp = input('¿Querés seguir gestionando los equipos? (S/N)   ').upper()
#     while resp == 'S':
#         eq = input ('Ingresá el nombre del equipo (A, B o C) con el querés trabajar:  ').upper()
#         opcion = input("""Elige una opción: 
#                     1.- Agregar integrantes a ese equipo
#                     2.- Mostrar integrantes de ese equipo    """)
#         if opcion == '1':               
#             agrego_integrante(equipos, eq)
#         elif opcion == '2':
#             print(mostrando_equipo(equipos, eq))
#         ##
#         resp = input('¿Querés seguir gestionando los equipos? (S/N)   ').upper()            
# except:
#     print('Ups aglún error se produjo en algún lado!..' )


# Analizá el código y decí qué es lo que hace, explicando en qué casos se pueden llegar a ejecutar
# los manejadores de excepciones y por qué. Proponé una modificación mínima al programa para que en
# el caso de que se produzca un error con el diccionario, el programa saque un mensaje pero sigue su ejecución.

def agrego_integrante(equipos, equipo):
    try:
        nombre = input('Ingresá nombre del /de la nueva/o integrante:  ')
        equipos[equipo][1].append(nombre)
    except ValueError:
        print ('Usp.. se produjo un error con el equipo!')
        
def mostrando_equipo(equipos, equipo):
    return equipos[equipo][1]
        
#Gestionando los equipos

resp = input('¿Querés seguir gestionando los equipos? (S/N)   ').upper()
while resp == 'S':
    try:
        eq = input ('Ingresá el nombre del equipo (A, B o C) con el querés trabajar:  ').upper()
        opcion = input("""Elige una opción: 
                    1.- Agregar integrantes a ese equipo
                    2.- Mostrar integrantes de ese equipo    """)
        if opcion == '1':               
                agrego_integrante(equipos, eq)
        elif opcion == '2':
                print(mostrando_equipo(equipos, eq))
    except KeyError:
        print('Ups aglún error se produjo en algún lado!..' )      
    resp = input('¿Querés seguir gestionando los equipos? (S/N)   ').upper()            
