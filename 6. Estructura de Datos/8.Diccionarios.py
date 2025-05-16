#Conjunto de datos ordenado y agrupado que tiene una llave y un valor
#Se puede modificar los valores

persona = {'nombre': 'Juan', 'edad': 28, 'ciudad': 'Madrid'}

print(persona)
print(persona['edad'])
print(persona['ciudad'])

persona['edad'] = 29
print(persona['edad'])

persona['profesion'] = 'Ingeniero'
print(persona)

del persona['nombre']
print(persona)