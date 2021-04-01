#Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
#letra. En caso que no se haya inrgesado un letra, indique el error. Ver: módulo string
import string

texto = """
        Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
        letra. En caso que no se haya inrgesado un letra, indique el error. Ver: módulo string
        """

palabras = texto.split()
print("Texto: ", texto)
print("Palabras: ", palabras)

plabras_elegidas = []

letra = input("\nIngrese letra, se buscaran las palabas que inicien con ella, \"FIN\" para terminar ")
while letra != "FIN":
    if letra[0].isalpha() and len(letra) == 1:
        for palabra in palabras:
            if palabra.startswith(letra.lower()) or palabra.startswith(letra.upper()):
                plabras_elegidas.append(palabra)
        if len(plabras_elegidas) > 0:
            print(f"Las palabras que inician con la letra \"{letra}\" son: \n {plabras_elegidas}")
        else:
            print(f"No hay ninguna palabra que empiece con \"{letra}\"")
    else:
        print(f"Error, usted NO ingreso una letra, inrgeso: \"{letra}\", intente nuevamente")

    letra = input("Ingrese letra, se buscaran las palabas que inicien con ella, \"FIN\" para terminar ")
    plabras_elegidas.clear()
    

