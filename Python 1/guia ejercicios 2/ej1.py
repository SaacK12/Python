nombre= input("Introduzca un nombre")
while True:
    if nombre.isalpha():
        nombre= str(nombre)
        break
    else:
        nombre= input("Por favor, ingrese un nombre valido: ")
numero= input("introduzca ahora un numero")
while True:
    if numero.isdigit():
        numero= int(numero)
        break
    else:
        numero= input("Por favor introduzca un numero valido")
vueltas= 0
while vueltas < numero:
    print(nombre)
    vueltas= vueltas + 1