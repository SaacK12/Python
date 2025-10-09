import math
def sumar(nmr):
    numeros= [int(n) for n in nmr.split()]
    print(sum(numeros))

def multiplicar(nmr):
    numeros= [int(n) for n in nmr.split()]
    print(math.prod(numeros))

entrada= input("Introduzca la lista de numeros (Separados por un espacio): ")
sumar(entrada)
multiplicar(entrada)
