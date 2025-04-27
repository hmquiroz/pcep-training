import copy

#copy : creamos copias modificables para no alterar la lista original
lista = [1, 2, 3, 4, 5]
copia = lista.copy()

print(lista)
print(copia)

copia.append(6)
print(copia)

copia.append(10)
print(copia)
print(lista)

#clonar : ambas listas son independientes
print("Clonacion \nLista 2")
lista2 = [1, 2, 3, 4, 5]
clonacion = copy.deepcopy(lista2)

lista2.append(6)
clonacion.append(10)
print(lista2)
print(clonacion)