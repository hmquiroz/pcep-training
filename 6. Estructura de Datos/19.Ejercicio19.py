#Crea un diccionario con tres pares clave-valor que representen el nombre, apellido y edad de una persona. 
# Además, añade una clave "amigos" con una lista de nombres de tres amigos. Muestra por consola el valor de la clave "nombre" y el nombre del segundo amigo de la lista.

persona = {
    "Nombre" : "Juan",
    "Apellido" : "Perez",
    "Edad" : 20,
    "Amigos" : ["Carlos", "Ana", "Pedro"]
}

nombre = persona["Nombre"]
segundoAmigo = persona["Amigos"][1]

print("El nombre de la persona es: ",nombre)
print("El segundo amigo de la lista es: ",segundoAmigo)