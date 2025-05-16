#Solicita al usuario que ingrese una palabra. Utiliza un bucle for para mostrar por consola la palabra invertida.

palabra = input("Ingrese una palabra: ")
palabraInvertida = ""

for letra in palabra:
    palabraInvertida = letra + palabraInvertida

print(f"La palabra invertida es: {palabraInvertida}")