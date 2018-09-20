salida = ""
while (salida != "quit"):
  edad = input("Buenos dias al sistema de entradas, por favor introduzca su edad para ver el precio del ticket\n")
  edad = int(edad)

  if (edad < 3):
    	print("El precio de la entrada de niños es gratuita")
  elif (edad >= 3) and (edad < 12):
    	print("El precio de infantil es de 10 euros")
  else:
	    print("El precio de la entrada general es de 15 euros")
  salida = input("Si desea puede salir del programa escribiendo quit\nsi no desea salir, aprete intro\n")