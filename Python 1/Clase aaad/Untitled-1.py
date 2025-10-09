usuario= input("Ingrese el usuario: ")
if usuario== ("admin") or usuario== ("profesor"):
    contraseña= input("Ingrese la contraseña:")
    if contraseña== ("1234"):
        nombre= input("Indique su nombre:")
        if nombre== (""):
            print ("El nombre se encuentra vacio.")
        else:
            print("¡Bienvenido, "+nombre+"!")
    else:
        print ("Contraseña invalida.")
else:
    print("Este usuario no es valido.")