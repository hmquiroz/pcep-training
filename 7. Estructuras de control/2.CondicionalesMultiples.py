calificacion = 100

#<59 = Insuficiente
#60-70 = Bueno
#70-80 = Muy Bueno
#>90 = Excelente

if calificacion >= 90 and calificacion < 100:
    print("Excelente")
elif calificacion >= 80:
    print("Muy Bueno")
elif calificacion >= 70:
    print("Bueno")
elif calificacion >= 60:
    print("Suficiente")
else:
    print("Insuficiente")