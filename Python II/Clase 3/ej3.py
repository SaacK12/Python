def convertir_numero_a_float(nmr):
    while True:
        try:
            nmr= float(nmr)
            return nmr
        except ValueError:
            nmr= input("El numero que ha introducido no es un numero. Intente de nuevo:")
numero=input("Introduzca un numero: ")
numero= convertir_numero_a_float(numero)
print(numero)