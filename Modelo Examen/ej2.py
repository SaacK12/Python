personas= []

def agregar (personas, **kwars):
    personas.append(kwars)

def busqueda(ps):
    mas_chico= 999999
    mas_chico_nombre=""
    for nombre in ps:
        if nombre["edad"] < mas_chico:
            mas_chico= nombre["edad"]
            mas_chico_nombre= nombre["nombre"]
            print("El mas chico es: ", mas_chico_nombre)
while True:
    print("Seleccione una opcion")
    print("1. Agregar")
    print("2. Mostrar el mas chico")
    print("3. Mostrar el mas grande.")
    print("4. Salir.")
    opcion= input(">>>")
    if opcion == "1":
        nombre= input("Introduzca el nombre")
        edad= int(input("Introduzca la edad"))
        agregar(personas, nombre=nombre, edad=edad)
    if opcion == "2":
        busqueda(personas)
    if opcion == "4":
        break