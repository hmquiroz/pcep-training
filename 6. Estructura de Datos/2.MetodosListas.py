frutas = ['coco', 'kiwi', 'uva']

print(frutas)
frutas.append('manzana')
print(frutas)

frutas.insert(1, 'mango')
print(frutas)

frutas.remove('coco')
print(frutas)

print(len(frutas))

del frutas[2]
print(frutas)

numeros = [2, 1, 5, 6]

print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))
numeros.sort(reverse=True)
print(numeros)