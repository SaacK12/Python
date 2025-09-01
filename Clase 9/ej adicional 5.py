import math
def verificador (nmr):
    while True:
        if nmr.isdigit(): 
            nmr = int(nmr)
            break
        else:
            nmr= input("Por favor, ingrese un número válido: ")
def factorial (nmr):
    nmr= int(nmr)
    resultado= math.factorial(nmr)
    print(resultado)

numero= (input("Introduzca el numero al cual quiera sacar el factorial: "))
verificador(numero)
factorial(numero)