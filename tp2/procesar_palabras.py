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

def texto_en_enteros(texto):
    """ Esta funcion espera un listado de numeros en string
    y retorna una lista de enteros
    """
    caracteres = set(texto)
    print(f"caracteres: {caracteres} \n")
    texto_mod = texto
    for car in caracteres:
        if (not car.isnumeric()) and (not car.isspace()):
            texto_mod = texto_mod.replace(car," ")
            print(f"caracter a reemplazar: {car} \n")
    texto_mod2 = texto_mod.split()
    lista_enteros = []
    for i in texto_mod2:
        lista_enteros.append(int(i))
    return lista_enteros