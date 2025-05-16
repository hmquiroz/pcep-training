saldo = 500
retiro = 800

if saldo >= retiro:
    print("El retiro fue exitoso!")
else:
    if saldo >= (retiro - 100):
        print("Retiro exitoso con un limite de sobregiro permitido")
    else:
        print("Fondos insuficientes")