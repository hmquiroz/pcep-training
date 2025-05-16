#Solicita al usuario que ingrese su nombre, apellido y edad. 
# Crea un diccionario con esos datos y muestra por consola el mensaje "Hola, [nombre] [apellido]. Tienes [edad] años." 
# utilizando f-strings.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

datosUsuario = {
    "Nombre" : nombre,
    "Apellido" : apellido,
    "Edad" : edad
}

print(f"Hola, {datosUsuario['Nombre']} {datosUsuario['Apellido']}. Tienes {datosUsuario['Edad']}")