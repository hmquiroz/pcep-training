#Solicita al usuario que ingrese su nombre y edad. Crea una tupla con esos datos y muestra por consola el mensaje "Hola, [nombre]. Tienes [edad] años." utilizando f-strings.

nombre = input("Por favor, ingrese su nombre: ")
edad = int(input("Por favor, ingrese su edad: "))

datosUsuario = (nombre, edad)

print(f"Hola, {datosUsuario[0]}. Tienes {datosUsuario[1]} años.")