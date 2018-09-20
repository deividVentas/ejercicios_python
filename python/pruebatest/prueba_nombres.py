from prueba_nombre_funcion import formato_nombre

print("Pulsa 'q' para salir en cualquier momento")

while True:
	nombre = input("Introduzca su nombre de pila: \n")
    
	if nombre == "q":
		break

	apellidos = input("Introduzca sus apellidos: \n")

	if apellidos == "q":
		break
    
	formato_nombres = formato_nombre(nombre, apellidos)
	print("\tMisteriosamente su formato de nombre es: " + formato_nombres + ".")