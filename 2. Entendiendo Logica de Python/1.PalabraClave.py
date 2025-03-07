import keyword

print(keyword.kwlist)

palabra_clave = ['continue']

for palabra in keyword.kwlist:
    if palabra in palabra_clave:
        print('Se encontro palabra rerservada:' + palabra)        