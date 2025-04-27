nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

#Salida Estandar
#print(nombre, edad)
#print(edad)

#Salida Concatenada
#print("Tu nombre es:", nombre, "tienes:", edad)
#print("Tu nombre es: " + nombre + "tienes: ", edad)

#Salida Format
print("Hola {} tienes {}".format(nombre, edad))

#Salida F String
print(f"Hola {nombre} tienes {edad}")