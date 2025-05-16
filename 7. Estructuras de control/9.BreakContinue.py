#Break:Detener el bucle en un punto especifico
#Continue: Saltarnos una iteracion
contador = 0

while contador <= 10:
    if contador == 6:
        break
    print("Contador:", contador)
    contador += 1

contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print("Numero Impar: ", contador)