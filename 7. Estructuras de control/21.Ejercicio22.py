#Solicita al usuario que ingrese una cadena de texto. Utiliza un condicional para determinar si la cadena tiene una longitud mayor a 10 caracteres. Si es mayor a 10 caracteres, muestra por consola la cadena en mayúsculas. Si no, muestra la cadena en minúsculas.

texto = input("Ingrese una cadena de texto: ")

if len(texto) > 10:
    print(texto.upper())
else:
    print(texto.lower())