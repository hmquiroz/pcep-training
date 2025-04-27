#Crea una variable que represente tu altura en metros y otra que represente tu peso en kilogramos. Calcula tu índice de masa corporal (IMC) utilizando la fórmula: 

# IMC = peso / (altura^2). 

# Muestra el resultado por consola utilizando f-strings.

altura = 1.80
peso = 65

IMC = peso / (altura ** 2)

print(f"Mi altura es {altura} metros. Mi peso es {peso} kilogramos. Mi indice de masa corporal es de: {IMC:.3f}")