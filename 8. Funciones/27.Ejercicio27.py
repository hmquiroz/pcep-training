#Crea una función llamada saludar que reciba un nombre como parámetro y retorne un saludo con el nombre ingresado. 
# Luego, pide al usuario que ingrese su nombre y utiliza la función saludar para mostrar el saludo por consola.

def saludar(nombre):
    return f"Hola, {nombre}"

nombreUsuario = input("Ingrese su nombre: ")
print(saludar(nombreUsuario))