import time
while True:
    print("Menú:")
    print("1 - Ingreso de empleado")
    print("2 – Egreso de empleado")
    print("3 - Salir del programa")
    f= open("registro.txt", "a")
    opcion= input(">>> ")
    if opcion == "1":
        nombre= input("¿Quien ha Ingresado? ")
        hora= time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
        registro= f"{hora} - {nombre} ha Ingresado.\n"
        f.write(registro)
    if opcion == "2":
        nombre= input("¿Quien ha Egresado? ")
        hora= time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
        registro= f"{hora} - {nombre} ha Egresado.\n"
        f.write(registro)
###### Salir ######   
    if opcion == "3":
        print("Gracias por usar nuestro programa.")
        break
##### Valores no validos del menu ######    
    if opcion != "1" and opcion != "2" and opcion != "3":
        print("Valor no valido")