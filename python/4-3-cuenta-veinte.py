numeros = []


# Este codigo muestra algunas funciones para sacar ciertos numeros
# for x in range(0,1000001):
#	numeros.append(x)
# print(min(numeros))
# print(max(numeros))
# print(sum(numeros))


#El siguiente codigo sirve para hacer una cuenta y que no sean numeros correlativos

# for x in range(3,30,3):
#   numeros.append(x)

# print(numeros)



# Nuestro codigo ahora hara el cubo de cada numero entre 1 y 10 ambos incluidos
count = 0
# for cubo in range(1,11):
#  	numeros.append(cubo**3)
#	print("El cubo de ", cubo , " es", numeros[count])
#	count = count + 1



# Este es el mismo codigo que el anterior pero con lista comprensiva,es decir, en una linea todo

cubo  = [x**3 for x in range(1,11)]
print(cubo) 