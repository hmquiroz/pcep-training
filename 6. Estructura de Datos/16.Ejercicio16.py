#Solicita al usuario que ingrese cinco números enteros separados por espacios.
# Crea una lista con los números ingresados y calcula el promedio de los números en la lista.

numeros = input("Por favor, ingresa cinco numeros separados por espacios:")

listaNumeros = list(map(int, numeros.split()))

suma = sum(listaNumeros)
promedio = suma / len(listaNumeros)

print("El promedio de los numeros ingresados es:", promedio)