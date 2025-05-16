#Crea una función llamada ocurrencias que reciba una cadena de texto y un carácter como parámetros, 
# y retorne la cantidad de veces que aparece el carácter en la cadena. 
# 
# Pide al usuario que ingrese una cadena de texto y un carácter, y utiliza la función ocurrencias para calcular
#  la cantidad de veces que aparece el carácter en la cadena. Muestra el resultado por consola.

def ocurrencias(texto, caracter):
    return texto.count(caracter)

cadena = input("Por favor, ingrese una cadena de texto: ")
caracter = input("Por favor, ingrese un carácter: ")

resultado = ocurrencias(cadena, caracter)
print(f"El carácter '{caracter}' aparece {resultado} veces en la cadena.")