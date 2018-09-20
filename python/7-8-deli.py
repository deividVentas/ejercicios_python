sandwich_orden = ["sandokan", "vegetariano", "jamon y queso"]

sandwich_final = []

while sandwich_orden:
	sandwich_actual = sandwich_orden.pop()
	print("Marchando un sandwich de " + sandwich_actual + "\n")

	sandwich_final.append(sandwich_actual)
print("----  Los sandwich totales  ----\n")
for sandwichfinal in sandwich_final:
	
	print(sandwichfinal.title())

