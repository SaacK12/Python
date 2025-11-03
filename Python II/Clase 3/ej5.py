import time
while True:
    print("Menú:")
    print("1 - Ingreso de empleado")
    print("2 – Egreso de empleado")
    print("3 - Mostrar los últimos 5 registros")
    print("4 - Salir del programa")
    opcion= input(">>> ")
    if opcion == "1":
        nombre= input("¿Quien ha Ingresado? ")
        hora= time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
        registro= f"{hora} - {nombre} ha Ingresado.\n"
        with open("registro - copia.txt", "a") as f:
            f.write(registro)
    elif opcion == "2":
        nombre= input("¿Quien ha Egresado? ")
        hora= time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
        registro= f"{hora} - {nombre} ha Egresado.\n"
        with open("registro - copia.txt", "a") as f:
            f.write(registro)
###### Mostrar los últimos 5 registros #####
    elif opcion == "3":
        try:
            with open("registro - copia.txt", "r") as f:
                eventos= f.readlines()
            if len(eventos) < 5:
                for r in eventos:
                    print("-" + r.strip())
            else:
                for r in eventos[-5:]:
                    print ("-" + r.strip())
        except FileNotFoundError:
            print("No hay registros que mostrar.")
###### Salir ######   
    elif opcion == "4":
        print("Gracias por usar nuestro programa.")
        break
##### Valores no validos del menu ######    
    else:
        print("Valor no valido")