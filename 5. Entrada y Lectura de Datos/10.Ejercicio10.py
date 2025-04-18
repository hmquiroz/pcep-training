#Pide al usuario que ingrese dos números enteros. Utiliza operadores de comparación para determinar si el primer número es mayor que el segundo y muestra el resultado por pantalla.

numero1 = int(input("Por favor, ingrese el primer numero: "))
numero2 = int(input("Por favor, ingrese el segundo numero: "))

esMayor = numero1 > numero2

print("El primer numero es mayor que el segundo:", esMayor)