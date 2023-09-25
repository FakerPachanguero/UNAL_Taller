
#VARIABLES
a : float = float(input("Escribe un número Real: "))
b : float = float(input("Escribe un número Real: "))


#CODE
print(a, " es multiplo de ", b) if a%b == 0 else print(a, " No es multiplo de ",b)
