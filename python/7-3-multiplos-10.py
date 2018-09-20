posible_multiplo = input("Introduzca un número para ver si es o no múltiplo de 10... ")
posible_multiplo = int(posible_multiplo)


if posible_multiplo > 10:
  if posible_multiplo % 10 == 0:
  	print("El número es múltiplo de 10")

  else:
  	print("EL número no es múltiplo de 10")

else:
	print("Debes introducir números más altos que 10")