def verificar_nombre(nombre):
    while True:
        if nombre.isalpha():
            nombre= str(nombre)
            return nombre
            break
        else:
            print("Por favor, ingrese un nombre de manera valida.")
            nombre= input("Ingresa el nombre: ")

                
def verificar_numero(numero):
    while True:
            if numero.isdigit(): 
                return int(numero)
                break
            else:
                print("Por favor, ingrese un numero de manera valida.")
                numero= input("Ingrese un numero para el pedido: ")

def cambio_de_turno(empleado):
    empleado = input("ingrese Nombre Del encargado ")
    return empleado

encargado = input("Ingrese Nombre Del encargado: ")
encargado= verificar_nombre(encargado)
while True:
    print(f"Welcome back {encargado} To The Los Pollos Hermanos Family")
    print("1. Ingresa Nuevo pedido")
    print("2. Cambio de turno")
    print("3. Apagar Sistema")
    opcion = input(">>> ")
    match opcion:
        case "1":
            #############################################################################################
            nombre= input("ingrese el nombre del cliente: ")
            verificar_nombre(nombre)

            combo1 = verificar_numero(input("Ingrese cantidad de Combo 1: "))

            combo2 = verificar_numero(input("Ingrese cantidad de Combo 2: "))

            combo3 = verificar_numero(input("Ingrese cantidad de Combo 3: "))

            postre = verificar_numero(input("Ingrese cantidad de Postre: "))

            PrecioCombo1 = 7

            PrecioCombo2 = 3

            PrecioCombo3 = 5

            PrecioPostre = 4

            totalCostoCombo1 = PrecioCombo1 * combo1

            totalCostoCombo2 = PrecioCombo2 * combo2

            totalCostoCombo3 = PrecioCombo3 * combo3

            totalCostoPostre = PrecioPostre * postre


            total= totalCostoCombo1 + totalCostoCombo2 + totalCostoCombo3 + totalCostoPostre

            print("el precio total del pedido es de $" , total)

            while True:
    
                paga= verificar_numero(input("Abona con $"))
                if paga < total:
                    print("¡¡¡ FALTA DINERO PARA COMPRAR EL PEDIDO !!!")
                else:
                    break    
            vuelto= paga - total

            print("el vuelto para el cliente es de $" , vuelto)


            while True:

                FinPedido=  input("¿Confirma pedido? Y/N : ").lower()
                match FinPedido:
                    case "y":
                        print(" ¡¡ Pedido Guardado !!") 
            
                        break 
                    case "n":
                        print("¡¡ Pedido Eliminado !!")
                        break
                    case _:
                        print("ERROR , Confirme el pedido con Y o no con N ")
        case "2":
            encargado= cambio_de_turno(encargado)
            encargado= verificar_nombre(encargado)
        case "3":
            print("¡¡Gracias por Trabajar en Los Pollos Hermanos!!")
            break
        case _:
            print("Opcion Invalida")