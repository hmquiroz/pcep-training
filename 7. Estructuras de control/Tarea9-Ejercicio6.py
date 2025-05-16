#Solicita al usuario que ingrese un número entero. 
# Utiliza un bucle while para calcular la suma de todos los números impares desde el 1 hasta el número ingresado, 
# pero solo suma aquellos impares que son múltiplos de 3. Muestra por consola la suma de esos números impares.

numero = int(input("Por favor, ingrese un número entero: "))

suma = 0
i = 1

while i <= numero:
    if i % 2 != 0 and i % 3 == 0:
        suma += i
    i += 1

print(f"La suma de los números impares múltiplos de 3 desde 1 hasta {numero} es {suma}.")