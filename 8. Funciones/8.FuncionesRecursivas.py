#Funcion Recursica que dentro de sus instrucciones se llama a si misma generando como un bucle hasta que no se cumple una condicion.
numero = int(input("Ingresa un numero entero: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(numero))