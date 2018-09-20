class Dog():
	""" Simple intento de modelar un perro"""


	def __init__(self, name, age):
		""" Inicializar los atributos nombre, y edad"""


		self.name = name
		self.age = age


	def sit(self):

		""" Simula que un perro se sienta a la respuesta de un comando """
		print(self.name.title() + " esta ahora sentado.")


	def roll_over(self):
		""" Simula que un perro se mueve a la respuesta de un comando"""

		print(self.name.title() + " esta ahora moviendose")


""" Forma de mandar informacion a la clase Dog, y forma de acceder a los datos de la clase esto se llama instancia """
mi_perro = Dog('Sultan','10')

print("Mi perro se llama " + mi_perro.name.title() + " y tiene " + mi_perro.age.title() + " años.")

""" Forma de acceder a los metodos de la clase tanto sit como roll_over """
mi_perro.sit()
mi_perro.roll_over()