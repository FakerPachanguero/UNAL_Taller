#VARIABLES

d : float = float(input("Digita una distancia en Km: "))

#* Velocidades dadas en Km/s
# Velocidad Max de la luz en el vacio
vLight : float = 299792
# Velocidad Max del sonido en el aire
vSound : float = 0.343
# velocidad Max del Koenigsegg Jesko Absolut
vCar : float = 0.147
# Velocidad Max Usain Bolt
vBolt : float = 0.0124

# https://www.motor1.com/features/459605/fastest-cars-in-the-world/   revista

#* CODE

print("La luz tardaria ","{:.3g}".format(d/vLight), f"s en recorrer una distancia de {d}km ")
print(" El sonido tarda ","{:.3g}".format(d/vSound), f"s en recorrer una distancia de {d}km ")
print(" El auto Koenigsegg Jesko Absolut tarda ","{:.3g}".format(d/vCar), f"s en recorrer una distancia de {d}km ")
print(" Usain Bold tarda ","{:.3g}".format(d/vBolt), f"s en recorrer una distancia de {d}km ")