import string
def calc_puntaje_palabra(palabra):
    puntaje = 0
    if palabra.isalpha():
        for letra in palabra:
            puntaje = puntaje + puntajes.get(letra.upper())
    return puntaje

# Diccionario de puntajes por letra de Screbble
puntajes = {}
for i in "AEIOULNRST":
    puntajes[i] = 1
for i in "DG":
    puntajes[i] = 2
for i in "BCMP":
    puntajes[i] = 3
for i in "FHVWY":
    puntajes[i] = 4
puntajes["K"] = 5
for i in "JX":
    puntajes[i] = 8
for i in "QZ":
    puntajes[i] = 10

palabra = input("Ingrese palabra: ")
puntaje = calc_puntaje_palabra(palabra)
if puntaje != 0:
    print(f"La palabra inrgesada es \"{palabra}\" y el puntaje asociado es {puntaje}")
else:
    print(f"La palabra \"{palabra}\" no es válida")