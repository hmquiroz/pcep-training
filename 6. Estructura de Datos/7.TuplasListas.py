#Se pueden combinar tuplas con listas como estructuras de datos.
#En este caso se puede tener una lista de tuplas
personas = [("Juan" , 25 , "M") , ("Maria" , 32 , "F") , ("Pedro" , 19 , "M")]

print(personas)
print(personas[0])
print(personas[2])
print(personas[1][0])
print(personas[0][1])

personas[0] = ("Walter" , 20 , "M")
print(personas)