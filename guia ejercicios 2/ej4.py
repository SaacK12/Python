prefijo="+34-"
extension= tuple(f"-{i:02}" for i in range (100))
numero= input("Introduzca el numero de telefono:" )
while True:
    if numero.startswith(prefijo) and numero.endswith(extension):
        numero= str(numero)
        break
    else:
        numero= input("Por favor introduzca un numero valido con el prefijo y con la extensión" )
print(numero[4:] [:-3])