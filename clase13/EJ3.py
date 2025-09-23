lista=[0, 1]
def formulaMatematicaZZZ(nro):
    fUno= 0
    fDos= 1
    while True:
        if len(lista) < 21:
            fDos= fUno + fDos
            lista.append(fDos)
            fUno= fUno + fDos
            lista.append(fUno)
        else:
            print(lista)
            break
numero= int(input("Introduzca un numero entero para la sucesión de Fibonacci: ")) #Quien es Fibonacci
while True:
    if numero < 2:
        numero= int(input("La cantidad debe ser mayor a 2. Intente de nuevo: "))
    else:
        formulaMatematicaZZZ(numero)
        break