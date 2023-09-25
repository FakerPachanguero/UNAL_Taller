
#VARIABLES
numbersList = []
listLen : int
n: float
promedio : float = 0
promedioMul : float = 1
mediana : float = 0
lowNumber : float
highNumber : float


#CODE

# pide 5 numeros y los guarda en una lista
for i in range (0,5):
    n = float(input("Digita un número: "))
    numbersList.append(n)



for a in range (len(numbersList)):
    promedio = promedio + a
promedio = promedio/2
print(promedio)


# Ordenar menor a mayor
numbersList.sort()
print (numbersList)

# Ordenar de mayor a menor
numbersList.reverse()
print(numbersList)

# Preparar Variables
lowNumber = numbersList[0]
highNumber = numbersList[len(numbersList)-1]
listLen = len(numbersList)

# Promedio multiplicativo
for i in range (0, listLen -1):
    promedioMul = promedioMul * numbersList[i]
promedioMul = promedioMul**(1/listLen)


# Mediana
mediana = numbersList[listLen//2]
print(f"La mediana de la lista de números es: {mediana} ")

# Potencia del mayor número elevado al menor
print(f"La potencia del número mayor elevado al menor es: {highNumber**lowNumber}")

# Raiz del del número menor
print(f"La raiz del número menor es: {lowNumber**0.5}")