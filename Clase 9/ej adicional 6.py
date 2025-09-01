def verificadorNombre (nmb):
    while True:
        if nmb.isalpha(): #Esto verifica que el nombre sea solo letras
            nmb= str(nmb)
            break
        else:
            nmb= input("Por favor, ingrese un nombre válido: ")
def verificadorEdad (nmr):
    while True:
        if nmr.isdigit(): 
            nmr = int(nmr)
            break
        else:
            nmr= input("Por favor, ingrese un número válido: ")
diccionario={}
idUsuario= 1
while True:
    print("1. Agregar.")
    print("2. Mostrar el más chico.")
    print("3. Mostrar el más grande.")
    print("4. Salir.")
    numero = (input(">>"))
    if numero == "1":
        print("Registrar usuario")
        nombre= input("Agregue el nombre: ")
        verificadorNombre(nombre)
        edad= input("Agregar edad: ")
        verificadorEdad(edad)
        diccionario[idUsuario]= {"Nombre": nombre, "Edad": edad}
        idUsuario += 1
    elif numero == "2":
        aux_id= min(diccionario, key=lambda k: int(diccionario[k]["Edad"]))
        print(diccionario[aux_id]["Nombre"]+" Es la persona mas pequeña")
    elif numero == "3":
        aux_id = max(diccionario, key=lambda k: int(diccionario[k]["Edad"]))
        print(diccionario[aux_id]["Nombre"] +" Es la persona más grande")
    elif numero == "4":
        print("Dale tomate el palo")
        break
    else:
        print("Error!!")