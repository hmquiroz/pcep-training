#Pide al usuario que ingrese un número entero. 
#Utiliza un condicional para determinar si el número es par o impar y muestra el resultado por consola. 
# Si el número es impar, también muestra su cuadrado.

numero = int(input("Ingresa un numero entero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par.")
else:
    print(f"El numero {numero} es impar.")
    print(f"El cuadrado del numero {numero} es: {numero ** 2}")