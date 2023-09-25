#VARIABLES
frecuencia : float = eval(input("Ingresa una frecuencia de onda en hz: "))


#CODE
if frecuencia > 3*10**19:
    print(f"Tu frecuencia {frecuencia} está asociada a los rayos gamma") 
elif frecuencia > 3*10**16:
    print(f"Tu frecuencia {frecuencia} está asociada a los rayos X")
elif frecuencia > 1.5*10**16:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Ultravioleta extrema")
elif frecuencia > 3*10**15:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Ultravioleta cercana")
elif frecuencia > 7.5*10**14:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación del Espectro Visible")
elif frecuencia > 120*10**12:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Infrarrojo cercano")
elif frecuencia > 6*10**12:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Infrarrojo medio")
elif frecuencia > 300*10**9:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Infrarrojo lejano/submilimétrico")
elif frecuencia > 3*10**8:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Microondas")
elif frecuencia > 300*10**6:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Ultra Alta Frecuencia-Radio")
elif frecuencia > 30*10**6: 
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Muy Alta Frecuencia-Radio")
elif frecuencia > 1.6*10**6:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Onda Corta - Radio")
elif frecuencia > 650*10**3:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Onda Media - Radio")
elif frecuencia > 30*10**3:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Onda Larga - Radio")
elif frecuencia < 30*10**3:
    print(f"Tu frecuencia {frecuencia} está asociada a la radiación Muy Baja Frecuencia - Radio")
