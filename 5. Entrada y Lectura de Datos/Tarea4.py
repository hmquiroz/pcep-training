#Pide al usuario que ingrese su nombre y apellido. 
#Luego, utiliza debanado y f-strings para crear y mostrar por consola un mensaje de bienvenida 
# que incluya solo la primera letra del nombre y del apellido, seguidas por un punto. 
# Por ejemplo, si el usuario ingresa "Ada Lovelace", el mensaje debería ser: "Bienvenida, A.L."

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")

iniciales = nombre[0].upper() + "." + apellido[0].upper() + "."

print(f"Bienvenida, {iniciales}")