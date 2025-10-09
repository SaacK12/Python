euro= input("Introduzca el precio del producto en euros con dos decimales.")
decimales= tuple(f".{i:00}" for i in range (100))
while True:
    if euro.endswith(decimales):
        euro= float(euro)
        parteEntera= int(euro)
        parteDecimal= euro - parteEntera
        print("Parte entera:",parteEntera)
        print("Parte decimal:",round(parteDecimal,2))
        break
    else:
        euro= input("El numero introducido no es valido, asegurece de que contenga al menos dos decimales.")