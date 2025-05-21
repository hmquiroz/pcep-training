'''
ZeroDivisionError: No se puede dividir un numero entre cero.
'''
try:
    x = 10
    y = 0
    resultado = x/y
    print(resultado)
except ZeroDivisionError:
    print("ERROR: No se puede dividir entre CERO")

try:
    numero = int("abc")
except ValueError:
    print("ERROR: No se puede convertir una cadena de texto a entero")