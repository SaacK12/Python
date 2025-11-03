paises = {
    "ar":"argentina",
    "es":"España",
    "us":"Estados Unidos",
    "fr":"Francia"
}

while True:
    codigo = input("Ingrese un codigo: ")
    if codigo == "salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("El codigo introducido no existe.")