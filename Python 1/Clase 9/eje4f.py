numero= input("Ingrese un numero")
def convertir(valor):

    while valor.isdecimal() == False:
        print("¡Error solo numeros enteros!")

        valor = input("Ingrese nuevamente el valor: ")

        valor = int(valor)
        return valor
convertir(numero)