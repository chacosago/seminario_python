# Escbriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
# misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
# inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
# es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.
# Tener en cuenta - Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean
# letras. - No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos
# la letra “T” y la letra “t” la misma NO será un Hererograma. - Para simplificar el ejercicio vamos
# a tomar como que las letras con tilde y sin tilde son distintas. Ya que Python las diferencia:
# >>> 'u' == 'ú'
# False
# ver Ejemplos

texto = input("Ingrese el texto para chequear si es un heterograma: ").lower()
caracteres_unicos = set(texto)
alfabeticos_unicos_lista = [n for n in caracteres_unicos if n.isalpha()]
print(f"Caracteres alfabeticos unicos: {alfabeticos_unicos_lista}")

es_heterograma = True
contador = 0
for car in alfabeticos_unicos_lista:
    if texto.count(car) > 1:
        es_heterograma = False
        contador+= 1
        break

if es_heterograma:
    print("El texto ingresado SI es Heterograma")
else:
    print(f"El texto ingresado NO es Heterograma. Contador: {contador}")
