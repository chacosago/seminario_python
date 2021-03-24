print("Ingrese texto")
palabra = input()

c= 0
for letra in palabra:
	if letra == "a":
		c = c + 1
	elif letra == "A":
		c = c + 1
		
print(f"La cantidad de letras a en el texto es: {c}")
