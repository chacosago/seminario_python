#prueba 1
saludo = "hola mundo"
saludo2 = "chau mundo"
numero = 1
#print(saludo)
print(type(numero))
print(type(saludo))
print(len(saludo))

menu = """ Menu miren
            1. opcion A
            2. opcion B
            3. opcion C
        """
print(menu)  

print(saludo)
print(saludo2)

print(saludo + " " + saludo2)
print(saludo[-1])

saludo_cortado1 = saludo[:4]
saludo_cortado2 = saludo[5:]
print(saludo_cortado1)
print(saludo_cortado2)
print(saludo.upper())

#cadena = input("Ingrese texto a dividir por espacios")
#print(cadena.split(" "))

print(menu.count("n"))

print(type(range(3)))

for i in range(5):
    print(f"Indice: {i}")

nombre = input("Ingrese su nombre ")
edad = int (input("Ingrese su edad "))
print("Hola Sr./Sra. {} su edad es {}, saludos".format(nombre,edad))
