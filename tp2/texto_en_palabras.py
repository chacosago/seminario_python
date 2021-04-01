def texto_en_palabras(texto):
    """ Esta funcion espera un texto en string y retorna una
    lista de palabras limpias de simbolos
     """
    caracteres = set(texto)
    print(f"caracteres: {caracteres} \n")
    texto_mod = texto
    for car in caracteres:
        if (not car.isalpha()) and (not car.isspace()):
            texto_mod = texto_mod.replace(car," ")
            print(f"caracter a reemplazar: {car} \n")
    return texto_mod.split()