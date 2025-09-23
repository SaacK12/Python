def verificar_numero(nmr):
    while True:
        if nmr.isdigit():
            return nmr
        else:
            nmr= input("el numero introducido no es valido")
lista= []
def multiplicar(nmr):
    for i in range( 1, 11):
        print(nmr, "x", i, "=", numero * i,)

numero= input("Introduzca un numero para multiplicar: ")
numero= int(verificar_numero(numero))
multiplicar(numero)