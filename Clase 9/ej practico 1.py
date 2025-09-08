def verificador (nmr):
    while True:
        if nmr.isdigit(): 
            return int(nmr)
            break
        else:
            nmr= input("Por favor, ingrese un número válido: ")
def maximo(nmr1, nmr2):
    print("El numero mayor es: ", max(nmr1,nmr2))

numeroUno= input("Introduzca el primer numero: ")
numeroUno= verificador(numeroUno)
numeroDos= input("Introduzca el segundo numero: ")
numeroDos= verificador(numeroDos)
maximo(numeroUno, numeroDos)