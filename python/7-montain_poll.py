respuestas = {}




polling_active = True

while polling_active:
  name = input("\n Cual es tu nombre? ")
  respuesta = input("Que montaña te gustaria escalar algun dia? ")


  respuestas[name] = respuesta
    
  repite = input("Le gustaria que respondiese otra persona? ")
  if repite == 'no':
    polling_active = False

# Mostrar los datos completos del programa que ha almacenado
print("\n--- Resultados Poll ---")
for name, respuesta in respuestas.items():
  print(name + " le gustaria escalar " + respuesta + ".")
