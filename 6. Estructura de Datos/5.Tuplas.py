#Es una agrupacion de datos (como una lista), pero no se pueden modificar.
colores = ('rojo' , 'verde' , 'azul')

print(colores)
print(colores[0])
print(colores[2])
print(colores[0 : 2])

lista = [1 , 2 , 3]
print(lista)
lista[0] = 10
print(lista)

coloresPrimarios = ('rojo' , 'verde' , 'azul')
coloresSecundarios = ('amarillo' , 'celeste' , 'cian')

coloresTotales = coloresPrimarios + coloresSecundarios
print(coloresTotales)