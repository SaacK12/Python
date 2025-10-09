numero= input("Ingrese un numero: ")
while True:
    if numero.isdecimal():
        print("Bien ahi")
        break
    else:
        numero= input("El numero caracter introducido no es valido. Intente de nuevo: ")