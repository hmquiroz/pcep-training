variableGlobal = "Soy una variable global"

print(variableGlobal)

def miFuncion():
    variableLocal = "Soy una variable local"
    return variableLocal

print(miFuncion())
print(miFuncion())

def incrementarContador():
    global contador
    contador = 0
    #contador += 1
    #return contador 

print(incrementarContador())
print(contador)