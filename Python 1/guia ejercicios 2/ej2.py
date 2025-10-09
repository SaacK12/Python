nombre= input("Introduzca su nombre/nombres: ")
while True:
    if nombre.isalpha:
        nombre= str(nombre)
        break
    else:
        nombre= input("Por favor ingrese un nombre/nombres valido: ")
apellido= input("Introduzca su apellido/apellidos: ")
while True:
    if apellido.isalpha:
        apellido= str(apellido)
        break
    else:
        apellido= input("Por favor ingrese un apellido/apellidos valido: ")
print(nombre.lower(), apellido.lower())
print(nombre.upper(), apellido.upper())
print(nombre.capitalize(), apellido.lower())
