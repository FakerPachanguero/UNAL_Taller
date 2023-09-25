# Taller N°1

## En este repositorio encontraras toda una serie de funcionalidades básicas escritas en Python. En la siguiente imagen hallaras un notebook para interactuar con el código.
[![Texto alternativo](icon_nbGoogleColab.jpg )](https://colab.research.google.com/drive/1zVdAh0Uk3JzmpDuXlgGyu9Z7JXUjELDS?usp=sharing)


## 1). Dados tres números. Determina cual es el mayor.
> Para este programa sencillamente se hace uso el condicional "If" para comparar los 3 números.

```python
#VARIABLES
a : float = float(input("Ingrese un número real: "))
b : float = float(input("Ingrese un número real: "))
c : float = float(input("Ingrese un número real: "))

# CODE
if a > b:
    if a > c:
        print(a, " es el número mayor")
    else:
        print(c, " es el número mayor")   
else:
    if b > c:
        print(b, " es el número mayor")
    else:
        print(c, " es el número mayor")   
```


## 2). Determina si un número es par.
> Para determinar si un número es par, tan solo realizamos el modulo 2 del número, si la operación devuelve 0, significa que es el número es par
```python
#VARIABLES
n : float = float(input("Escribe un número Real: "))

#CODE
print(n, " es par") if n%2 == 0 else print (n, " No es par")
```


## 3). Determina si un número es multiplo de otro
>Al igual que en el punto anterior, realizamos la operación módulo pero esta vez entre los dos números, si el resultado es cero, significa que es multiplo.
```python
#VARIABLES
a : float = float(input("Escribe un número Real: "))
b : float = float(input("Escribe un número Real: "))

#CODE
print(a, " es multiplo de ", b) if a%b == o else print(a, " No es multiplo de ",b)
```

## 4). Dados tres números. Determina si la suma de los dos primeros es mayor que el tercero.
> Se realiza la suma de los números para posteriormente evaluar las 3 posibilidades con ayuda del condicional if
```python
#VARIABLES
a : float = float(input("Ingrese un número real: "))
b : float = float(input("Ingrese un número real: "))
c : float = float(input("Ingrese un número real: "))


#CODE
if a+b < c:
    print( f"La suma de {a} + {b} es menor que {c}" )
elif a+b == c:
    print( f"La suma de {a} + {b} es igual a {c}" )
elif a+b > c:
    print( f"La suma de {a} + {b} es mayor que {c}" )
```

## 5). Dada una letra. Determina si es una vocal o una consonante
>Para este programa se evalúa si el código ASCII de la letra está dentro del rango de las letras, si es así, se evalúa si es vocal o consonante, para ello se creó una lista de los códigos ASCII de las vocales, si el código de la letra coincide con alguno de la lista, significa que es vocal.
```python

#VARIABLES
c : str = str(input("Ingrese una letra: "))

lowVowelsAscii : [int] = [97,101,105,111,117]
highVowelsAcii : [int] = [65,69,73,79,85]


#CODE

if ord(c) >= 65 and ord(c) <= 90:
    if ord(c) in highVowelsAcii:
        print(f"La letra {c} es una vocal mayúscula" )
    else:
        print(f" {c} es una consonante mayúscula")
elif ord(c) >= 97 and ord(c) <= 122:
    if ord(c) in lowVowelsAscii:
        print(f"La letra {c} es una vocal minúscula" )
    else:
        print(f" {c} es una consonante minúscula")
else:
    print(f"{c} no es una letra")
```

## 6). Dados 5 números, realiza las siguientes operaciones
  - Promedio y promedio multiplicativo
  - Mediana
  - Los ordena de mayor a menor, y viceversa 
  - Halla la potencia del mayor número elevado al menor
  - Halla la raiz cúbica del número menor 
>
```python
#VARIABLES
# Lista donde se van a guardar los números
numbersList = []
# Número total de numeros en la lista
listLen : int
# Promedio del grupo de números
promedio : float = 0
# Promedio multiplicativo del grupo de números
promedioMul : float = 1
# Mediana del grupo de números
mediana : float = 0
# Número menor de la lista
lowNumber : float
# Número mayor de la lista
highNumber : float

# TEMP VARIABLES
n: float


#CODE

# pide 5 numeros y los guarda en una lista
for i in range (0,5):
    n = float(input("Digita un número: "))
    numbersList.append(n)


# Halla el promedio de la lista
for a in range (len(numbersList)):
    promedio = promedio + numbersList[a]
promedio = promedio/len(numbersList)
print(f"El promedio de la lista es: {promedio}")


# Ordenar menor a mayor
numbersList.sort()
print(f"Lista de números de menor a mayor {numbersList}")

# Ordenar de mayor a menor
numbersList.reverse()
print(f"Lista de números de mayor a menor {numbersList}")

# Preparar Variables
highNumber = numbersList[0]
lowNumber = numbersList[len(numbersList)-1]
listLen = len(numbersList)

# Promedio multiplicativo
for i in range (0, listLen -1):
    promedioMul = promedioMul * numbersList[i]
promedioMul = promedioMul**(1/listLen)
print(f"El promedio multiplicativo de la lista es: {promedioMul}")

# Mediana
mediana = numbersList[listLen//2]
print(f"La mediana de la lista de números es: {mediana} ")

# Potencia del mayor número elevado al menor
print(f"La potencia del número mayor elevado al menor es: {highNumber**lowNumber}")

# Raiz del del número menor
print(f"La raiz del número menor es: {lowNumber**0.5}")
```

## 7). Dada una frecuencia. Determina en que parte del espectro electromagnético se encuentra
>Para desarrollar este programa se tomó la información del siguiente link : https://es.wikipedia.org/wiki/Espectro_electromagn%C3%A9tico , siguiendo la tabla de bandas de espectro se realizo una cadena de elif, evaluando cada una de las diferentes regiones del espectro.
```python
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

```

## 8). Dado el nombre de un país de América en minúsculas, arroja su capital.
>En primer lugar de se crearon dos listas, una para los países y otra para las capitales, se evalúa si el país escrito esta dentro de la lista, si es correcto, se toma el index del país para buscarlo en la lista de capitales.
```python
#VARIABLES
# Paises de América
countries = [
    "canadá", "estados unidos", "méxico",
    "belice", "costa rica", "el salvador", "guatemala", "honduras", "nicaragua", "panamá",
    "argentina", "bolivia", "brasil", "chile", "colombia", "ecuador", "paraguay", "perú",
    "surinam", "trinidad y tobago", "uruguay", "venezuela",
    "antigua y barbuda", "bahamas", "barbados", "cuba", "dominica", "granada", "guyana",
    "haití", "jamaica", "república dominicana", "san cristóbal y nieves", "san vicente y las granadinas", "santa lucía"
]

# Capitales de América
capitals = [
    "otawwa", "washington dc", "méxico df",
    "belmopán", "san josé", "san salvador", "ciudad de guatemala", "tegucigalpa", "managua", "panamá",
    "buenos aires", "sucre", "brasilia", "santiago de chile", "bogotá", "quito", "asunción", "lima",
    "parabarimo", "puerto españa", "montevideo", "caracas",
    "saint john", "nasáu", "bridgetown", "la habana", "roseau", "saint george", "georgetown",
    "puerto príncipe", "kingston", "santo domingo", "basseterre", "kingstown", "castries"
]

# Nombre del país
p : chr = input("Ingresa el nombre de un país (en español y en minusculas): ")


#CODE
if p in countries:
    print(f"La capital de {p} es: {capitals[countries.index(p)]}")

```

## 9). A partir de una distancia, calcula cuanto tardaria en recorrerla :
  - La luz en el vacio
  - La velocidad del sonido en el aire
  - Un Koenigsegg Jesko Absolut
  - Usain Bolt
>Para este caso sencillamente se sigue la ecuación D = VT,  en donde D es igual a distancia, V es igual a velocidad y T es igual a tiempo. Se toma el dato de la distancia y  se evalúa en los cuatro casos.
```python
#VARIABLES

d : float = float(input("Digita una distancia en Km: "))

#* Velocidades dadas en Km/s
# Velocidad Max de la luz en el vacio
vLight : float = 299792
# Velocidad Max del sonido en el aire
vSound : float = 0.343
# velocidad Max del Koenigsegg Jesko Absolut
vCar : float = 0.1477
# Velocidad Max Usain Bolt
vBolt : float = 0.0124

#* CODE
if d > 0:
    print(" La luz tardaria ","{:.3g}".format(d/vLight), f"s en recorrer una distancia de {d}km ")
    print(" El sonido tarda ","{:.3g}".format(d/vSound), f"s en recorrer una distancia de {d}km ")
    print(" El auto Koenigsegg Jesko Absolut tarda ","{:.3g}".format(d/vCar), f"s en recorrer una distancia de {d}km ")
    print(" Usain Bold tarda ","{:.3g}".format(d/vBolt), f"s en recorrer una distancia de {d}km ")
else:
    print("La distancia tiene que ser mayor a 0 ")
```
