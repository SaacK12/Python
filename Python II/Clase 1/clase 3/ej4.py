import time
f= open("registro.txt", "a")
while True:
    print("Menú:")
    print("1 - Ingreso de empleado")
    print("2 – Egreso de empleado")
    print("3 - Ver los ultimos cinco registros")
    print("4 - Salir del programa")
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
    if opcion == "4":
        print("Gracias por usar nuestro programa.")
        break
##### Valores no validos del menu ######    
    else:
        print("Valor no valido")
f.close()