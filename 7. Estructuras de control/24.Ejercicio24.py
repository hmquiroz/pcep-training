#Pide al usuario que ingrese una cadena de texto. 
# Utiliza un bucle while para contar e imprimir la cantidad de vocales que hay en la cadena.

texto = input("Ingrese una cadena de texto: ")
vocales = "aeiouAEIOU"

contadorVocales = 0
i = 0

while i < len(texto):
    if texto[i] in vocales:
        contadorVocales += 1
    i += 1

print(f"La cadena de texto contiene {contadorVocales} vocales")