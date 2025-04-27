#Crea una lista con los nombres de 5 amigos y muestra el nombre del primer y último amigo utilizando índices. 
# Luego, calcula cuántos caracteres tienen esos nombres y muestra los resultados por consola.

amigos = ["Carlos", "Ana", "Pedro", "Monica", "Luis"]

primerAmigo = amigos[0]
ultimoAmigo = amigos[-1]

longitudPrimerAmigo = len(primerAmigo)
longitudUltimoAmigo = len(ultimoAmigo)

print("El primer amigo en la lista es:", primerAmigo)
print("El ultimo amigo de la lista es:", ultimoAmigo)
print("El primer amigo tiene", longitudPrimerAmigo, "caracteres")
print("El ultimo amigo tiene", longitudUltimoAmigo, "caracteres")