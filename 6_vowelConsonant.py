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
