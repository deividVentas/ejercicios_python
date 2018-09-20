class Restaurante():
	def __init__(self, nombre, tipo_cocina):
		self.nombre = nombre
		self.tipo_cocina = tipo_cocina
		self.numero_servido = 0

	def describe_restaurante(self):
		print("El restaurante " + self.nombre.title())
		print("Tiene estilo de comida " + self.tipo_cocina.title())

	def open_restaurante(self):
		print("El restaurante " + self.nombre.title() + " esta abierto.")

	""" Modificaciones de un atributo de varias formas, a lo bruto, modificando con otro metodo, o incrementando """
	def restaurante(self):
		print("El numero servido es " + str(self.numero_servido))

	""" Modificando el valor desde el metodo"""
	def set_numero_servido(self, servicios):
		self.numero_servido = servicios 


	""" Incrementando el valor desde un metodo """
	def incremento_numero_servicios(self,servicios):
		self.numero_servido += servicios
    	

chino = Restaurante("kin young", "china")
chino.describe_restaurante()
chino.open_restaurante()

""" A lo bruto, llamas al atributo de la clase y lo seteas."""
chino.numero_servido = 100
chino.restaurante()
print(" ")

anden = Restaurante("El anden", "bar restaurante")
anden.describe_restaurante()
anden.open_restaurante()
""" Modificando el valor desde el metodo """
anden.set_numero_servido(120)
anden.restaurante()
print(" ")

gallego = Restaurante("El gallego", "gallega")
gallego.describe_restaurante()
gallego.open_restaurante()

""" Incrementando el valor desde el metodo"""
gallego.incremento_numero_servicios(23)
gallego.incremento_numero_servicios(37)
gallego.restaurante()
print(" ")

ferraura = Restaurante("La ferraura", "tipica valenciana")
ferraura.describe_restaurante()
ferraura.open_restaurante()
