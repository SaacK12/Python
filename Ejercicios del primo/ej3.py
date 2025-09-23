def verificar_numero(nmr):
    while True:
        if nmr.isdigit():
            return nmr
        else:
            nmr= input("el numero introducido no es valido")
def verificar_edad(nmr):
    while True:
        if nmr > 18:
            print("acceso permitido")
        else:
            print("Debes ser mayor de edad para poder acceder a este contenido")
edad= input("Por favor introduce tu edad: ")
edad= verificar_numero(edad)