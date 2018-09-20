class Restaurante():
	def __init__(self, nombre, tipo_cocina):
		self.nombre = nombre
		self.tipo_cocina = tipo_cocina


	def descripcion_restaurante(self):
		print("El restaurante " + self.nombre.title())
		print("Tiene un tipo de comida calificado como " + self.tipo_cocina)

	def apertura_restaurante(self):
		print("El restaurante " + self.nombre.title() + " esta abierto.")

""" Esto se llama instanciar las clases extension ejercicio 9-2 tres instancias"""
restaurante = Restaurante("Gallego ", "comida gallega")
chino = Restaurante("Kin yon", "comida china")
laferraura = Restaurante("La Ferraura", "comida valenciana")

chino.descripcion_restaurante()
laferraura.descripcion_restaurante()

restaurante.descripcion_restaurante()
restaurante.apertura_restaurante()