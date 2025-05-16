#Crea una función llamada es_primo que reciba un número entero como parámetro y retorne True si el número es primo, 
# de lo contrario, retorne False. 
# Pide al usuario que ingrese un número entero y utiliza la función es_primo para determinar si es primo o no. 
# Muestra el resultado por consola.

def esPrimo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False 
        return True

numero = int(input("Ingresa un numero entero: "))

if esPrimo(numero):
    print("ES PRIMO")
else:
    print("NO ES PRIMO")