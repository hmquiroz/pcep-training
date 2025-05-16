#Crea una tupla con los nombres de tres ciudades y la población de cada una (en millones). 
#Muestra el nombre de la segunda ciudad y su población utilizando índices y f-strings.

ciudades = (("Madrid", 3.3), ("Paris", 2.1), ("Roma", 2.9))

segundaCiudad = ciudades[1][0]
poblacionCiudad = ciudades[1][1]

print(f"La segunda ciudad en la tupla es {segundaCiudad} con una poblacion de: {poblacionCiudad} millones de personas")