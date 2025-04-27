#Crea tres variables con números enteros y calcula lo siguiente:

# El producto de los tres números.

# La suma del primero y el segundo número, dividida por el tercer número.

# El promedio de los tres números.

# Muestra los resultados por consola utilizando f-strings.

numero1 = 100
numero2 = 200
numero3 = 300

producto = numero1 * numero2 * numero3
sumaDividida = (numero1 + numero2) / numero3
promedio = (numero1 + numero2 + numero3) / 3

print(f"El producto de los numeros {numero1}, {numero2}, {numero3} es de: {producto}")
print(f"La suma del primer numero y segundo numero, dividida entre el tercer numero es de: {sumaDividida}")
print(f"El promedio de los numeros {numero1}, {numero2}, {numero3} es de: {promedio}")