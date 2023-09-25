
#VARIABLES

# Paises de America
countries = [
    "canadá", "estados unidos", "méxico",
    "belice", "costa rica", "el salvador", "guatemala", "honduras", "nicaragua", "panamá",
    "argentina", "bolivia", "brasil", "chile", "colombia", "ecuador", "paraguay", "perú",
    "surinam", "trinidad y tobago", "uruguay", "venezuela",
    "antigua y barbuda", "bahamas", "barbados", "cuba", "dominica", "granada", "guyana",
    "haití", "jamaica", "república dominicana", "san cristóbal y nieves", "san vicente y las granadinas", "santa lucía"
]

# Capitales de Amrica
capitals = [
    "otawwa", "washington dc", "méxico df",
    "belmopán", "san josé", "san salvador", "ciudad de guatemala", "tegucigalpa", "managua", "panamá",
    "buenos aires", "sucre", "brasilia", "santiago de chile", "bogotá", "quito", "asunción", "lima",
    "parabarimo", "puerto españa", "montevideo", "caracas",
    "saint john", "nasáu", "bridgetown", "la habana", "roseau", "saint george", "georgetown",
    "puerto príncipe", "kingston", "santo domingo", "basseterre", "kingstown", "castries"
]

p : chr = input("Ingresa el nombre de un país (en español y en minusculas): ")

#CODE

if p in countries:
    print(f"La capital de {p} es: {capitals[countries.index(p)]}")
