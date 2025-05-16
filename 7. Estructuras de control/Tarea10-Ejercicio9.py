#Pide al usuario que ingrese un número entero. 
# Utiliza un bucle for para calcular la suma de todos los números impares desde el 1 hasta el número ingresado, pero solo suma aquellos impares que son múltiplos de 3. Muestra por consola la suma de esos números impares.

numero = int(input("Por favor, ingrese un número entero: "))

suma = 0

for i in range(1, numero + 1, 2):
    if i % 3 == 0:
        suma += i

print(f"La suma de los números impares múltiplos de 3 desde 1 hasta {numero} es {suma}.")