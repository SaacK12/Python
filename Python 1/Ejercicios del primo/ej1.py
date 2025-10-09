def comprobar_valor_numerico(nmr):
    if nmr > 0:
        print("El numero introducido es positivo!")
    elif nmr == 0:
        print("El numero es 0 (cero)!")
    elif nmr < 0:
        print("El numero introducido es negativo!")

numero= input("Por favor, ingrese un numero (Positivo, negativo, o cero): ")
numero= int(numero)
comprobar_valor_numerico(numero)