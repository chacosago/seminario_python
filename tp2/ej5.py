#Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras,
#y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir
#entre mayúsculas y minúsculas.

import procesar_palabras

frase = input("Ingrese una frase: ").lower()
cadena = input("Ingrese la cadena: ").lower()

palabras = procesar_palabras.texto_en_palabras(frase)
cant = 0
seleccionadas = []

for palabra in palabras:
    if cadena in palabra:
        cant+= 1
        seleccionadas.append(palabra)

print(f"Palabras {len(palabras)}: {palabras} \n\nSleccionadas: {seleccionadas}")
print(f"\nLa cantidad de palabras en las que aparece la cadena \"{cadena}\" es: {cant}")
