class Jugador:
	"""..."""
	def __init__(self, nombre, juego="Tetris", tiene_equipo=False, equipo=False) -> None:
		self.nombre = nombre
		self.juego = juego
		self.tiene_equipo = tiene_equipo
		self.equipo = equipo
	def jugar(self):
		if self.tiene_equipo:
			pass
		else:
			pass

class Deportista:
	def __init__(self, nombre, equipo = "Racing"):
		self.nombre = nombre
		self.equipo = equipo
	def jugar(self):
		print (f"Mi equipo es {self.equipo}")

class JugadorDeFifa(Jugador):
	"""..."""
	def __init__(self, nombre, equipo) -> None:
		Jugador.__init__(self,nombre,"PS4",True,equipo)

class JugadorDeLOL(Jugador):
	"""..."""
	def __init__(self, nombre, equipo) -> None:
		Jugador.__init__(self,nombre,"LOL")
		#super().__init__(nombre,"LOL")
# si uso super(). no necesito usar el parametro self porque super es una
# instancia de la clase padre/base y por eso no necesito pasarle el objeto
# receptor directamente con self.
# super es una instancia no una clase

nico = JugadorDeFifa("Nico","Basilea")
faker = JugadorDeLOL("Faker","SK Telcon")
nico.jugar()
faker.jugar()

# polimorfismo, capacidad de que 2 Obj distintos respondan al mismo mensaje 
# en este caso nico y faker a .jugar()

# variables de instancia vs. variable de clase:
# en el __init__ creo las var  de instancia
# las variables de clase se crean fuera de los métodos
# si las variables inician con _ son "privadas" del objeto

# las propiedades permiten usar las variables de instancia privadas como si 
# fueran publicas, pero internamente estoy usando el get/set/delete
# nombre_propiedad = property(get_variable_inst_priv, set_variable_inst_priv, del_variable_inst_priv, "docstring")

# Decoradores: recordar que un decorador deberia retornar funcion no funcion()

# @decorador permite pasarle la funcion que se define a continuacion a la funcion decorador
# se usa mucho con propiedades

# se usa tmb para defini metodos de clase:
""" @classmethod
def limpio_villanos(cls, confirmo=False): """

# notar que si una variable de instancia empieza con doble _ al intentar acceder desde afuera 
# con objeto.__variable va a dar error, porque el doble _ reeplaza por el nombre de la clase, y 
# podria acceder asi: objeto._NombreClase__variable