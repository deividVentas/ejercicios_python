class Usuarios():
	def __init__(self, nombre, apellidos, twitter, localidad):

		self.nombre = nombre
		self.apellidos = apellidos
		self.twitter = twitter
		self.localidad = localidad
		self.login = 0

	def describe_usuario(self):
		print("El usuario " + self.nombre.title() + " " + self.apellidos.title())
		print("Su twitter " + self.twitter.title())
		print("Se conecta desde... " + self.localidad.title())


	def saludo_usuario(self):
		print("Buenos dias " + self.nombre.title() + " " + self.apellidos.title())
		print("Espero que tengas una feliz visita")
		print("El numero de login es " + str(self.login))


	def incremento_login(self):
		self.login += 1
	

	def reset_login(self):
		self.login = 0


david = Usuarios("David", "Ventas", "@deividventas", "Valencia")
julia = Usuarios("Julia", "Marin", "no tiene", "Valencia")
silvia = Usuarios("Silvia", "Ventas", "no tiene", "Valencia")
laura = Usuarios("Laura", "Ventas", "No tiene", "Valencia")
bernardo = Usuarios("Bernardo", "Ventas", "No tiene", "Valencia")


bernardo.describe_usuario()
bernardo.saludo_usuario()
bernardo.incremento_login()
bernardo.incremento_login()
bernardo.incremento_login()
bernardo.incremento_login()
bernardo.saludo_usuario()
bernardo.reset_login()
bernardo.saludo_usuario(-
	---           )
print(" ")
julia.describe_usuario()
julia.saludo_usuario()
print(" ")
silvia.describe_usuario()
silvia.saludo_usuario()
print(" ")
david.describe_usuario()
david.saludo_usuario()
print(" ")
laura.describe_usuario()
laura.saludo_usuario()