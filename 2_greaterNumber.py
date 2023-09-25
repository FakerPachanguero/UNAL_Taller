
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
