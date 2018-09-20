pizzas = ["Margarita", "carne picada", "carbonara"]
pizzas_amigos = pizzas[:]
pizzas.append("especialidad de la casa")
pizzas_amigos.append("silvia")
pizzas_amigos.append("julia")
pizzas_amigos.append("aaron")
pizzas_amigos.append("cristina")
for sabores in pizzas:
	print("Mis pizzas favoritas son, "+ sabores)

for sabores in pizzas_amigos:
	print("Las pizzas favoritas de mis amigos son, "+ sabores)