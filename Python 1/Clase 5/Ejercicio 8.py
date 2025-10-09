numeroUno= int(input("Ingres un numero entero"))
while numeroUno < 0:
    numeroUno= int(input("Por favor intruzca un numero entero positivo"))
numeroDos= int(input("Ingrese otro numero entero"))
while numeroUno < 0:
    numeroUno= int(input("Por favor intruzca un numero entero positivos"))
cociente= numeroUno / numeroDos
resto= numeroUno % numeroDos
print("El cociente es", cociente)
print("El resto es", resto)