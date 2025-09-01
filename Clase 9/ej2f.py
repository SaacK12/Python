numero= input("Introduzca un numero")
def verificacion(nro):
    while True:
        if nro.isdecimal():
            print("bien ahi")
            break
        else:
            nro= input("Error, el numero no es valido")
verificacion(numero)
