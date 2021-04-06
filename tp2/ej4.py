#Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
#parte de una palabra ingresada:
print("Version original:\n")

cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ ni !:")

if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
cant = 0
for car in cadena:
    if car == "@" or car == "!":
        cant = cant + 1
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Ingreso OK")

#¿Cómo podemos simplificarlo? 
print("Version modificada:\n")

if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
if ("@" in cadena) or ("!" in cadena ):
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Ingreso OK")